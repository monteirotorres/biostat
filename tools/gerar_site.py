"""Gera o site (gitbook-style): sidebar à esquerda + uma página por seção.

- Lê SUMMARY.md (nomes de seção limpos).
- Converte markdown → HTML preservando LaTeX (KaTeX no cliente).
- Sidebar lista todas as seções/tópicos; links cross-page navegam, same-page alternam.
- Notebooks viram badges "Open in Colab".
- Injeta widgets interativos.
"""

import re
from pathlib import Path
import markdown

BASE = Path(__file__).parent.parent
SUMMARY = BASE / "SUMMARY.md"

GITHUB_REPO = "monteirotorres/biostat"
GITHUB_BRANCH = "main"

# arquivo .md  ->  (id base, função JS do widget)
WIDGETS = {
    "01_introducao/03_precisao_acuracia.md": ("precisao", "wPrecisao"),
    "01_introducao/07_histogramas.md": ("histograma", "wHistograma"),
    "01_introducao/08_curva_normal.md": ("curva_normal", "wCurvaNormal"),
    "02_estatistica_descritiva/01_tendencia_central.md": ("tendencia", "wTendencia"),
    "02_estatistica_descritiva/09_teorema_limite_central.md": ("tlc", "wTLC"),
    "02_estatistica_descritiva/10_amplitude.md": ("boxplot", "wBoxplot"),
    "03_probabilidade/06_sensibilidade_especificidade.md": ("sens", "wSensEsp"),
    "03_probabilidade/08_valor_preditivo.md": ("vpp", "wSensEsp"),
    "03_probabilidade/09_curva_roc.md": ("roc", "wROC"),
    "03_probabilidade/10_distribuicao_binomial.md": ("binom", "wBinomial"),
    "05_distribuicoes_amostrais/01_de_onde_vem.md": ("dist", "wDistAmostral"),
    "04_estatistica_inferencial/03_intervalo_confianca.md": ("ic", "wIC"),
    "04_estatistica_inferencial/04_hipoteses.md": ("hip", "wHipoteses"),
    "04_estatistica_inferencial/06_valor_p.md": ("vp", "wValorP"),
    "04_estatistica_inferencial/07_erros_tipo_i_ii.md": ("err", "wErros"),
    "04_estatistica_inferencial/12_anova.md": ("anova", "wANOVA"),
    "04_estatistica_inferencial/14_correlacao.md": ("corr", "wCorrelacao"),
    "04_estatistica_inferencial/17_design_experimental.md": ("pot", "wPotenciaCalc"),
}

# nome de arquivo da página por seção
SECTION_FILES = {
    "Introdução": "introducao.html",
    "Estatística Descritiva": "descritiva.html",
    "Probabilidade": "probabilidade.html",
    "Distribuições amostrais": "distribuicoes.html",
    "Estatística Inferencial": "inferencial.html",
    "Tabelas estatísticas": "tabelas.html",
    "Exercícios": "exercicios.html",
}


# ---------------- widget HTML ----------------
def widget_html(wid, fn):
    raw = _widget_body(wid, fn)
    return raw.replace('<div class="widget">',
                       f'<div class="widget" data-widget="{fn}" data-id="{wid}">', 1)


def _slider(wid, key, label, mn, mx, step, val):
    return (f'<div class="ctrl-row"><span class="ctrl-label">{label}</span>'
            f'<input type="range" min="{mn}" max="{mx}" step="{step}" value="{val}" id="{wid}-{key}">'
            f'<span class="ctrl-val" id="{wid}-{key}-v">{val}</span></div>')


def _card(wid, key, label, desc, color=""):
    style = f' style="color:{color};"' if color else ""
    return (f'<div class="stat-card"><div class="slabel">{label}</div>'
            f'<div class="sval" id="{wid}-{key}"{style}>—</div>'
            f'<div class="sdesc">{desc}</div></div>')


def _widget_body(wid, fn):
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
    {_slider(wid,'mu','Média (μ)',-5,5,0.1,0)}
    {_slider(wid,'sg','Desvio padrão (σ)',0.5,4,0.1,1)}
  </div>
  <div class="stat-grid">
    {_card(wid,'p1','±1σ','cobertura')}{_card(wid,'p2','±2σ','cobertura')}{_card(wid,'p3','±3σ','cobertura')}
  </div>
</div>"""
    if fn == "wTLC":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Teorema do Limite Central</div>
  <div class="btn-row">
    <button class="btn outline active" data-tlc-dist="{wid}" data-dist="uniforme">Uniforme</button>
    <button class="btn outline" data-tlc-dist="{wid}" data-dist="exponencial">Exponencial</button>
    <button class="btn outline" data-tlc-dist="{wid}" data-dist="bimodal">Bimodal</button>
    <button class="btn" id="{wid}-redraw">Nova simulação ↺</button>
  </div>
  <div class="controls">{_slider(wid,'n','Tamanho de cada amostra (n)',1,100,1,5)}</div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'mean','Média','das 2000 amostras')}{_card(wid,'sd','Desvio padrão','erro padrão da média')}
  </div>
</div>"""
    if fn == "wBinomial":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Distribuição Binomial</div>
  <div class="controls">
    {_slider(wid,'n','Número de tentativas (n)',2,60,1,20)}
    {_slider(wid,'p','Probabilidade de sucesso (p)',0.01,0.99,0.01,0.5)}
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid">
    {_card(wid,'mean','E[X] = np','média esperada')}{_card(wid,'sd','SD','√(np(1−p))')}{_card(wid,'modek','Moda','valor mais provável')}
  </div>
</div>"""
    if fn == "wSensEsp":
        return f"""
<div class="widget">
  <div class="widget-title">Calculadora — Sensibilidade, Especificidade, VPP e VPN</div>
  <div class="controls">
    {_slider(wid,'sens','Sensibilidade',0.5,1,0.01,0.95)}
    {_slider(wid,'esp','Especificidade',0.5,1,0.01,0.95)}
    {_slider(wid,'prev','Prevalência',0.001,0.5,0.001,0.01)}
  </div>
  <table style="font-family:'Courier New',monospace;font-size:0.85rem;text-align:center;">
    <thead><tr><th></th><th>Doente</th><th>Saudável</th></tr></thead>
    <tbody>
      <tr><th>Teste +</th><td id="{wid}-vp" style="color:#3266ad;font-weight:bold">—</td><td id="{wid}-fp" style="color:#c0392b;font-weight:bold">—</td></tr>
      <tr><th>Teste −</th><td id="{wid}-fn" style="color:#c0392b;font-weight:bold">—</td><td id="{wid}-vn" style="color:#3266ad;font-weight:bold">—</td></tr>
    </tbody>
  </table>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'vpp','VPP','P(doente | teste +)','#3266ad')}{_card(wid,'vpn','VPN','P(saudável | teste −)','#3266ad')}
  </div>
</div>"""
    if fn == "wROC":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Curva ROC + Matriz de Confusão</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">Ajuste a separação entre doentes e saudáveis, a prevalência e o ponto de corte. A matriz de confusão e as métricas se atualizam.</p>
  <div class="controls">
    {_slider(wid,'sep','Separação (efeito do teste)',0,5,0.1,2)}
    {_slider(wid,'prev','Prevalência',0.05,0.9,0.05,0.3)}
    {_slider(wid,'thr','Ponto de corte',-3,6,0.1,1)}
  </div>
  <canvas id="{wid}"></canvas>
  <table style="font-family:'Courier New',monospace;font-size:0.85rem;text-align:center;margin-top:0.6rem;">
    <thead><tr><th></th><th>Doente</th><th>Saudável</th></tr></thead>
    <tbody>
      <tr><th>Teste +</th><td id="{wid}-tp" style="color:#3266ad;font-weight:bold">—</td><td id="{wid}-fp" style="color:#c0392b;font-weight:bold">—</td></tr>
      <tr><th>Teste −</th><td id="{wid}-fn" style="color:#c0392b;font-weight:bold">—</td><td id="{wid}-tn" style="color:#3266ad;font-weight:bold">—</td></tr>
    </tbody>
  </table>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'sens','Sensibilidade','VP/(VP+FN)')}{_card(wid,'spec','Especificidade','VN/(VN+FP)')}
    {_card(wid,'ppv','VPP','VP/(VP+FP)')}{_card(wid,'npv','VPN','VN/(VN+FN)')}
  </div>
  <div class="stat-grid" style="margin-top:0.4rem;">
    {_card(wid,'acc','Acurácia','(VP+VN)/N')}{_card(wid,'auc','AUC','área sob a curva')}
  </div>
</div>"""
    if fn == "wIC":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Intervalo de Confiança</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">Cada linha é o IC de uma amostra da mesma população (μ = 100, σ = 15). <span style="color:#3266ad">Azul</span> contém μ; <span style="color:#c0392b">vermelho</span> falha. O eixo é fixo.</p>
  <div class="controls">
    {_slider(wid,'n','Tamanho da amostra (n)',5,200,5,30)}
    {_slider(wid,'conf','Nível de confiança',0.8,0.99,0.01,0.95)}
  </div>
  <div class="btn-row"><button class="btn" id="{wid}-redraw">Nova simulação ↺</button></div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">{_card(wid,'cov','Cobertura observada','em 60 amostras')}</div>
</div>"""
    if fn == "wValorP":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Valor-p</div>
  <div class="controls">
    {_slider(wid,'z','Estatística z observada',-4,4,0.05,1.96)}
    <div class="ctrl-row"><label style="font-size:0.78rem;font-family:'Courier New',monospace;color:#666;"><input type="checkbox" id="{wid}-bil" checked> teste bilateral</label></div>
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">{_card(wid,'p','valor-p','área sombreada','#c0392b')}</div>
</div>"""
    if fn == "wErros":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Erros Tipo I e Tipo II</div>
  <div class="legend">
    <span class="legend-item"><span class="swatch" style="background:#3266ad"></span>H₀</span>
    <span class="legend-item"><span class="swatch" style="background:#c0392b"></span>H₁</span>
    <span class="legend-item"><span class="swatch" style="background:rgba(192,57,43,0.5)"></span>α</span>
    <span class="legend-item"><span class="swatch" style="background:rgba(41,128,185,0.5)"></span>β</span>
  </div>
  <div class="controls">
    {_slider(wid,'alpha','Nível de significância (α)',0.01,0.20,0.01,0.05)}
    {_slider(wid,'delta','Tamanho de efeito (δ/σ)',0.5,3,0.1,1.5)}
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'vAlpha','α','erro tipo I','#c0392b')}{_card(wid,'vBeta','β','erro tipo II','#2980b9')}
    {_card(wid,'vPower','Poder','1 − β','#1a7a4a')}{_card(wid,'vZ','z*','corte de rejeição')}
  </div>
</div>"""
    if fn == "wCorrelacao":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Correlação e resíduos</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">As linhas vermelhas verticais são os <strong>resíduos</strong> (distância de cada ponto à reta). Mover o slider de r não sorteia novos pontos.</p>
  <div class="controls">{_slider(wid,'r','Coeficiente r (Pearson)',-1,1,0.05,0.6)}</div>
  <div class="btn-row"><button class="btn" id="{wid}-redraw">Nova amostra ↺</button></div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">{_card(wid,'r2','R²','variância explicada')}</div>
</div>"""
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
    {_slider(wid,'n','Tamanho da amostra (N)',1,8,1,3)}
    {_slider(wid,'bins','Número de bins',3,60,1,15)}
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'mean','Média','média amostral')}{_card(wid,'sd','Desvio padrão','desvio padrão amostral')}
  </div>
</div>"""
    if fn == "wPrecisao":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Precisão e Acurácia</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">O centro do alvo é o valor verdadeiro. <strong>Viés</strong> afasta os tiros do centro (perde acurácia); <strong>ruído</strong> os espalha (perde precisão).</p>
  <div class="controls">
    {_slider(wid,'bias','Viés (afeta acurácia)',0,3,0.1,0.3)}
    {_slider(wid,'noise','Ruído (afeta precisão)',0.2,3,0.1,0.5)}
  </div>
  <div class="btn-row"><button class="btn" id="{wid}-redraw">Nova amostra ↺</button></div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'acc','Acurácia','proximidade do centro')}{_card(wid,'prec','Precisão','agrupamento dos tiros')}
  </div>
</div>"""
    if fn == "wTendencia":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Média × Mediana × Moda</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">Há um conjunto fixo de dados. Arraste o slider para mover um <strong>valor extremo</strong> e veja como cada medida reage.</p>
  <div class="controls">{_slider(wid,'out','Valor do ponto extremo',5,25,1,7)}</div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'mean','Média','sensível a extremos','#c0392b')}{_card(wid,'median','Mediana','robusta','#1a7a4a')}{_card(wid,'mode','Moda','mais frequente')}
  </div>
</div>"""
    if fn == "wBoxplot":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Boxplot e quartis</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">Histograma (em cima) e boxplot (embaixo) dos mesmos dados. Aumente a assimetria para ver outliers surgirem nos bigodes.</p>
  <div class="controls">{_slider(wid,'skew','Assimetria',0,3,0.1,0)}</div>
  <div class="btn-row"><button class="btn" id="{wid}-redraw">Nova amostra ↺</button></div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'q1','Q1','percentil 25')}{_card(wid,'med','Mediana','percentil 50')}{_card(wid,'q3','Q3','percentil 75')}{_card(wid,'iqr','IQR','Q3 − Q1')}
  </div>
</div>"""
    if fn == "wHipoteses":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Teste de hipóteses</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">A curva é a distribuição da estatística <strong>sob H₀</strong>. As áreas vermelhas são as regiões de rejeição (α). Mova a estatística observada e veja a decisão.</p>
  <div class="controls">
    {_slider(wid,'obs','Estatística observada',-4,4,0.05,2.2)}
    {_slider(wid,'alpha','Nível de significância (α)',0.01,0.20,0.01,0.05)}
    <div class="ctrl-row"><label style="font-size:0.78rem;font-family:'Courier New',monospace;color:#666;"><input type="checkbox" id="{wid}-bil" checked> teste bilateral</label></div>
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'p','valor-p','área além do observado','#c0392b')}{_card(wid,'dec','Decisão','com base em α')}
  </div>
</div>"""
    if fn == "wANOVA":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — ANOVA (3 grupos)</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">F compara a variância <strong>entre</strong> grupos com a variância <strong>dentro</strong>. Afaste as médias ou reduza a dispersão e veja o F crescer.</p>
  <div class="controls">
    {_slider(wid,'sep','Separação entre grupos',0,5,0.1,1)}
    {_slider(wid,'spread','Dispersão dentro dos grupos',0.5,4,0.1,2)}
  </div>
  <div class="btn-row"><button class="btn" id="{wid}-redraw">Nova amostra ↺</button></div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'F','F','entre / dentro')}{_card(wid,'p','valor-p','distribuição F')}{_card(wid,'sig','Resultado','α = 0,05')}
  </div>
</div>"""
    if fn == "wPotenciaCalc":
        return f"""
<div class="widget">
  <div class="widget-title">Calculadora interativa — Potência de testes</div>
  <p style="font-size:0.85rem;color:#666;margin-bottom:0.6rem;">Escolha o teste e ajuste o tamanho de efeito, o tamanho da amostra e o α. A curva mostra o poder em função de n; o ponto vermelho é a configuração atual.</p>
  <div class="btn-row">
    <button class="btn outline active" data-pot="{wid}" data-teste="t">Teste t (2 grupos)</button>
    <button class="btn outline" data-pot="{wid}" data-teste="anova">ANOVA</button>
    <button class="btn outline" data-pot="{wid}" data-teste="chi2">Qui-quadrado</button>
    <button class="btn outline" data-pot="{wid}" data-teste="prop">Proporções</button>
  </div>
  <div class="controls">
    <div class="ctrl-row"><span class="ctrl-label" id="{wid}-ef-lbl">tamanho de efeito</span>
      <input type="range" min="0.05" max="1.5" step="0.05" value="0.5" id="{wid}-ef"><span class="ctrl-val" id="{wid}-ef-v">0.50</span></div>
    <div class="ctrl-row"><span class="ctrl-label" id="{wid}-n-lbl">n por grupo</span>
      <input type="range" min="2" max="200" step="1" value="30" id="{wid}-n"><span class="ctrl-val" id="{wid}-n-v">30</span></div>
    <div class="ctrl-row"><span class="ctrl-label">Nível de significância (α)</span>
      <input type="range" min="0.01" max="0.20" step="0.01" value="0.05" id="{wid}-alpha"><span class="ctrl-val" id="{wid}-alpha-v">0.05</span></div>
    <div class="ctrl-row" id="{wid}-k-row"><span class="ctrl-label">Número de grupos (k)</span>
      <input type="range" min="3" max="8" step="1" value="3" id="{wid}-k"><span class="ctrl-val" id="{wid}-k-v">3</span></div>
    <div class="ctrl-row" id="{wid}-df-row"><span class="ctrl-label">Graus de liberdade</span>
      <input type="range" min="1" max="10" step="1" value="1" id="{wid}-df"><span class="ctrl-val" id="{wid}-df-v">1</span></div>
  </div>
  <canvas id="{wid}"></canvas>
  <div class="stat-grid" style="margin-top:0.6rem;">
    {_card(wid,'pw','Poder (1 − β)','na configuração atual','#1a7a4a')}
    {_card(wid,'n80','n para 80%','tamanho de amostra necessário')}
  </div>
  <p style="font-size:0.78rem;color:#888;margin-top:0.4rem;">Efeitos (Cohen): pequeno/médio/grande ≈ d 0,2/0,5/0,8 · f 0,1/0,25/0,4 · w 0,1/0,3/0,5. Valores aproximados (ANOVA via χ² não-central).</p>
</div>"""
    if fn == "wDistAmostral":
        return f"""
<div class="widget">
  <div class="widget-title">Demonstração interativa — Distribuições t, χ² e F</div>
  <div class="btn-row">
    <button class="btn outline active" data-dist="{wid}" data-tipo="t">t de Student</button>
    <button class="btn outline" data-dist="{wid}" data-tipo="chi2">χ² (qui-quadrado)</button>
    <button class="btn outline" data-dist="{wid}" data-tipo="f">F</button>
  </div>
  <div class="controls">
    {_slider(wid,'df','Graus de liberdade',1,40,1,5)}
    <div id="{wid}-df2row">{_slider(wid,'df2','Graus de liberdade (denominador)',1,40,1,10)}</div>
  </div>
  <canvas id="{wid}"></canvas>
  <p style="font-size:0.8rem;color:#888;margin-top:0.4rem;">Na t, a curva verde tracejada é a normal padrão — repare como a t se aproxima dela com mais graus de liberdade.</p>
</div>"""
    return ""


# ---------------- markdown → HTML ----------------
def md_to_html(text):
    blocks, inline = [], []
    text = re.sub(r"\$\$([\s\S]+?)\$\$", lambda m: blocks.append(m.group(0)) or f"@@MB{len(blocks)-1}@@", text)
    text = re.sub(r"(?<!\\)\$([^\n$]+?)(?<!\\)\$", lambda m: inline.append(m.group(0)) or f"@@MI{len(inline)-1}@@", text)
    html = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])
    html = re.sub(r'<pre><code class="language-mermaid">([\s\S]+?)</code></pre>',
                  lambda m: f'<div class="mermaid-container"><pre class="mermaid">{m.group(1)}</pre></div>', html)
    for i, b in enumerate(blocks):
        html = html.replace(f"@@MB{i}@@", b)
    for i, b in enumerate(inline):
        html = html.replace(f"@@MI{i}@@", b)
    html = re.sub(r"<p>\s*(\$\$[\s\S]+?\$\$)\s*</p>", r'<div class="math-display">\1</div>', html)
    return html


# ---------------- SUMMARY ----------------
def parse_summary():
    section, sections, items = None, [], []
    for line in SUMMARY.read_text(encoding="utf-8").splitlines():
        h2 = re.match(r"^##\s+(.+)$", line)
        it = re.match(r"^\*\s+\[(.+?)\]\((.+?)\)$", line)
        if h2:
            if section is not None:
                sections.append((section, items))
            section, items = h2.group(1).strip(), []
        elif it and it.group(2).startswith("0"):
            items.append((it.group(1).strip(), it.group(2).strip()))
    if section is not None:
        sections.append((section, items))
    return sections


def slugify(path):
    return re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")


# ---------------- HTML shell ----------------
def head(title):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Bioestatística IBCCF</title>
<script>(function(){{try{{var t=localStorage.getItem('tema');if(!t){{t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}}if(t==='dark')document.documentElement.setAttribute('data-theme','dark');}}catch(e){{}}}})();</script>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:false}});"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body>
<button class="menu-toggle" id="menuToggle" aria-label="Menu">☰</button>
<button class="theme-toggle" id="themeToggle" aria-label="Alternar tema" title="Alternar tema claro/escuro"><span class="theme-icon"></span></button>
"""


FOOT = """
<script src="assets/widgets.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:document.documentElement.dataset.theme==='dark'?'dark':'neutral',securityLevel:'loose'});</script>
</body>
</html>
"""


def sidebar(sections, current_file):
    out = ['<nav class="sidebar" id="sidebar">']
    out.append('<a class="sidebar-brand" href="index.html">Bioestatística<span>IBCCF · UFRJ</span></a>')
    for si, (sec, items) in enumerate(sections, 1):
        page = SECTION_FILES.get(sec, "index.html")
        out.append('<div class="nav-group">')
        out.append(f'<div class="nav-group-title">{si}. {sec}</div>')
        out.append('<ul>')
        for ti, (title, path) in enumerate(items, 1):
            slug = slugify(path)
            if page == current_file:
                out.append(f'<li><a class="nav-link" data-target="{slug}" href="#{slug}"><span class="n">{si}.{ti}</span>{title}</a></li>')
            else:
                out.append(f'<li><a href="{page}#{slug}"><span class="n">{si}.{ti}</span>{title}</a></li>')
        out.append('</ul></div>')
    out.append('</nav>')
    return "\n".join(out)


def footer():
    return ('<div class="footer">'
            '<img src="assets/ibccf-logo.png" alt="IBCCF" class="footer-logo">'
            '<div class="footer-text">Instituto de Biofísica Carlos Chagas Filho — UFRJ<br>'
            'Material didático de Bioestatística · Pedro Torres &amp; Gilberto Weissmuller</div>'
            '</div>')


def colab_link(ipynb):
    url = f"https://colab.research.google.com/github/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{ipynb}"
    return (f'<a class="colab-link" href="{url}" target="_blank" rel="noopener">'
            f'<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir no Colab">'
            f'</a>')


def write_section_page(idx, sections):
    sec, items = sections[idx]
    page = SECTION_FILES[sec]
    out = [head(sec)]
    out.append(sidebar(sections, page))
    out.append('<main class="content"><div class="content-inner">')
    out.append(f'<div class="page-eyebrow">{idx+1}. {sec}</div>')
    for ti, (title, path) in enumerate(items, 1):
        slug = slugify(path)
        md_text = (BASE / path).read_text(encoding="utf-8")
        md_text = re.sub(r"^#\s+.+\n+", "", md_text, count=1)
        body = md_to_html(md_text)
        ipynb = path.replace(".md", ".ipynb")
        has_nb = (BASE / ipynb).exists()
        nb = colab_link(ipynb) if has_nb else ""
        widget = ""
        if path in WIDGETS:
            base_id, fn = WIDGETS[path]
            widget = widget_html(f"{base_id}_{idx+1}_{ti}", fn)
        out.append(f'<article id="{slug}" class="topic">')
        out.append(f'<div class="topic-num">{idx+1}.{ti}</div>')
        out.append(f'<h1 class="topic-title">{title}</h1>')
        if nb:
            out.append(f'<div class="nb-row">{nb}</div>')
        out.append(body)
        out.append(widget)
        out.append('</article>')
    out.append('</div>')
    out.append(footer())
    out.append('</main>')
    out.append(FOOT)
    (BASE / page).write_text("\n".join(out), encoding="utf-8")
    return page


def write_index(sections):
    out = [head("Início")]
    out.append(sidebar(sections, "index.html"))
    out.append('<main class="content"><div class="content-inner">')
    out.append('<div class="hero">')
    out.append('<h1 class="hero-title">Bioestatística</h1>')
    out.append('<p class="hero-sub">Instituto de Biofísica Carlos Chagas Filho · UFRJ</p>')
    out.append('<p class="hero-desc">Curso com abordagem intuitiva, demonstrações interativas e notebooks em Python (pandas, seaborn, scipy.stats). Navegue pelo menu à esquerda.</p>')
    out.append('<p class="hero-authors">Pedro Torres · Gilberto Weissmuller</p>')
    out.append('</div>')
    out.append('<div class="cards">')
    descs = {
        "Introdução": "Amostra, população, variáveis, histogramas, curva normal e amostragem.",
        "Estatística Descritiva": "Tendência central, dispersão e o teorema do limite central.",
        "Probabilidade": "Eventos, testes diagnósticos, ROC e distribuição binomial.",
        "Distribuições amostrais": "De onde vêm as distribuições t, χ² e F.",
        "Estatística Inferencial": "Intervalos, testes t, ANOVA, qui-quadrado, regressão e potência.",
        "Tabelas estatísticas": "Tabelas Z, t, χ² e F para consulta.",
        "Exercícios": "Exercícios resolvidos por tema, com soluções em Python.",
    }
    for si, (sec, items) in enumerate(sections, 1):
        page = SECTION_FILES.get(sec, "index.html")
        first = slugify(items[0][1]) if items else ""
        out.append(f'<a class="card" href="{page}#{first}">'
                   f'<div class="cnum">{si}</div>'
                   f'<div class="ctitle">{sec}</div>'
                   f'<div class="cdesc">{descs.get(sec,"")}</div>'
                   f'<div class="ccount">{len(items)} tópicos</div></a>')
    out.append('</div>')
    out.append(footer())
    out.append('</main>')
    out.append(FOOT)
    (BASE / "index.html").write_text("\n".join(out), encoding="utf-8")


def main():
    sections = parse_summary()
    write_index(sections)
    for i in range(len(sections)):
        page = write_section_page(i, sections)
        print(f"  {page}  ({(BASE/page).stat().st_size/1024:.1f} KB)")
    print(f"  index.html  ({(BASE/'index.html').stat().st_size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
