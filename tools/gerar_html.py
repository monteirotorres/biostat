"""Gera um único HTML moderno e interativo com todo o conteúdo do curso.

Lê SUMMARY.md, monta a navegação e embarca todos os markdowns
em <script type="text/markdown"> para renderização no cliente
(marked + KaTeX + highlight.js + Mermaid).
"""

import re
from pathlib import Path

BASE = Path(__file__).parent.parent
SUMMARY = BASE / "SUMMARY.md"
OUT = BASE / "bioestatistica.html"


def parse_summary():
    """Lê o SUMMARY.md e devolve [(section_title, [(item_title, path)])]."""
    section, sections = None, []
    items = []
    for line in SUMMARY.read_text(encoding="utf-8").splitlines():
        m_h2 = re.match(r"^##\s+(.+)$", line)
        m_item = re.match(r"^\*\s+\[(.+?)\]\((.+?)\)$", line)
        if m_h2:
            if section is not None:
                sections.append((section, items))
            section = m_h2.group(1).strip()
            items = []
        elif m_item:
            title, path = m_item.group(1).strip(), m_item.group(2).strip()
            if path.startswith("0"):  # ignora o README
                items.append((title, path))
    if section is not None:
        sections.append((section, items))
    return sections


def slugify(path: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")


def main():
    sections = parse_summary()

    nav_html = []
    main_html = []

    for sec_title, items in sections:
        nav_html.append(f'<div class="nav-section"><h3>{sec_title}</h3><ul>')
        for title, path in items:
            slug = slugify(path)
            nav_html.append(
                f'<li><a href="#{slug}" data-target="{slug}">{title}</a></li>'
            )
            md = (BASE / path).read_text(encoding="utf-8")
            ipynb_path = path.replace(".md", ".ipynb")
            main_html.append(f'''<article id="{slug}" class="topic" data-section="{sec_title}">
  <div class="topic-meta">
    <span class="badge">{sec_title}</span>
    <a class="nb-link" href="{ipynb_path}" target="_blank" rel="noopener">notebook ↗</a>
  </div>
  <script type="text/markdown" data-target="{slug}-content">{md}</script>
  <div id="{slug}-content" class="markdown-body"></div>
</article>''')
        nav_html.append("</ul></div>")

    html = TEMPLATE.replace("__NAV__", "\n".join(nav_html))
    html = html.replace("__MAIN__", "\n".join(main_html))
    OUT.write_text(html, encoding="utf-8")
    print(f"Gerado: {OUT}  ({OUT.stat().st_size / 1024:.1f} KB)")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bioestatística — IBCCF / UFRJ</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github.min.css" id="hljs-light">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github-dark.min.css" id="hljs-dark" disabled>
<style>
:root {
  --bg: #ffffff;
  --bg-soft: #f7f8fa;
  --bg-elev: #ffffff;
  --text: #1a1d23;
  --text-soft: #555a65;
  --text-mute: #8a909c;
  --border: #e6e8ec;
  --primary: #2563eb;
  --primary-soft: #dbeafe;
  --accent: #7c3aed;
  --code-bg: #f4f5f7;
  --sidebar-w: 320px;
  --header-h: 60px;
  --content-max: 760px;
}
[data-theme="dark"] {
  --bg: #0f1115;
  --bg-soft: #161922;
  --bg-elev: #1a1e28;
  --text: #e8eaef;
  --text-soft: #b3b8c4;
  --text-mute: #7d8392;
  --border: #2a2f3a;
  --primary: #60a5fa;
  --primary-soft: #1e3a5f;
  --accent: #a78bfa;
  --code-bg: #161922;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: calc(var(--header-h) + 20px); }
body {
  margin: 0;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  transition: background 0.2s, color 0.2s;
}
code, pre { font-family: 'JetBrains Mono', ui-monospace, monospace; }

/* Header */
header.topbar {
  position: fixed; top: 0; left: 0; right: 0; height: var(--header-h);
  background: rgba(255,255,255,0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; padding: 0 24px; gap: 16px;
  z-index: 100;
}
[data-theme="dark"] header.topbar { background: rgba(15,17,21,0.85); }
header h1 {
  margin: 0; font-size: 1.05rem; font-weight: 600;
  display: flex; align-items: center; gap: 10px;
}
header h1::before {
  content: ""; width: 28px; height: 28px;
  background: linear-gradient(135deg, var(--primary), var(--accent));
  border-radius: 8px;
  display: inline-block;
}
.header-spacer { flex: 1; }
.header-actions { display: flex; gap: 8px; align-items: center; }
.btn-icon {
  background: transparent; border: 1px solid var(--border);
  color: var(--text-soft); cursor: pointer;
  width: 36px; height: 36px; border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  transition: all 0.15s;
}
.btn-icon:hover { background: var(--bg-soft); color: var(--text); }

/* Sidebar */
nav.sidebar {
  position: fixed; left: 0; top: var(--header-h); bottom: 0;
  width: var(--sidebar-w);
  background: var(--bg-soft);
  border-right: 1px solid var(--border);
  overflow-y: auto;
  padding: 20px 0;
  transition: transform 0.25s;
}
.search-box {
  padding: 0 20px 16px; position: sticky; top: 0;
  background: var(--bg-soft); z-index: 2;
}
.search-box input {
  width: 100%; padding: 9px 12px; border-radius: 8px;
  border: 1px solid var(--border); background: var(--bg);
  font-family: inherit; font-size: 0.9rem; color: var(--text);
}
.search-box input:focus { outline: 2px solid var(--primary); outline-offset: -1px; }
.nav-section { padding: 0 12px 18px; }
.nav-section h3 {
  font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--text-mute); padding: 8px 12px; margin: 0;
  font-weight: 600;
}
.nav-section ul { list-style: none; padding: 0; margin: 0; }
.nav-section li a {
  display: block; padding: 7px 12px; border-radius: 6px;
  color: var(--text-soft); text-decoration: none; font-size: 0.92rem;
  border-left: 2px solid transparent; transition: all 0.15s;
}
.nav-section li a:hover { background: var(--bg-elev); color: var(--text); }
.nav-section li a.active {
  background: var(--primary-soft); color: var(--primary);
  border-left-color: var(--primary); font-weight: 500;
}
.nav-section li.hidden, .nav-section.hidden { display: none; }

/* Main content */
main {
  margin-left: var(--sidebar-w);
  padding: calc(var(--header-h) + 40px) 48px 80px;
}
.content-wrap { max-width: var(--content-max); margin: 0 auto; }

article.topic {
  padding-bottom: 60px;
  margin-bottom: 60px;
  border-bottom: 1px solid var(--border);
  scroll-margin-top: calc(var(--header-h) + 20px);
}
article.topic:last-child { border-bottom: none; }
.topic-meta {
  display: flex; align-items: center; gap: 12px;
  margin-bottom: 8px;
}
.badge {
  font-size: 0.72rem; padding: 3px 10px; border-radius: 999px;
  background: var(--primary-soft); color: var(--primary);
  font-weight: 500; letter-spacing: 0.02em;
}
.nb-link {
  font-size: 0.82rem; color: var(--text-mute);
  text-decoration: none; padding: 2px 8px;
  border-radius: 6px; border: 1px solid var(--border);
  transition: all 0.15s;
}
.nb-link:hover { color: var(--primary); border-color: var(--primary); }

/* Markdown styles */
.markdown-body h1 {
  font-size: 2rem; font-weight: 700; margin: 0 0 24px;
  letter-spacing: -0.02em; line-height: 1.25;
}
.markdown-body h2 {
  font-size: 1.4rem; font-weight: 600; margin: 36px 0 14px;
  letter-spacing: -0.01em;
}
.markdown-body h3 {
  font-size: 1.1rem; font-weight: 600; margin: 24px 0 10px;
}
.markdown-body p { margin: 0 0 14px; color: var(--text); }
.markdown-body ul, .markdown-body ol { margin: 0 0 14px; padding-left: 24px; }
.markdown-body li { margin-bottom: 4px; }
.markdown-body strong { font-weight: 600; }
.markdown-body em { font-style: italic; }
.markdown-body blockquote {
  margin: 18px 0; padding: 12px 18px;
  border-left: 3px solid var(--primary);
  background: var(--bg-soft); border-radius: 0 8px 8px 0;
  color: var(--text-soft);
}
.markdown-body blockquote p:last-child { margin: 0; }
.markdown-body code {
  background: var(--code-bg); padding: 2px 6px; border-radius: 4px;
  font-size: 0.88em;
}
.markdown-body pre {
  background: var(--code-bg); padding: 16px; border-radius: 10px;
  overflow-x: auto; margin: 16px 0;
  border: 1px solid var(--border);
  position: relative;
}
.markdown-body pre code { background: none; padding: 0; font-size: 0.88rem; }
.markdown-body table {
  border-collapse: collapse; margin: 18px 0;
  font-size: 0.92rem; width: 100%;
}
.markdown-body th, .markdown-body td {
  padding: 8px 14px; border: 1px solid var(--border);
  text-align: left;
}
.markdown-body th {
  background: var(--bg-soft); font-weight: 600;
}
.markdown-body tr:nth-child(even) td { background: var(--bg-soft); }
.markdown-body hr {
  border: 0; border-top: 1px solid var(--border); margin: 28px 0;
}
.markdown-body a { color: var(--primary); }

/* Copy button on code blocks */
.code-copy {
  position: absolute; top: 8px; right: 8px;
  background: var(--bg); border: 1px solid var(--border);
  color: var(--text-mute); padding: 4px 10px;
  border-radius: 6px; cursor: pointer; font-size: 0.75rem;
  font-family: inherit; opacity: 0; transition: opacity 0.15s;
}
.markdown-body pre:hover .code-copy { opacity: 1; }
.code-copy:hover { color: var(--primary); border-color: var(--primary); }
.code-copy.copied { color: var(--primary); border-color: var(--primary); }

/* Mermaid */
.mermaid { text-align: center; margin: 20px 0; }

/* KaTeX */
.katex-display { overflow-x: auto; overflow-y: hidden; padding: 6px 0; }
.katex { font-size: 1.05em; }

/* Hero */
.hero {
  text-align: center; padding: 40px 20px 60px;
  border-bottom: 1px solid var(--border); margin-bottom: 40px;
}
.hero h1 {
  font-size: 2.8rem; font-weight: 700; margin: 0 0 12px;
  background: linear-gradient(135deg, var(--primary), var(--accent));
  -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: -0.02em;
}
.hero p { color: var(--text-soft); max-width: 600px; margin: 0 auto 8px; }
.hero .authors {
  margin-top: 20px; font-size: 0.9rem; color: var(--text-mute);
}

/* Progress bar */
.progress {
  position: fixed; top: var(--header-h); left: 0; right: 0;
  height: 2px; z-index: 99;
}
.progress-bar {
  height: 100%; background: linear-gradient(90deg, var(--primary), var(--accent));
  width: 0%; transition: width 0.1s;
}

/* Mobile */
.menu-toggle { display: none; }
@media (max-width: 900px) {
  nav.sidebar { transform: translateX(-100%); z-index: 90; box-shadow: 4px 0 12px rgba(0,0,0,0.1); }
  nav.sidebar.open { transform: translateX(0); }
  main { margin-left: 0; padding: calc(var(--header-h) + 24px) 20px 60px; }
  .menu-toggle { display: flex; }
  .hero h1 { font-size: 2rem; }
}

/* Empty state */
.no-results {
  text-align: center; color: var(--text-mute); padding: 40px;
  display: none;
}
.no-results.show { display: block; }
</style>
</head>
<body>

<header class="topbar">
  <button class="btn-icon menu-toggle" id="menuToggle" aria-label="Menu">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
  </button>
  <h1>Bioestatística</h1>
  <div class="header-spacer"></div>
  <div class="header-actions">
    <button class="btn-icon" id="themeToggle" aria-label="Alternar tema">
      <svg id="iconSun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.93 4.93l1.41 1.41m11.32 11.32l1.41 1.41M2 12h2m16 0h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
      <svg id="iconMoon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
    </button>
  </div>
</header>
<div class="progress"><div class="progress-bar" id="progressBar"></div></div>

<nav class="sidebar" id="sidebar">
  <div class="search-box">
    <input type="search" id="search" placeholder="Buscar tópico..." aria-label="Buscar">
  </div>
  <div class="no-results" id="noResults">Nenhum tópico encontrado</div>
__NAV__
</nav>

<main>
  <div class="content-wrap">
    <section class="hero">
      <h1>Bioestatística</h1>
      <p>Curso completo do Instituto de Biofísica Carlos Chagas Filho — UFRJ. Conceitos fundamentais, com abordagem intuitiva e exemplos práticos em Python.</p>
      <div class="authors">
        Pedro Torres &middot; Gilberto Weissmuller
      </div>
    </section>
__MAIN__
  </div>
</main>

<script src="https://cdn.jsdelivr.net/npm/marked@11.1.1/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/highlight.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/languages/python.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/languages/bash.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

<script>
// ---- Theme ----
const root = document.documentElement;
const stored = localStorage.getItem('theme');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const initial = stored || (prefersDark ? 'dark' : 'light');
applyTheme(initial);

function applyTheme(theme) {
  root.setAttribute('data-theme', theme);
  document.getElementById('hljs-light').disabled = theme === 'dark';
  document.getElementById('hljs-dark').disabled = theme === 'light';
  document.getElementById('iconSun').style.display = theme === 'dark' ? 'none' : '';
  document.getElementById('iconMoon').style.display = theme === 'dark' ? '' : 'none';
  if (window.mermaid) {
    mermaid.initialize({ startOnLoad: false, theme: theme === 'dark' ? 'dark' : 'default', securityLevel: 'loose' });
  }
}
document.getElementById('themeToggle').addEventListener('click', () => {
  const current = root.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  localStorage.setItem('theme', next);
  applyTheme(next);
});

// ---- Mermaid init ----
mermaid.initialize({ startOnLoad: false, theme: initial === 'dark' ? 'dark' : 'default', securityLevel: 'loose' });

// ---- Marked customization ----
marked.use({
  renderer: {
    code(code, lang) {
      if (lang === 'mermaid') {
        return `<div class="mermaid">${code}</div>`;
      }
      const valid = hljs.getLanguage(lang) ? lang : 'plaintext';
      const highlighted = hljs.highlight(code, { language: valid }).value;
      return `<pre><button class="code-copy">copiar</button><code class="hljs language-${valid}">${highlighted}</code></pre>`;
    }
  }
});

// ---- Render all markdown blocks ----
document.querySelectorAll('script[type="text/markdown"]').forEach(s => {
  const targetId = s.dataset.target;
  const target = document.getElementById(targetId);
  if (!target) return;
  let md = s.textContent;
  // Proteger blocos $$ ... $$ e $ ... $ contra interpretação do markdown
  const placeholders = [];
  md = md.replace(/\$\$([\s\S]+?)\$\$/g, (_, expr) => {
    placeholders.push('$$' + expr + '$$');
    return `@@MATHBLOCK${placeholders.length - 1}@@`;
  });
  md = md.replace(/\$([^\n$]+?)\$/g, (_, expr) => {
    placeholders.push('$' + expr + '$');
    return `@@MATHINLINE${placeholders.length - 1}@@`;
  });
  let html = marked.parse(md);
  html = html.replace(/@@MATH(BLOCK|INLINE)(\d+)@@/g, (_, _t, i) => placeholders[parseInt(i)]);
  target.innerHTML = html;
});

// ---- KaTeX render ----
renderMathInElement(document.body, {
  delimiters: [
    {left: "$$", right: "$$", display: true},
    {left: "$", right: "$", display: false}
  ],
  throwOnError: false
});

// ---- Mermaid render after content is in ----
mermaid.run({ querySelector: '.mermaid' });

// ---- Copy buttons ----
document.querySelectorAll('.code-copy').forEach(btn => {
  btn.addEventListener('click', () => {
    const code = btn.parentElement.querySelector('code').innerText;
    navigator.clipboard.writeText(code).then(() => {
      btn.textContent = 'copiado!';
      btn.classList.add('copied');
      setTimeout(() => { btn.textContent = 'copiar'; btn.classList.remove('copied'); }, 1500);
    });
  });
});

// ---- Sidebar active-item highlighting ----
const navLinks = document.querySelectorAll('.nav-section a');
const linkByTarget = {};
navLinks.forEach(a => { linkByTarget[a.dataset.target] = a; });

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(a => a.classList.remove('active'));
      const link = linkByTarget[entry.target.id];
      if (link) {
        link.classList.add('active');
        // garantir que está visível no sidebar
        const rect = link.getBoundingClientRect();
        if (rect.top < 80 || rect.bottom > window.innerHeight - 20) {
          link.scrollIntoView({ block: 'nearest' });
        }
      }
    }
  });
}, { rootMargin: '-30% 0px -60% 0px' });

document.querySelectorAll('article.topic').forEach(t => observer.observe(t));

// ---- Progress bar ----
const progressBar = document.getElementById('progressBar');
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  const scrolled = (h.scrollTop) / (h.scrollHeight - h.clientHeight) * 100;
  progressBar.style.width = scrolled + '%';
});

// ---- Search ----
const searchInput = document.getElementById('search');
const noResults = document.getElementById('noResults');
searchInput.addEventListener('input', () => {
  const q = searchInput.value.toLowerCase().trim();
  let anyVisible = false;
  document.querySelectorAll('.nav-section').forEach(sec => {
    let sectionHasMatch = false;
    sec.querySelectorAll('li').forEach(li => {
      const text = li.textContent.toLowerCase();
      const match = !q || text.includes(q);
      li.classList.toggle('hidden', !match);
      if (match) sectionHasMatch = true;
    });
    sec.classList.toggle('hidden', !sectionHasMatch);
    if (sectionHasMatch) anyVisible = true;
  });
  noResults.classList.toggle('show', !anyVisible);
});

// ---- Mobile menu ----
const sidebar = document.getElementById('sidebar');
document.getElementById('menuToggle').addEventListener('click', () => {
  sidebar.classList.toggle('open');
});
sidebar.addEventListener('click', e => {
  if (e.target.tagName === 'A') sidebar.classList.remove('open');
});

// ---- Smooth scroll on initial hash ----
if (window.location.hash) {
  setTimeout(() => {
    const el = document.getElementById(window.location.hash.slice(1));
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  }, 100);
}
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
