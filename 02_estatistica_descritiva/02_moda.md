# Moda

A **moda** é o valor que aparece com maior frequência em um conjunto de dados.

## Definição

Dado um conjunto $\{x_1, x_2, \ldots, x_n\}$, a moda é o valor (ou valores) que mais se repete.

## Casos

| Caso | Nome |
| --- | --- |
| Um único valor mais frequente | **unimodal** |
| Dois valores empatados | **bimodal** |
| Três ou mais valores empatados | **multimodal** |
| Todos diferentes | **amodal** (sem moda) |

### Exemplos

- $\{1, 2, 2, 3, 4\}$ → moda = 2 (unimodal).
- $\{1, 2, 2, 3, 3\}$ → modas = 2 e 3 (bimodal).
- $\{1, 2, 3, 4, 5\}$ → não há moda (amodal).

## Quando usar

A moda é particularmente útil em:

- **Variáveis categóricas**, em que média e mediana nem fazem sentido. Ex.: a moda do tipo sanguíneo no Brasil é "O+".
- **Distribuições com picos claros**, em que a "categoria mais comum" é a informação de interesse.

> Em distribuições contínuas, é raro dois valores serem **exatamente** iguais. Nesses casos, a moda é localizada visualmente no histograma: corresponde ao **pico** da distribuição.

## Limitações

1. **Pode não ser única** ou nem existir.
2. **Não usa todos os dados**: depende apenas das frequências.
3. **Sensível à precisão** dos dados: arredondar pode mudar drasticamente a moda.

## Distribuições multimodais — uma pista

Quando o histograma tem **mais de um pico**, vale investigar: pode haver duas subpopulações misturadas. Por exemplo, a altura de adultos mostra um histograma bimodal quando misturamos homens e mulheres — cada grupo tem sua própria moda.
