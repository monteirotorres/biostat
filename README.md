# Bioestatística

Material didático de Bioestatística do Instituto de Biofísica Carlos Chagas Filho (IBCCF) — Universidade Federal do Rio de Janeiro (UFRJ).

**Professores:**

- Pedro Torres — [monteirotorres@biof.ufrj.br](mailto:monteirotorres@biof.ufrj.br)
- Gilberto Weissmuller — [gweissmu@biof.ufrj.br](mailto:gweissmu@biof.ufrj.br)

## Site do curso

**Página inicial:** [`index.html`](index.html)

O site é dividido em quatro capítulos, cada um com abas para navegar entre os tópicos:

- [Parte 1 — Introdução](parte1.html)
- [Parte 2 — Estatística Descritiva](parte2.html)
- [Parte 3 — Probabilidade](parte3.html)
- [Parte 4 — Estatística Inferencial](parte4.html)

Diversos tópicos têm **demonstrações interativas** (curva normal, TLC, distribuição binomial, sensibilidade/especificidade, curva ROC, intervalo de confiança, erros tipo I/II, valor-p, correlação, histograma) — manipule os parâmetros e veja o efeito em tempo real.

## Conteúdo

Cada tópico tem um arquivo markdown (`*.md`) com a explicação e um notebook Jupyter (`*.ipynb`) com exemplos práticos em Python.

Os notebooks usam apenas três bibliotecas:

- `pandas` — manipulação de dados
- `seaborn` — visualização
- `scipy.stats` — funções estatísticas

```bash
pip install pandas seaborn scipy jupyter
```

## Regenerar o site

```bash
python3 tools/gerar_site.py
```

O script lê `SUMMARY.md`, converte todos os markdowns para HTML (preservando LaTeX para KaTeX), injeta os widgets interativos e escreve `index.html` e `parte1..4.html`.
