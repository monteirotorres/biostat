"""Monta o PPTX de Bioestatística no estilo do site (paleta bege/azul,
títulos serifados), com figuras estáticas geradas por gerar_figuras_slides.py.
Layout inspirado nos slides originais: título no topo, marca IBCCF, número."""

from pathlib import Path
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

BASE = Path(__file__).parent.parent
FIG = BASE / "assets" / "slides"
LOGO = BASE / "assets" / "ibccf-logo.png"
OUT = BASE / "bioestatistica_slides.pptx"

# paleta
BG = RGBColor(0xF3, 0xEC, 0xDF)
PAPER = RGBColor(0xFF, 0xFD, 0xF8)
INK = RGBColor(0x1A, 0x1A, 0x1A)
BLUE = RGBColor(0x32, 0x66, 0xAD)
RED = RGBColor(0xC0, 0x39, 0x2B)
MUTED = RGBColor(0x6B, 0x64, 0x57)
LINE = RGBColor(0xC9, 0xBF, 0xA9)

SERIF = "Georgia"
MONO = "Consolas"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

_num = 0


def _bg(slide, color=BG):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    sh.fill.solid(); sh.fill.fore_color.rgb = color
    sh.line.fill.background()
    sh.shadow.inherit = False
    slide.shapes._spTree.remove(sh._element)
    slide.shapes._spTree.insert(2, sh._element)
    return sh


def _box(slide, l, t, w, h):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tb.text_frame.word_wrap = True
    return tb


def _set(p, text, size, color=INK, bold=False, font=SERIF, italic=False):
    p.text = text
    for r in p.runs:
        r.font.size = Pt(size); r.font.color.rgb = color
        r.font.bold = bold; r.font.name = font; r.font.italic = italic


def _rect(slide, l, t, w, h, color):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    sh.fill.solid(); sh.fill.fore_color.rgb = color
    sh.line.fill.background(); sh.shadow.inherit = False
    return sh


def _img_fit(slide, path, l, t, w, h):
    iw, ih = Image.open(path).size
    ar = iw / ih; box_ar = w / h
    if ar > box_ar:
        nw = w; nh = int(w / ar)
    else:
        nh = h; nw = int(h * ar)
    nl = l + (w - nw) // 2; nt = t + (h - nh) // 2
    slide.shapes.add_picture(str(path), nl, nt, nw, nh)


def _footer(slide):
    global _num
    _num += 1
    tb = _box(slide, Inches(0.5), Inches(7.05), Inches(6), Inches(0.4))
    _set(tb.text_frame.paragraphs[0], "Bioestatística · IBCCF · UFRJ", 10, MUTED, font=MONO)
    nb = _box(slide, Inches(12.3), Inches(7.05), Inches(0.8), Inches(0.4))
    p = nb.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT
    _set(p, str(_num), 10, MUTED, font=MONO)


def title_slide():
    s = prs.slides.add_slide(BLANK); _bg(s)
    if LOGO.exists():
        _img_fit(s, LOGO, Inches(4.67), Inches(1.1), Inches(4.0), Inches(1.3))
    tb = _box(s, Inches(1), Inches(2.8), Inches(11.33), Inches(1.6))
    _set(tb.text_frame.paragraphs[0], "Bioestatística", 60, INK, bold=True)
    tb.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    sub = _box(s, Inches(1), Inches(4.3), Inches(11.33), Inches(0.6))
    p = sub.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    _set(p, "Instituto de Biofísica Carlos Chagas Filho · UFRJ", 18, MUTED, font=MONO)
    au = _box(s, Inches(1), Inches(5.3), Inches(11.33), Inches(0.8))
    p = au.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    _set(p, "Pedro Torres   ·   Gilberto Weissmuller", 18, INK)


def section_slide(num, title):
    s = prs.slides.add_slide(BLANK); _bg(s)
    _rect(s, Inches(1), Inches(3.0), Inches(1.4), Inches(0.12), BLUE)
    nb = _box(s, Inches(1), Inches(2.0), Inches(3), Inches(1.0))
    _set(nb.text_frame.paragraphs[0], f"Parte {num}", 22, BLUE, font=MONO)
    tb = _box(s, Inches(1), Inches(3.3), Inches(11), Inches(1.6))
    _set(tb.text_frame.paragraphs[0], title, 46, INK, bold=True)
    _footer(s)


def content_slide(eyebrow, title, bullets=None, image=None, caption=None):
    s = prs.slides.add_slide(BLANK); _bg(s)
    # eyebrow
    eb = _box(s, Inches(0.7), Inches(0.45), Inches(11), Inches(0.4))
    _set(eb.text_frame.paragraphs[0], eyebrow.upper(), 12, MUTED, font=MONO)
    # title
    tb = _box(s, Inches(0.7), Inches(0.8), Inches(12), Inches(1.0))
    _set(tb.text_frame.paragraphs[0], title, 30, INK, bold=True)
    _rect(s, Inches(0.72), Inches(1.75), Inches(1.1), Inches(0.05), BLUE)

    top = Inches(2.1)
    if bullets and image:
        # bullets left, image right
        _bullets(s, bullets, Inches(0.7), top, Inches(5.4), Inches(4.6))
        _img_fit(s, FIG / image, Inches(6.4), top, Inches(6.4), Inches(4.5))
    elif image:
        _img_fit(s, FIG / image, Inches(1.2), top, Inches(11.0), Inches(4.6))
        if caption:
            cb = _box(s, Inches(1), Inches(6.55), Inches(11.33), Inches(0.4))
            p = cb.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
            _set(p, caption, 12, MUTED, italic=True)
    elif bullets:
        _bullets(s, bullets, Inches(0.9), top, Inches(11.5), Inches(4.6), size=20)
    _footer(s)


def _bullets(slide, items, l, t, w, h, size=18):
    tb = _box(slide, l, t, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        _set(p, "•  " + it, size, INK)
        p.space_after = Pt(10); p.line_spacing = 1.1


def refs_slide():
    s = prs.slides.add_slide(BLANK); _bg(s)
    tb = _box(s, Inches(0.7), Inches(0.7), Inches(11), Inches(1))
    _set(tb.text_frame.paragraphs[0], "Referências e contato", 30, INK, bold=True)
    _rect(s, Inches(0.72), Inches(1.65), Inches(1.1), Inches(0.05), BLUE)
    if LOGO.exists():
        _img_fit(s, LOGO, Inches(0.9), Inches(2.4), Inches(4.5), Inches(1.5))
    cb = _box(s, Inches(0.9), Inches(4.2), Inches(11), Inches(2))
    tf = cb.text_frame
    _set(tf.paragraphs[0], "Material teórico completo e interativo:", 18, INK)
    p = tf.add_paragraph(); _set(p, "monteirotorres.github.io/biostat", 18, BLUE, font=MONO)
    p = tf.add_paragraph(); _set(p, " ", 10)
    p = tf.add_paragraph(); _set(p, "Contato: monteirotorres@biof.ufrj.br", 16, MUTED, font=MONO)
    _footer(s)


# ============================ CONTEÚDO ============================
title_slide()

# ---- Parte 1 ----
section_slide(1, "Introdução")
content_slide("Introdução", "Amostra e população", bullets=[
    "População: todos os indivíduos de interesse — parâmetros μ e σ, em geral desconhecidos.",
    "Amostra: subconjunto que medimos — estatísticas x̄ e s, calculadas dos dados.",
    "A amostragem aleatória é o que permite generalizar da amostra para a população.",
    "Ideia central: medimos a amostra para aprender sobre a população.",
])
content_slide("Introdução", "Descrição vs. inferência", bullets=[
    "Estatística descritiva: resume os dados que temos em mãos.",
    "Estatística inferencial: generaliza para a população, sempre com incerteza.",
    "A inferência quantifica essa incerteza — ela não a elimina.",
    "Regra de ouro: descreva os dados antes de inferir qualquer coisa.",
])
content_slide("Introdução", "Precisão e acurácia", image="precisao.png",
              caption="Acurácia: proximidade do valor verdadeiro. Precisão: consistência entre as medidas.")
content_slide("Introdução", "Algarismos significativos", bullets=[
    "Refletem a precisão real do instrumento de medida.",
    "Zeros à esquerda não contam; à direita após a vírgula, contam.",
    "Em operações, o resultado segue o termo menos preciso.",
    "Notação científica elimina a ambiguidade dos zeros.",
])
content_slide("Introdução", "Tipos de variáveis", bullets=[
    "Qualitativas: nominais (sem ordem) e ordinais (com ordem).",
    "Quantitativas: discretas (contagens) e contínuas (medidas).",
    "O tipo da variável determina o gráfico e o teste adequados.",
])
content_slide("Introdução", "Histogramas", image="histograma.png",
              caption="O histograma revela forma, centro, dispersão e a presença de outliers.")
content_slide("Introdução", "Curva normal", image="normal.png",
              caption="Definida por μ e σ; vale a regra 68–95–99,7 e a padronização Z = (X − μ)/σ.")
content_slide("Introdução", "Técnicas de amostragem", bullets=[
    "Amostragem probabilística: aleatória simples, estratificada, conglomerados.",
    "A aleatorização neutraliza as variáveis de confusão.",
    "Voluntários geram viés de seleção — evite-os ao comparar intervenções.",
    "Pareamento e blocos reduzem a variabilidade conhecida.",
])

# ---- Parte 2 ----
section_slide(2, "Estatística Descritiva")
content_slide("Descritiva", "Medidas de tendência central", image="tendencia.png",
              caption="A média é sensível a valores extremos; a mediana é robusta.")
content_slide("Descritiva", "Variações da média", bullets=[
    "Aritmética: a soma dividida pela contagem.",
    "Ponderada: cada valor entra com um peso.",
    "Geométrica: apropriada para dados multiplicativos (taxas, diluições).",
    "Cortada: descarta os extremos para reduzir o efeito de outliers.",
])
content_slide("Descritiva", "Média vs. mediana", bullets=[
    "Distribuição simétrica: média e mediana praticamente coincidem.",
    "Distribuição assimétrica: a mediana representa melhor o caso típico.",
    "Sempre olhe o histograma antes de escolher.",
])
content_slide("Descritiva", "Teorema do limite central", image="tlc.png",
              caption="A média de amostras tende à normal: x̄ ~ N(μ, σ²/n), com erro padrão σ/√n.")
content_slide("Descritiva", "Dispersão", bullets=[
    "Amplitude: maior menos o menor valor (sensível a outliers).",
    "Variância: média dos quadrados dos desvios em relação à média.",
    "Desvio padrão: a raiz da variância, na unidade original dos dados.",
])
content_slide("Descritiva", "Boxplot e quartis", image="boxplot.png",
              caption="O IQR = Q3 − Q1 descreve os 50% centrais e é robusto a outliers.")
content_slide("Descritiva", "Coeficiente de variação", bullets=[
    "CV = s / x̄, expresso em porcentagem — é a dispersão relativa.",
    "Permite comparar variabilidade entre grupos de escalas diferentes.",
    "Só faz sentido em variáveis com zero absoluto.",
])

# ---- Parte 3 ----
section_slide(3, "Probabilidade")
content_slide("Probabilidade", "Eventos e probabilidade", bullets=[
    "0 ≤ P(A) ≤ 1; o complemento dá P(Aᶜ) = 1 − P(A).",
    "União: P(A ∪ B) = P(A) + P(B) − P(A ∩ B).",
    "Eventos independentes: P(A ∩ B) = P(A) · P(B).",
])
content_slide("Probabilidade", "Probabilidade condicional", bullets=[
    "P(A | B) = P(A ∩ B) / P(B).",
    "Teorema de Bayes inverte a condicional.",
    "Atenção: P(A | B) ≠ P(B | A) — base do paradoxo diagnóstico.",
])
content_slide("Probabilidade", "Sensibilidade e especificidade", image="sens_esp.png",
              caption="Sensibilidade = P(+ | doente); especificidade = P(− | saudável). O corte é um trade-off.")
content_slide("Probabilidade", "Valor preditivo", bullets=[
    "VPP: probabilidade de ser doente dado um teste positivo.",
    "VPP e VPN dependem fortemente da prevalência.",
    "Em doenças raras, a maioria dos positivos é falsa, mesmo com bom teste.",
])
content_slide("Probabilidade", "Curva ROC", image="roc.png",
              caption="Mostra o desempenho do teste em todos os cortes; a AUC resume a qualidade.")
content_slide("Probabilidade", "Distribuição binomial", image="binomial.png",
              caption="Conta k sucessos em n tentativas independentes; E[X] = np, Var = np(1 − p).")

# ---- Parte 4 ----
section_slide(4, "Distribuições amostrais")
content_slide("Distribuições amostrais", "De onde vêm t, χ² e F", image="dist_amostral.png",
              caption="Todas surgem da amostragem de variáveis normais; dependem dos graus de liberdade.")
content_slide("Distribuições amostrais", "As três distribuições", bullets=[
    "χ² (qui-quadrado): soma de quadrados de normais — base de variâncias e tabelas.",
    "t de Student: média padronizada com σ estimado; tem caudas mais pesadas.",
    "F: razão de duas variâncias — base da ANOVA.",
    "Com muitos graus de liberdade, tudo se aproxima da normal.",
])

# ---- Parte 5 ----
section_slide(5, "Estatística Inferencial")
content_slide("Inferencial", "Lógica da inferência", bullets=[
    "Assume-se H₀ verdadeira e calcula-se a probabilidade dos dados.",
    "Se essa probabilidade é muito baixa, rejeita-se H₀.",
    "É um filtro consensual contra o acaso e o viés do pesquisador.",
])
content_slide("Inferencial", "Estimação e intervalo de confiança", image="ic.png",
              caption="IC 95%: ao repetir o estudo, 95% dos intervalos conteriam o parâmetro verdadeiro.")
content_slide("Inferencial", "Hipóteses H₀ e H₁", bullets=[
    "H₀: ausência de efeito ou diferença (o status quo).",
    "H₁: existe efeito ou diferença.",
    "Não rejeitar H₀ não é o mesmo que provar H₀.",
])
content_slide("Inferencial", "Nível de significância e valor-p", image="valorp.png",
              caption="O valor-p é a probabilidade de dados tão extremos sob H₀; rejeita-se se p < α.")
content_slide("Inferencial", "Erros tipo I e II", image="erros.png",
              caption="α = falso positivo; β = falso negativo; poder = 1 − β (desejável ≥ 80%).")
content_slide("Inferencial", "Teste t", bullets=[
    "Uma amostra: compara a média com um valor de referência.",
    "Duas amostras independentes: compara dois grupos (Welch por padrão).",
    "Pareado: duas medidas no mesmo indivíduo, mais potente.",
])
content_slide("Inferencial", "ANOVA", image="anova.png",
              caption="Compara 3+ grupos: F = variância entre grupos / variância dentro dos grupos.")
content_slide("Inferencial", "Teste do qui-quadrado", bullets=[
    "Testa associação entre variáveis categóricas.",
    "Compara contagens observadas com as esperadas sob independência.",
    "Depende do número absoluto de observações, não só das proporções.",
])
content_slide("Inferencial", "Correlação", image="correlacao.png",
              caption="r de Pearson mede associação linear; correlação não implica causalidade.")
content_slide("Inferencial", "Regressão linear", image="regressao.png",
              caption="Ajusta uma reta por mínimos quadrados; R² é a fração da variância explicada.")
content_slide("Inferencial", "Design experimental e potência", bullets=[
    "Pilares: controle, aleatorização, repetição e pareamento.",
    "Significância estatística não é o mesmo que relevância prática.",
    "Poder ≥ 80% é a meta; o cálculo amostral deve preceder o estudo.",
])

refs_slide()

prs.save(str(OUT))
print(f"Slides salvos: {OUT}  ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")
