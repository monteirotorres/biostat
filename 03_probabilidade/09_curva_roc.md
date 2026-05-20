# Curva ROC

A **curva ROC** (em inglês, *Receiver Operating Characteristic*) descreve como um teste se comporta para **vários valores de corte**.

## A ideia

Muitos exames retornam **um número**, e a decisão de "positivo ou negativo" depende de um valor de corte. Por exemplo:

- glicemia em jejum > 126 mg/dL → diabetes;
- PSA > 4 ng/mL → suspeita de câncer de próstata;
- febre > 37,8 °C → suspeita de infecção.

Mudar o corte muda a sensibilidade e a especificidade. A curva ROC mostra **todas** as combinações possíveis dessas duas medidas, à medida que o corte varia.

## Construção da curva

No eixo de cada ponto da curva:

| Eixo | O que é |
| --- | --- |
| Eixo **x** | $1 - \text{Especificidade}$ (taxa de falsos positivos) |
| Eixo **y** | Sensibilidade (taxa de verdadeiros positivos) |

Cada ponto corresponde a um valor de corte. Variando o corte, descrevemos uma curva.

## Interpretação visual

![Curva ROC para testes de diferentes qualidades](assets/roc_exemplo.png)

- A **diagonal** representa um teste **inútil**, equivalente a sortear no cara-ou-coroa.
- Quanto mais a curva se aproxima do **canto superior esquerdo**, melhor o teste.

## AUC — área sob a curva

A medida mais usada para comparar curvas ROC é a **área sob a curva** (*Area Under the Curve*):

$$
0 \leq \text{AUC} \leq 1
$$

| AUC | Interpretação |
| --- | --- |
| 1,0 | Teste perfeito |
| 0,9–1,0 | Excelente |
| 0,8–0,9 | Bom |
| 0,7–0,8 | Razoável |
| 0,5–0,7 | Fraco |
| 0,5 | Equivalente ao acaso |
| < 0,5 | Pior que acaso (inverter o critério resolve) |

## Como escolher o ponto de corte ideal?

Não existe resposta universal — depende do contexto clínico:

1. **Ponto mais próximo do canto (0,1)**: minimiza a distância euclidiana ao teste perfeito.
2. **Índice de Youden**: maximiza $\text{Sens.} + \text{Esp.} - 1$.
3. **Trade-off custo-benefício**: pondera o custo de um FP versus um FN.

Por exemplo, em **triagem**, escolhemos um corte que prioriza sensibilidade (não perder doentes). Em **confirmação**, priorizamos especificidade.

## Aplicações típicas

- Avaliação de **novos biomarcadores** versus padrão-ouro.
- Comparação entre **dois testes** para a mesma doença.
- Comparação de **modelos de aprendizado de máquina** para classificação.
- Definição de **valores de corte** clínicos.

## Vantagem da ROC

A curva ROC sintetiza, em **um único gráfico**, o desempenho do teste em **todos** os pontos de corte possíveis. Por isso é a forma padrão de reportar a performance de um teste diagnóstico em artigos científicos.
