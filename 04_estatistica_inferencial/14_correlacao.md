# Correlação

A **correlação** quantifica a força e a direção da associação **linear** entre duas variáveis numéricas.

## Coeficiente de Pearson ($r$)

O mais usado quando ambas as variáveis são quantitativas e aproximadamente normais.

$$
r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^{2}} \cdot \sqrt{\sum_{i=1}^{n} (y_i - \bar{y})^{2}}}
$$

## Interpretação

| $r$ | Significado |
| --- | --- |
| **+1** | Correlação positiva perfeita (todos os pontos em uma reta crescente) |
| **+0,5** | Correlação positiva moderada |
| **0** | Nenhuma associação linear |
| **−0,5** | Correlação negativa moderada |
| **−1** | Correlação negativa perfeita |

## Valor de p para correlação

Testamos se $r$ é diferente de zero:

$$
H_0: \rho = 0 \quad \text{vs.} \quad H_1: \rho \neq 0
$$

A estatística do teste é:

$$
t = r \sqrt{\frac{n - 2}{1 - r^{2}}}
$$

com $n - 2$ graus de liberdade. Pacotes como `scipy.stats.pearsonr` fazem isso automaticamente.

## Coeficiente de determinação ($r^2$)

$$
r^{2} = (\text{coef. de Pearson})^{2}
$$

Interpretação: **fração da variabilidade de $y$ explicada por $x$** (em modelo linear). Vai de 0 a 1.

Exemplo: $r = 0{,}8$ → $r^{2} = 0{,}64$ → 64% da variabilidade de $y$ é "explicada" por $x$.

## Spearman ($\rho$) — não paramétrica

Substitui Pearson quando:

- Os dados não são normais;
- A relação é monotônica mas não linear;
- Há outliers ou dados ordinais.

A ideia é calcular Pearson **nos postos** (*ranks*), não nos valores originais.

$$
\rho_s = \text{Pearson aplicado aos postos de } x \text{ e } y
$$

## Kendall ($\tau$) — outra alternativa não paramétrica

Mede a concordância de pares ordenados. Para cada par $(x_i, y_i)$, $(x_j, y_j)$ pergunta-se se ambos sobem ou ambos descem. Mais robusto a outliers, mas computacionalmente mais caro.

## Cuidados importantes

### 1. Correlação NÃO implica causalidade

Duas variáveis podem correlacionar por:

- $X$ causa $Y$;
- $Y$ causa $X$;
- Uma terceira variável causa ambas (confundidor);
- Pura coincidência (especialmente em séries temporais).

> Um exemplo famoso: o consumo de chocolate per capita correlaciona com o número de Prêmios Nobel por país. Isso **não significa** que comer chocolate ganha Nobel.

### 2. Pearson só detecta relações lineares

Variáveis podem ter relação **forte mas não linear** e Pearson dar zero. Por exemplo, $y = x^2$ no intervalo $[-1, 1]$.

### 3. Outliers podem distorcer

Um único ponto extremo pode tanto **criar** uma correlação inexistente quanto **mascarar** uma correlação real.

### 4. Sempre faça um diagrama de dispersão

O quarteto de Anscombe mostra que datasets muito diferentes podem ter o mesmo $r$. **Olhar o gráfico** é essencial.

## Quando usar cada um

| Caso | Recomendação |
| --- | --- |
| Duas variáveis quantitativas, ambas aproximadamente normais | Pearson |
| Dados ordinais | Spearman ou Kendall |
| Variáveis não normais ou com outliers | Spearman |
| Relação monotônica não linear | Spearman |
| Amostras muito pequenas | Kendall |

## Tabela de exemplos

Em pinguins:

| Par | r de Pearson |
| --- | --- |
| Comprimento da nadadeira × massa | ~0,87 (forte positivo) |
| Comprimento do bico × profundidade do bico | ~−0,24 (fraco negativo) |
| Massa × ano de coleta | ~0 (independentes) |

## Relação com regressão

A correlação $r$ tem **sinal igual** ao da inclinação da reta de regressão. O coeficiente de determinação $r^2$ é exatamente o mesmo $R^2$ que aparece em regressão linear simples.
