"""Small build hooks for bilingual metadata and static asset cache busting."""

import hashlib
import html as html_lib
import logging
import posixpath
import re
from pathlib import Path
from urllib.parse import unquote_plus, urlsplit, urlunsplit


_LOG = logging.getLogger("mkdocs.hooks.cache_busting")
_HASH_LENGTH = 12
_CSS_ASSETS = (
    "stylesheets/extra.css",
    "aml2024/archive.css",
)
_LINK_TAG_RE = re.compile(r"<link\b[^>]*>", re.IGNORECASE | re.DOTALL)
_HREF_RE = re.compile(
    r"(?P<prefix>\bhref\s*=\s*)(?P<quote>[\"'])(?P<url>.*?)(?P=quote)",
    re.IGNORECASE | re.DOTALL,
)


def on_post_page(output, *, page, config):
    """Declare Chinese pages as zh-CN without changing existing page URLs."""
    if not page.file.src_uri.endswith("_zh.md"):
        return output

    output = output.replace('<html lang="en"', '<html lang="zh-CN"', 1)
    output = output.replace('aria-label="Table of contents"', 'aria-label="目录"')
    output = re.sub(
        r"(?P<before>>\s*)Table of contents(?P<after>\s*<)",
        r"\g<before>目录\g<after>",
        output,
    )
    output = re.sub(
        r"(?P<before>>\s*)Skip to content(?P<after>\s*<)",
        r"\g<before>跳到正文\g<after>",
        output,
    )
    return output


def _content_hash(path):
    """Return a short SHA-256 digest for one built asset."""
    return hashlib.sha256(path.read_bytes()).hexdigest()[:_HASH_LENGTH]


def _site_relative_asset(url_path, html_directory, site_url_prefix):
    """Resolve a local URL path to a path relative to the built site root."""
    if url_path.startswith("/"):
        normalized = posixpath.normpath(url_path).lstrip("/")
        if site_url_prefix:
            prefix = site_url_prefix + "/"
            if normalized.startswith(prefix):
                normalized = normalized[len(prefix) :]
        return normalized

    normalized = posixpath.normpath(posixpath.join(html_directory, url_path))
    if normalized == ".." or normalized.startswith("../"):
        return None
    return normalized


def _versioned_url(url, html_directory, site_url_prefix, hashes):
    """Add or replace the v query parameter for a known local CSS asset URL."""
    decoded_url = html_lib.unescape(url)
    try:
        parts = urlsplit(decoded_url)
    except ValueError:
        return url
    if parts.scheme or parts.netloc:
        return url

    asset = _site_relative_asset(parts.path, html_directory, site_url_prefix)
    if asset not in hashes:
        return url

    query_parts = []
    if parts.query:
        query_parts = [
            item
            for item in parts.query.split("&")
            if unquote_plus(item.split("=", 1)[0]).lower() != "v"
        ]
    query_parts.append("v=" + hashes[asset])

    versioned_url = urlunsplit(
        (parts.scheme, parts.netloc, parts.path, "&".join(query_parts), parts.fragment)
    )
    return html_lib.escape(versioned_url, quote=True)


def _version_stylesheets(html, html_directory, site_url_prefix, hashes):
    """Rewrite only known CSS hrefs inside link tags."""
    replacements = 0

    def replace_link(tag_match):
        tag = tag_match.group(0)

        def replace_href(href_match):
            nonlocal replacements
            old_url = href_match.group("url")
            new_url = _versioned_url(
                old_url, html_directory, site_url_prefix, hashes
            )
            if new_url == old_url:
                return href_match.group(0)
            replacements += 1
            return (
                href_match.group("prefix")
                + href_match.group("quote")
                + new_url
                + href_match.group("quote")
            )

        return _HREF_RE.sub(replace_href, tag)

    return _LINK_TAG_RE.sub(replace_link, html), replacements


def on_post_build(config, **kwargs):
    """Version selected built CSS URLs from each file's SHA-256 content hash."""
    site_dir = Path(config.site_dir)
    hashes = {}
    for asset in _CSS_ASSETS:
        asset_path = site_dir / Path(asset)
        if not asset_path.is_file():
            raise RuntimeError("Built CSS asset is missing: {}".format(asset_path))
        hashes[asset] = _content_hash(asset_path)

    site_url_prefix = urlsplit(config.site_url or "").path.strip("/")
    replacement_count = 0
    changed_files = 0

    for html_path in sorted(site_dir.rglob("*.html")):
        html = html_path.read_text(encoding="utf-8")
        html_directory = html_path.relative_to(site_dir).parent.as_posix()
        if html_directory == ".":
            html_directory = ""
        versioned_html, replacements = _version_stylesheets(
            html, html_directory, site_url_prefix, hashes
        )
        if replacements:
            html_path.write_text(versioned_html, encoding="utf-8")
            replacement_count += replacements
            changed_files += 1

    _LOG.info(
        "Versioned %d CSS references in %d HTML files: %s",
        replacement_count,
        changed_files,
        ", ".join("{}={}".format(asset, digest) for asset, digest in hashes.items()),
    )
