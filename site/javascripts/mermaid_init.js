// Mermaid initialization for MkDocs Material
// Supports dark/light theme switching
(function () {
  function getTheme() {
    var palette = document.querySelector('[data-md-color-scheme]');
    if (palette) {
      var scheme = palette.getAttribute('data-md-color-scheme');
      return scheme === 'slate' ? 'dark' : 'default';
    }
    return 'default';
  }

  function initMermaid() {
    if (typeof mermaid !== 'undefined') {
      mermaid.initialize({
        startOnLoad: true,
        theme: getTheme(),
        themeVariables: {
          primaryColor: '#eef2ff',
          primaryTextColor: '#1e293b',
          primaryBorderColor: '#6366f1',
          lineColor: '#6366f1',
          secondaryColor: '#f1f5f9',
          tertiaryColor: '#f8fafc',
          fontFamily: 'Inter, ui-sans-serif, -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif'
        },
        flowchart: {
          useMaxWidth: true,
          htmlLabels: true,
          curve: 'basis'
        },
        gantt: {
          useMaxWidth: true
        },
        sequence: {
          useMaxWidth: true
        }
      });

      // Re-render on theme switch
      var observer = new MutationObserver(function () {
        var theme = getTheme();
        mermaid.initialize({ theme: theme });
        // Re-render all mermaid diagrams
        document.querySelectorAll('.mermaid').forEach(function (el) {
          var code = el.textContent;
          el.removeAttribute('data-processed');
          el.innerHTML = code;
        });
        if (typeof mermaid.run === 'function') {
          mermaid.run();
        }
      });

      var paletteEl = document.querySelector('body');
      if (paletteEl) {
        observer.observe(paletteEl, {
          attributes: true,
          attributeFilter: ['data-md-color-scheme']
        });
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMermaid);
  } else {
    initMermaid();
  }
})();
