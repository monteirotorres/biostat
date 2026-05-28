# Design experimental e potência

Um bom resultado estatístico começa **antes** da coleta de dados — no **planejamento** do experimento. Nenhuma análise conserta um experimento mal desenhado.

## Os pilares de um bom experimento

| Princípio | O que é |
| --- | --- |
| **Controle** | manter constantes as variáveis que não estão sendo estudadas |
| **Aleatorização** | sortear quem recebe cada tratamento (neutraliza confundidores) |
| **Repetição** | medir vários indivíduos (reduz o efeito do acaso) |
| **Pareamento/blocos** | agrupar unidades semelhantes para reduzir variabilidade |

## Experimento verdadeiro vs. estudo observacional

| | Experimento verdadeiro | Estudo de correlação/observacional |
| --- | --- | --- |
| Variável manipulada? | sim, pelo pesquisador | não, apenas observada |
| Aleatorização? | sim | não |
| Permite causa-efeito? | sim | **não**, apenas associação |
| Exemplo | ensaio clínico randomizado | coorte, caso-controle |

> Lembre: **correlação não é causa**. Só o experimento controlado e aleatorizado permite afirmar causalidade.

## Significância vs. relevância

Um erro comum é confundir os dois:

- **Significância estatística**: a diferença é grande o bastante para ser detectada pelo design (depende de $n$, variabilidade, pareamento).
- **Relevância (tamanho de efeito)**: a diferença é grande o bastante para **importar** na prática.

> Exemplo clássico: com $n$ enorme, é possível detectar uma diferença significativa de 0,1 ponto de QI entre primogênitos e caçulas. É **significativo**, mas **irrelevante** na prática. Por outro lado, um efeito antitérmico de 0,1 °C é estatisticamente detectável e clinicamente inútil.

Sempre reporte **ambos**: o valor-p **e** o tamanho de efeito (com intervalo de confiança).

## Poder estatístico

O **poder** é a probabilidade de detectar um efeito que **realmente existe**:

$$
\text{poder} = 1 - \beta = P(\text{rejeitar } H_0 \mid H_1 \text{ verdadeira})
$$

Convenção: queremos poder **≥ 80%**.

O poder depende de quatro fatores interligados — fixados três, o quarto está determinado:

| Fator | Efeito no poder |
| --- | --- |
| Tamanho da amostra $n$ | ↑ n → ↑ poder |
| Tamanho do efeito real $\delta$ | ↑ efeito → ↑ poder |
| Variabilidade $\sigma$ | ↑ σ → ↓ poder |
| Nível $\alpha$ | ↑ α → ↑ poder (mas ↑ erro tipo I) |

## Os quatro quadrantes (efeito × variabilidade)

| | Efeito pequeno | Efeito grande |
| --- | --- | --- |
| **Baixa variabilidade** | experimentos difíceis (precisam de muito controle/n) | quadrante fácil |
| **Alta variabilidade** | luta quotidiana (n moderado, raramente conclusivo) | quadrante anômalo |

## Cálculo amostral

A pergunta de planejamento mais importante:

> Quantos indivíduos preciso para ter 80% de poder de detectar um efeito de tamanho $\delta$, com $\alpha = 0{,}05$?

Aproximação para comparação de duas médias:

$$
n \approx 2\left(\frac{z_{1-\alpha/2} + z_{1-\beta}}{\delta/\sigma}\right)^2 \quad \text{(por grupo)}
$$

> Exemplo (da planilha do curso): com $\sigma_1 = \sigma_2 = 1$, $\delta = 1$ e poder de 81%, precisamos de $n \approx 17$ por grupo. Para detectar a diferença real de pressão arterial entre homens e mulheres ($\delta = 3$, $\sigma \approx 17$–$21$), seriam necessários **~568 por grupo** — por isso amostras pequenas dão poder ridiculamente baixo (~7%).

## A armadilha do experimento subdimensionado

Um estudo com poder baixo é eticamente questionável:

- expõe participantes sem chance real de chegar a uma conclusão;
- gera "negativos" que não distinguem "sem efeito" de "amostra pequena demais";
- quando dá positivo, tende a **superestimar** o efeito (a *winner's curse*).

Por isso, o cálculo amostral deve ser feito **antes** do estudo e reportado.

## Slides da aula

▶ [Slides interativos — Planejamento Experimental](planejamento_experimental_slides.html) &nbsp;·&nbsp; [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/monteirotorres/biostat/blob/main/04_estatistica_inferencial/19_planejamento_pratico.ipynb)

## No notebook

Simulamos o poder: para um dado efeito e $n$, rodamos milhares de experimentos e contamos em quantos rejeitamos $H_0$. A fração observada é o poder — e bate com o valor teórico.
