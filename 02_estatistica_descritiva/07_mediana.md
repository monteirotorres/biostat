# Mediana

A **mediana** é o valor que ocupa a posição do meio quando os dados estão ordenados. Divide o conjunto em duas metades de tamanho igual.

## Como calcular

1. **Ordene** os valores em ordem crescente.
2. Se $n$ é **ímpar**, a mediana é o valor central.
3. Se $n$ é **par**, a mediana é a **média dos dois valores centrais**.

### Exemplo (n ímpar)

Dados: $3, 1, 4, 1, 5, 9, 2$
Ordenados: $1, 1, 2, \mathbf{3}, 4, 5, 9$
Mediana = **3**.

### Exemplo (n par)

Dados: $3, 1, 4, 1, 5, 9, 2, 6$
Ordenados: $1, 1, 2, \mathbf{3}, \mathbf{4}, 5, 6, 9$
Mediana = $(3 + 4)/2 = 3{,}5$.

## A propriedade fundamental

Exatamente **50% dos dados estão abaixo** da mediana e **50% acima**. Por isso ela também é chamada de **segundo quartil** ($Q_2$) ou **percentil 50**.

## Robustez a outliers

A grande vantagem da mediana é não ser afetada por valores extremos:

| Dados | Média | Mediana |
| --- | --- | --- |
| $1, 2, 3, 4, 5$ | 3,0 | 3 |
| $1, 2, 3, 4, 500$ | 102,0 | 3 |

A média explodiu, mas a mediana ficou igual. É por isso que reportamos mediana para variáveis como **renda**, **tempo até um evento**, **dose recebida** etc.

## Generalização — quantis e percentis

A mesma ideia da mediana se estende para outros pontos da distribuição:

| Nome | O que é |
| --- | --- |
| Mediana / Q2 / P50 | 50% dos dados abaixo |
| Q1 / P25 | 25% dos dados abaixo |
| Q3 / P75 | 75% dos dados abaixo |
| P10, P90 | percentis 10 e 90 |

Esses pontos aparecem no **boxplot** e dão uma visão muito mais rica que apenas a média.

## Limitações

- Em **amostras pequenas**, a mediana pode ser instável: mudar 1 valor pode mudar muito.
- Não é tão sensível à **forma** da distribuição — duas distribuições muito diferentes podem ter a mesma mediana.
- Operações algébricas (combinar grupos, propagar erros) são mais complicadas com mediana do que com média.
