# Matriz de confusão

A **matriz de confusão** é uma tabela 2x2 (ou maior, para múltiplas categorias) que mostra **onde o teste acertou e onde errou**.

O nome vem da ideia de que ela mostra **onde o classificador se confundiu**: em vez de só dizer "70% de acertos", ela mostra **quais classes foram trocadas por quais**.

## Versão 2x2 (clássica)

|   | Real positivo | Real negativo |
| --- | --- | --- |
| **Previsto positivo** | VP (verdadeiro positivo) | FP (falso positivo) |
| **Previsto negativo** | FN (falso negativo) | VN (verdadeiro negativo) |

## Métricas derivadas

A partir dessa tabela conseguimos calcular várias métricas, cada uma respondendo a uma pergunta diferente:

| Métrica | Fórmula | Pergunta |
| --- | --- | --- |
| **Acurácia** | $\dfrac{\text{VP} + \text{VN}}{\text{total}}$ | "Qual a fração de acertos?" |
| **Sensibilidade** | $\dfrac{\text{VP}}{\text{VP} + \text{FN}}$ | "Dos doentes, quantos pegamos?" |
| **Especificidade** | $\dfrac{\text{VN}}{\text{VN} + \text{FP}}$ | "Dos saudáveis, quantos descartamos?" |
| **VPP** (precisão) | $\dfrac{\text{VP}}{\text{VP} + \text{FP}}$ | "Dos positivos do teste, quantos têm a doença?" |
| **VPN** | $\dfrac{\text{VN}}{\text{VN} + \text{FN}}$ | "Dos negativos do teste, quantos não têm?" |
| **F1-score** | média harmônica de sensibilidade e VPP | balanço entre as duas |

## Por que "acurácia" sozinha engana

Imagine uma doença rara que afeta 1% da população. Um teste que dá **sempre negativo** acerta 99% dos casos. A acurácia parece ótima, mas o teste é inútil — não identifica nenhum doente.

Por isso, em desbalanceamento de classes, é essencial olhar **sensibilidade e VPP** separadamente.

## Versão multiclasse

Quando há mais de duas categorias, a matriz fica $k \times k$. Linhas são previsões, colunas são valores reais (ou vice-versa, conforme convenção).

Exemplo: classificar espécies de pinguins.

|   | Real Adelie | Real Chinstrap | Real Gentoo |
| --- | --- | --- | --- |
| Pred Adelie | 142 | 3 | 1 |
| Pred Chinstrap | 4 | 65 | 0 |
| Pred Gentoo | 0 | 0 | 119 |

Os elementos da **diagonal** são acertos. Fora da diagonal, é onde o modelo "se confundiu".

## Como interpretar a diagonal

- **Diagonal forte** = classificador bom.
- **Padrão fora da diagonal** = revela onde estão os erros (ex.: o modelo confunde frequentemente Adelie com Chinstrap).

## Visualização

Heatmap é a forma padrão de mostrar matrizes de confusão: a intensidade de cor mostra rapidamente onde estão os acertos e os erros.

## Em pesquisa clínica

A matriz de confusão é a forma padrão de reportar resultados de:

- testes diagnósticos novos vs. padrão-ouro;
- ferramentas de triagem;
- modelos de aprendizado de máquina aplicados a imagens médicas, ECGs, sequências genéticas, etc.
