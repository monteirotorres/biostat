# De onde vêm as distribuições t, F e χ²

Até agora usamos a **distribuição normal** o tempo todo. Mas nos testes de hipóteses aparecem outras três distribuições: **qui-quadrado ($\chi^2$)**, **t de Student** e **F**. De onde elas vêm?

A resposta curta: **todas surgem quando combinamos variáveis normais ao calcular estatísticas a partir de amostras.** Elas são as "distribuições da amostragem" — descrevem como certas contas (variâncias, médias padronizadas, razões de variâncias) se comportam quando repetimos a coleta de amostras muitas vezes.

## A ideia central: distribuição amostral

Imagine repetir um experimento **milhares de vezes**, cada vez com uma nova amostra, e calcular uma estatística (a média, a variância, um valor t...). Os valores dessa estatística formam uma distribuição — a **distribuição amostral** daquela estatística.

- A média amostral $\bar{x}$ tem distribuição **normal** (pelo TLC).
- A variância amostral (padronizada) tem distribuição **qui-quadrado**.
- A média padronizada com $\sigma$ desconhecido tem distribuição **t**.
- A razão de duas variâncias tem distribuição **F**.

Não precisamos derivar a matemática. O importante é entender **qual conta gera qual distribuição** e **por que** elas têm a forma que têm.

## Mapa das três distribuições

| Distribuição | Surge de... | Aparece em... |
| --- | --- | --- |
| $\chi^2$ (qui-quadrado) | soma de quadrados de variáveis normais padrão | teste qui-quadrado, variâncias |
| t de Student | normal dividida por um desvio padrão **estimado** | teste t, intervalos de confiança |
| F | razão entre duas variâncias | ANOVA, comparação de variâncias |

## O conceito de graus de liberdade

As três distribuições dependem de um parâmetro chamado **graus de liberdade** (gl). Intuitivamente:

> Graus de liberdade = número de valores que podem variar livremente ao calcular uma estatística.

Exemplo: se temos $n$ valores e já calculamos a média $\bar{x}$, então só $n-1$ desvios são "livres" — o último fica determinado, porque a soma dos desvios é zero. Por isso a variância amostral usa $n-1$ no denominador, e a distribuição t tem $n-1$ graus de liberdade.

Quanto **maiores** os graus de liberdade:

- a distribuição t se aproxima da **normal**;
- a qui-quadrado e a F ficam mais **simétricas**.

Isso reflete uma ideia profunda: **com amostras grandes, a incerteza de estimar parâmetros desaparece**, e tudo volta a se comportar como uma normal.

## Por que isso importa

Quando você roda um teste t no `scipy.stats` e ele devolve um valor-p, por trás está acontecendo:

1. calcula-se uma estatística (t, F ou χ²) a partir dos dados;
2. compara-se essa estatística com a **distribuição teórica** correspondente (sob $H_0$);
3. a área na cauda dá o valor-p.

Entender de onde vêm essas distribuições tira o "mistério" dos testes: eles nada mais são do que perguntar **"quão extremo é meu resultado, comparado ao que o acaso produziria?"**.

Nos próximos tópicos, vemos cada uma em detalhe — e, no notebook, **construímos** cada distribuição por simulação, amostrando de normais e vendo a forma emergir.
