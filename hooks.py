"""Small build hooks for bilingual page metadata."""

import re


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
