# Média cortada (truncada)

A **média cortada** é uma variação da média aritmética em que **removemos uma porcentagem dos valores extremos** antes de calcular a média.

## A ideia

Como a média comum é sensível a outliers, uma forma de torná-la mais **robusta** é descartar uma fatia dos valores mais altos e mais baixos. O que sobra é menos influenciado por valores extremos.

## Fórmula

Cortando $k$ valores de cada lado (após ordenar) em uma amostra de $n$:

$$
\bar{x}_{\text{cortada}} = \frac{1}{n - 2k} \sum_{i=k+1}^{n-k} x_{(i)}
$$

onde $x_{(i)}$ é o $i$-ésimo valor **ordenado**.

Costuma-se especificar o corte em **porcentagem**: cortar 10% significa remover 10% dos valores de cada extremo.

## Exemplo

Dados ordenados: $10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 200$. São 12 valores.

Cortando 10% de cada lado → removemos 1 de cada extremo (10 e 200):

$$
\bar{x}_{\text{cortada 10\%}} = \frac{11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20}{10} = 15{,}5
$$

Compare com a média comum: $\approx 30{,}4$ (puxada pelo 200).

## Quanto cortar?

| Corte | Comentário |
| --- | --- |
| 0% | é a média comum |
| 5% | corte leve, comum em estudos esportivos |
| 10–25% | reduz bem a influência de outliers |
| 50% | é a **mediana** |

## Onde aparece

- Olimpíadas, ginástica artística: descartam-se a maior e a menor nota dos juízes.
- Notas finais de programas que ignoram a melhor e a pior prova.
- Estudos econômicos que querem reduzir o impacto de valores extremos.

## Vantagens e desvantagens

| Vantagem | Desvantagem |
| --- | --- |
| Mais robusta a outliers que a média | Descarta informação |
| Mantém a interpretação de "média" | Definição depende do corte escolhido |
