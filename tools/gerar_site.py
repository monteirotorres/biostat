"""Gera o site multi-página (4 capítulos + index) com abas.

Lê SUMMARY.md, converte cada markdown para HTML (preservando LaTeX
para renderização via KaTeX), injeta widgets interativos onde apropriado
e escreve os arquivos em site/.
"""

import re
from pathlib import Path
import markdown

BASE = Path(__file__).parent.parent
SITE = BASE
SUMMARY = BASE / "SUMMARY.md"

# ---- mapeamento de widgets por arquivo de markdown ----
WIDGETS = {
    "01_introducao/07_histogramas.md":           ("histograma",          "wHistograma"),
    "01_introducao/08_curva_normal.md":          ("curva_normal",        "wCurvaNormal"),
    "02_estatistica_descritiva/09_teorema_limite_central.md": ("tlc",   "wTLC"),
    "03_probabilidade/06_sensibilidade_especificidade.md":    ("sens",  "wSensEsp"),
    "03_probabilidade/08_valor_preditivo.md":    ("vpp",                 "wSensEsp"),
    "03_probabilidade/09_curva_roc.md":          ("roc",                 "wROC"),
    "03_probabilidade/10_distribuicao_binomial.md": ("binom",            "wBinomial"),
    "04_estatistica_inferencial/03_intervalo_confianca.md": ("ic",       "wIC"),
    "04_estatistica_inferencial/06_valor_p.md":  ("vp",                  "wValorP"),
    "04_estatistica_inferencial/07_erros_tipo_i_ii.md": ("err",          "wErros"),
    "04_estatistica_inferencial/14_correlacao.md": ("corr",              "wCorrelacao"),
}

# ---- HTML do widget e chamada JS ----
def widget_html(wid: str, fn: str) -> str:
    raw = _widget_body(wid, fn)
    return raw.replace(
        '<div class="widget">',
        f'<div class="widget" data-widget="{fn}" data-id="{wid}">',
        1,
    )


def _widget_body(wid: str, fn: str) -> str:
    if fn == "wCurvaNormal":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Curva Normal</div>
  <canvas id="{wid}"></canvas>
  <div class="legend">
    <span class="legend-item"><span class="swatch" style="background:#3266ad;opacity:0.3"></span>±1σ ≈ 68%</span>
    <span class="legend-item"><span class="swatch" style="background:#3266ad;opacity:0.18"></span>±2σ ≈ 95%</span>
    <span class="legend-item"><span class="swatch" style="background:#3266ad;opacity:0.10"></span>±3σ ≈ 99,7%</span>
  </div>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Média (μ)</span>
      <input type="range" min="-5" max="5" step="0.1" value="0" id="{wid}-mu">
      <span class="ctrl-val" id="{wid}-mu-v">0.0</span>
    </div>
    <div class="ctrl-row">
      <span class="ctrl-label">Desvio padrão (σ)</span>
      <input type="range" min="0.5" max="4" step="0.1" value="1" id="{wid}-sg">
      <span class="ctrl-val" id="{wid}-sg-v">1.0</span>
    </div>
  </div>
  <div class="stat-grid">
    <div class="stat-card"><div class="slabel">±1σ</div><div class="sval" id="{wid}-p1">—</div><div class="sdesc">cobertura</div></div>
    <div class="stat-card"><div class="slabel">±2σ</div><div class="sval" id="{wid}-p2">—</div><div class="sdesc">cobertura</div></div>
    <div class="stat-card"><div class="slabel">±3σ</div><div class="sval" id="{wid}-p3">—</div><div class="sdesc">cobertura</div></div>
  </div>
</div>
"""
    if fn == "wTLC":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Teorema do Limite Central</div>
  <div class="btn-row">
    <button class="btn outline active" data-tlc-dist="{wid}" data-dist="uniforme">Uniforme</button>
    <button class="btn outline" data-tlc-dist="{wid}" data-dist="exponencial">Exponencial</button>
    <button class="btn outline" data-tlc-dist="{wid}" data-dist="bimodal">Bimodal</button>
  </div>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Tamanho de cada amostra (n)</span>
      <input type="range" min="1" max="100" step="1" value="5" id="{wid}-n">
      <span class="ctrl-val" id="{wid}-n-v">5</span>
    </div>
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    <div class="stat-card"><div class="slabel">Média</div><div class="sval" id="{wid}-mean">—</div><div class="sdesc">das 2000 amostras</div></div>
    <div class="stat-card"><div class="slabel">Desvio padrão</div><div class="sval" id="{wid}-sd">—</div><div class="sdesc">erro padrão da média</div></div>
  </div>
</div>
"""
    if fn == "wBinomial":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Distribuição Binomial</div>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Número de tentativas (n)</span>
      <input type="range" min="2" max="60" step="1" value="20" id="{wid}-n">
      <span class="ctrl-val" id="{wid}-n-v">20</span>
    </div>
    <div class="ctrl-row">
      <span class="ctrl-label">Probabilidade de sucesso (p)</span>
      <input type="range" min="0.01" max="0.99" step="0.01" value="0.5" id="{wid}-p">
      <span class="ctrl-val" id="{wid}-p-v">0.50</span>
    </div>
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid">
    <div class="stat-card"><div class="slabel">E[X] = np</div><div class="sval" id="{wid}-mean">—</div><div class="sdesc">média esperada</div></div>
    <div class="stat-card"><div class="slabel">SD = √(np(1−p))</div><div class="sval" id="{wid}-sd">—</div><div class="sdesc">desvio padrão</div></div>
    <div class="stat-card"><div class="slabel">Moda</div><div class="sval" id="{wid}-modek">—</div><div class="sdesc">valor mais provável</div></div>
  </div>
</div>
"""
    if fn == "wSensEsp":
        return f"""
<div class="widget">
  <div class="widget-title">Calculadora — Sensibilidade, Especificidade, VPP e VPN</div>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Sensibilidade</span>
      <input type="range" min="0.5" max="1" step="0.01" value="0.95" id="{wid}-sens">
      <span class="ctrl-val" id="{wid}-sens-v">0.95</span>
    </div>
    <div class="ctrl-row">
      <span class="ctrl-label">Especificidade</span>
      <input type="range" min="0.5" max="1" step="0.01" value="0.95" id="{wid}-esp">
      <span class="ctrl-val" id="{wid}-esp-v">0.95</span>
    </div>
    <div class="ctrl-row">
      <span class="ctrl-label">Prevalência</span>
      <input type="range" min="0.001" max="0.5" step="0.001" value="0.01" id="{wid}-prev">
      <span class="ctrl-val" id="{wid}-prev-v">1.0%</span>
    </div>
  </div>
  <table style="font-family:'Courier New',monospace;font-size:0.85rem;text-align:center;">
    <thead><tr><th></th><th>Doente</th><th>Saudável</th></tr></thead>
    <tbody>
      <tr><th>Teste +</th><td id="{wid}-vp" style="color:#3266ad;font-weight:bold">—</td><td id="{wid}-fp" style="color:#c0392b;font-weight:bold">—</td></tr>
      <tr><th>Teste −</th><td id="{wid}-fn" style="color:#c0392b;font-weight:bold">—</td><td id="{wid}-vn" style="color:#3266ad;font-weight:bold">—</td></tr>
    </tbody>
  </table>
  <div class="stat-grid" style="margin-top:0.6rem;">
    <div class="stat-card"><div class="slabel">VPP</div><div class="sval" id="{wid}-vpp" style="color:#3266ad;">—</div><div class="sdesc">P(doente | teste +)</div></div>
    <div class="stat-card"><div class="slabel">VPN</div><div class="sval" id="{wid}-vpn" style="color:#3266ad;">—</div><div class="sdesc">P(saudável | teste −)</div></div>
  </div>
</div>
"""
    if fn == "wROC":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Curva ROC</div>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Separação entre doentes e saudáveis</span>
      <input type="range" min="0" max="5" step="0.1" value="2" id="{wid}-sep">
      <span class="ctrl-val" id="{wid}-sep-v">2.0</span>
    </div>
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    <div class="stat-card"><div class="slabel">AUC</div><div class="sval" id="{wid}-auc">—</div><div class="sdesc">área sob a curva</div></div>
    <div class="stat-card"><div class="slabel">Sensibilidade*</div><div class="sval" id="{wid}-sens">—</div><div class="sdesc">no corte ótimo</div></div>
    <div class="stat-card"><div class="slabel">Especificidade*</div><div class="sval" id="{wid}-esp">—</div><div class="sdesc">no corte ótimo</div></div>
  </div>
</div>
"""
    if fn == "wIC":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Intervalo de Confiança</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">
    Cada linha é o IC de uma amostra independente da mesma população (μ = 100, σ = 15).
    <span style="color:#3266ad">Azul</span> = contém μ; <span style="color:#c0392b">vermelho</span> = falha.
  </p>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Tamanho da amostra (n)</span>
      <input type="range" min="5" max="200" step="5" value="30" id="{wid}-n">
      <span class="ctrl-val" id="{wid}-n-v">30</span>
    </div>
    <div class="ctrl-row">
      <span class="ctrl-label">Nível de confiança</span>
      <input type="range" min="0.8" max="0.99" step="0.01" value="0.95" id="{wid}-conf">
      <span class="ctrl-val" id="{wid}-conf-v">95%</span>
    </div>
  </div>
  <div class="btn-row"><button class="btn" id="{wid}-redraw">Nova simulação ↺</button></div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    <div class="stat-card"><div class="slabel">Cobertura observada</div><div class="sval" id="{wid}-cov">—</div><div class="sdesc">em 60 amostras simuladas</div></div>
  </div>
</div>
"""
    if fn == "wValorP":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Valor-p</div>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Estatística z observada</span>
      <input type="range" min="-4" max="4" step="0.05" value="1.96" id="{wid}-z">
      <span class="ctrl-val" id="{wid}-z-v">1.96</span>
    </div>
    <div class="ctrl-row">
      <label style="font-size:0.78rem;font-family:'Courier New',monospace;color:#666;">
        <input type="checkbox" id="{wid}-bil" checked> teste bilateral
      </label>
    </div>
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    <div class="stat-card"><div class="slabel">valor-p</div><div class="sval" id="{wid}-p" style="color:#c0392b;">—</div><div class="sdesc">área sombreada</div></div>
  </div>
</div>
"""
    if fn == "wErros":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Erros Tipo I e Tipo II</div>
  <div class="legend">
    <span class="legend-item"><span class="swatch" style="background:#3266ad"></span>H₀ verdadeira</span>
    <span class="legend-item"><span class="swatch" style="background:#c0392b"></span>H₁ verdadeira</span>
    <span class="legend-item"><span class="swatch" style="background:rgba(192,57,43,0.5)"></span>α — falso positivo</span>
    <span class="legend-item"><span class="swatch" style="background:rgba(41,128,185,0.5)"></span>β — falso negativo</span>
  </div>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Nível de significância (α)</span>
      <input type="range" min="0.01" max="0.20" step="0.01" value="0.05" id="{wid}-alpha">
      <span class="ctrl-val" id="{wid}-alpha-v">0.05</span>
    </div>
    <div class="ctrl-row">
      <span class="ctrl-label">Tamanho de efeito (δ/σ)</span>
      <input type="range" min="0.5" max="3" step="0.1" value="1.5" id="{wid}-delta">
      <span class="ctrl-val" id="{wid}-delta-v">1.5</span>
    </div>
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    <div class="stat-card"><div class="slabel">α</div><div class="sval" id="{wid}-vAlpha" style="color:#c0392b;">—</div><div class="sdesc">erro tipo I</div></div>
    <div class="stat-card"><div class="slabel">β</div><div class="sval" id="{wid}-vBeta" style="color:#2980b9;">—</div><div class="sdesc">erro tipo II</div></div>
    <div class="stat-card"><div class="slabel">Poder</div><div class="sval" id="{wid}-vPower" style="color:#1a7a4a;">—</div><div class="sdesc">1 − β</div></div>
    <div class="stat-card"><div class="slabel">z*</div><div class="sval" id="{wid}-vZ">—</div><div class="sdesc">corte de rejeição</div></div>
  </div>
</div>
"""
    if fn == "wCorrelacao":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Correlação</div>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Coeficiente r (Pearson)</span>
      <input type="range" min="-1" max="1" step="0.05" value="0.6" id="{wid}-r">
      <span class="ctrl-val" id="{wid}-r-v">0.60</span>
    </div>
  </div>
  <div class="btn-row"><button class="btn" id="{wid}-redraw">Nova amostra ↺</button></div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    <div class="stat-card"><div class="slabel">R²</div><div class="sval" id="{wid}-r2">—</div><div class="sdesc">variância explicada</div></div>
  </div>
</div>
"""
    if fn == "wHistograma":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Histograma e amostragem</div>
  <div class="btn-row">
    <button class="btn outline active" data-hist-dist="{wid}" data-dist="uniforme">Uniforme</button>
    <button class="btn outline" data-hist-dist="{wid}" data-dist="normal">Normal</button>
    <button class="btn" id="{wid}-redraw">Nova amostra ↺</button>
  </div>
  <div class="controls">
    <div class="ctrl-row">
      <span class="ctrl-label">Tamanho da amostra (N)</span>
      <input type="range" min="1" max="8" step="1" value="3" id="{wid}-n">
      <span class="ctrl-val" id="{wid}-n-v">100</span>
    </div>
    <div class="ctrl-row">
      <span class="ctrl-label">Número de bins</span>
      <input type="range" min="3" max="60" step="1" value="15" id="{wid}-bins">
      <span class="ctrl-val" id="{wid}-bins-v">15</span>
    </div>
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    <div class="stat-card"><div class="slabel">Média</div><div class="sval" id="{wid}-mean">—</div><div class="sdesc">média amostral</div></div>
    <div class="stat-card"><div class="slabel">Desvio padrão</div><div class="sval" id="{wid}-sd">—</div><div class="sdesc">desvio padrão amostral</div></div>
  </div>
</div>
"""
    return ""


# ----------- markdown → HTML preservando LaTeX -----------
def md_to_html(text: str) -> str:
    math_blocks, math_inline = [], []

    def save_block(m):
        math_blocks.append(m.group(0))
        return f"@@MATHB{len(math_blocks)-1}@@"

    def save_inline(m):
        math_inline.append(m.group(0))
        return f"@@MATHI{len(math_inline)-1}@@"

    text = re.sub(r"\$\$([\s\S]+?)\$\$", save_block, text)
    text = re.sub(r"(?<!\\)\$([^\n$]+?)(?<!\\)\$", save_inline, text)

    html = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists"],
    )

    # Mermaid → div + script no client
    def replace_mermaid(m):
        body = m.group(1)
        return f'<div class="mermaid-container"><pre class="mermaid">{body}</pre></div>'

    html = re.sub(
        r'<pre><code class="language-mermaid">([\s\S]+?)</code></pre>',
        replace_mermaid,
        html,
    )

    for i, b in enumerate(math_blocks):
        html = html.replace(f"@@MATHB{i}@@", b)
    for i, b in enumerate(math_inline):
        html = html.replace(f"@@MATHI{i}@@", b)

    # Tira display math de dentro de <p> (HTML inválido + render quebrado)
    html = re.sub(
        r"<p>\s*(\$\$[\s\S]+?\$\$)\s*</p>",
        r'<div class="math-display">\1</div>',
        html,
    )

    return html


# ----------- parser do SUMMARY.md -----------
def parse_summary():
    section, sections, items = None, [], []
    for line in SUMMARY.read_text(encoding="utf-8").splitlines():
        m_h2 = re.match(r"^##\s+(.+)$", line)
        m_item = re.match(r"^\*\s+\[(.+?)\]\((.+?)\)$", line)
        if m_h2:
            if section is not None:
                sections.append((section, items))
            section = m_h2.group(1).strip()
            items = []
        elif m_item:
            title = m_item.group(1).strip()
            path = m_item.group(2).strip()
            if path.startswith("0"):
                items.append((title, path))
    if section is not None:
        sections.append((section, items))
    return sections


# ----------- templates HTML -----------
SHELL_HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Bioestatística</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {{ delimiters: [{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}], throwOnError:false }});"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body>
<div class="container">
"""

SHELL_FOOT = """
<div class="footer">Produzido para fins didáticos — bioestatística — UFRJ / IBCCF</div>
</div>
<script src="assets/widgets.js"></script>
<script>mermaid.initialize({ startOnLoad: true, theme: 'neutral', securityLevel: 'loose' });</script>
</body>
</html>
"""


def make_topnav(current: str, parts: list) -> str:
    items = ['<a href="index.html"' + (' class="current"' if current == "index" else "") + ">Início</a>"]
    for i, (sec, _) in enumerate(parts, 1):
        url = f"parte{i}.html"
        cls = ' class="current"' if current == f"parte{i}" else ""
        items.append(f'<a href="{url}"{cls}>Parte {i}</a>')
    return (
        '<div class="topnav">'
        '<span class="brand"><strong>Bioestatística</strong> · IBCCF / UFRJ</span>'
        + "".join(items)
        + "</div>"
    )


def slugify(path: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")


def write_index(parts: list):
    out = []
    out.append(SHELL_HEAD.format(title="Bioestatística"))
    out.append(make_topnav("index", parts))
    out.append(
        '<header class="page-head">'
        '<h1>Bioestatística</h1>'
        '<div class="subtitle">Curso · IBCCF · Universidade Federal do Rio de Janeiro</div>'
        "</header>"
    )
    out.append(
        '<p style="margin-bottom:1.2rem;">'
        "Material didático com abordagem intuitiva. Cada tópico tem um capítulo "
        "explicativo e um notebook em Python (pandas, seaborn e scipy.stats) "
        "para experimentar os conceitos."
        "</p>"
        '<p style="margin-bottom:1.2rem;color:#555;font-size:0.92rem;">'
        "Em vários capítulos você encontrará <strong>demonstrações interativas</strong> — "
        "manipule os parâmetros e veja, em tempo real, como os conceitos se comportam."
        "</p>"
        '<p style="margin-bottom:1.5rem;font-family:\'Courier New\',monospace;font-size:0.78rem;color:#888;">'
        "Pedro Torres &nbsp;·&nbsp; Gilberto Weissmuller"
        "</p>"
    )
    out.append('<div class="cards">')
    descriptions = [
        "Amostra, população, variáveis, histogramas e curva normal.",
        "Tendência central, dispersão e o teorema do limite central.",
        "Eventos, testes diagnósticos, ROC e distribuição binomial.",
        "Intervalos de confiança, testes t, ANOVA, qui-quadrado, regressão.",
    ]
    for i, ((sec, items), desc) in enumerate(zip(parts, descriptions), 1):
        out.append(
            f'<a class="card" href="parte{i}.html">'
            f'<div class="cnum">Parte {i}</div>'
            f'<div class="ctitle">{sec}</div>'
            f'<div class="cdesc">{desc}</div>'
            f'<div class="ccount">{len(items)} tópicos</div>'
            "</a>"
        )
    out.append("</div>")
    out.append(SHELL_FOOT)
    (SITE / "index.html").write_text("".join(out), encoding="utf-8")


def write_part(idx: int, parts: list):
    sec, items = parts[idx - 1]
    out = []
    out.append(SHELL_HEAD.format(title=sec))
    out.append(make_topnav(f"parte{idx}", parts))
    out.append(
        f'<header class="page-head">'
        f'<h1>Parte {idx} — {sec}</h1>'
        f'<div class="subtitle">{len(items)} tópicos · navegue pelas abas abaixo</div>'
        "</header>"
    )

    # tabs
    out.append('<div class="tabs">')
    for i, (title, path) in enumerate(items, 1):
        slug = slugify(path)
        cls = "tab active" if i == 1 else "tab"
        out.append(f'<button class="{cls}" data-target="{slug}"><span class="num">{i:02d}</span>{title}</button>')
    out.append("</div>")

    # painéis
    for i, (title, path) in enumerate(items, 1):
        slug = slugify(path)
        cls = "topic active" if i == 1 else "topic"
        md_path = BASE / path
        md_text = md_path.read_text(encoding="utf-8")
        # tira o H1 (vamos botar o nosso próprio)
        md_text = re.sub(r"^#\s+.+\n+", "", md_text, count=1)
        body_html = md_to_html(md_text)
        ipynb = path.replace(".md", ".ipynb")
        nb_link = f'<a class="nb-link" href="{ipynb}" target="_blank">⓪ Abrir notebook</a>'

        widget = ""
        if path in WIDGETS:
            wid, fn = WIDGETS[path]
            widget = widget_html(wid + f"_{idx}_{i}", fn)

        out.append(f'<section id="{slug}" class="{cls}">')
        out.append(f"<h1>{title}</h1>")
        out.append(body_html)
        out.append(widget)
        out.append(nb_link)
        out.append("</section>")

    out.append(SHELL_FOOT)
    (SITE / f"parte{idx}.html").write_text("".join(out), encoding="utf-8")


def main():
    SITE.mkdir(exist_ok=True)
    (SITE / "assets").mkdir(exist_ok=True)
    parts = parse_summary()
    write_index(parts)
    for i in range(1, len(parts) + 1):
        write_part(i, parts)
        print(f"  parte{i}.html escrito  ({(SITE / f'parte{i}.html').stat().st_size / 1024:.1f} KB)")
    print(f"  index.html escrito   ({(SITE / 'index.html').stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
