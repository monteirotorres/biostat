# Regressão linear simples

A regressão linear ajusta uma **reta** que descreve como uma variável $y$ depende de uma variável $x$.

## O modelo

$$
y = \beta_0 + \beta_1 \cdot x + \varepsilon
$$

Onde:

- $\beta_0$: **intercepto** (valor de $y$ quando $x = 0$);
- $\beta_1$: **inclinação** (quanto $y$ muda para cada unidade de $x$);
- $\varepsilon$: erro aleatório (incluí tudo o que $x$ não explica).

Após o ajuste, ficamos com:

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 \cdot x
$$

## Como ajustar — método dos mínimos quadrados

A reta é escolhida para **minimizar a soma dos quadrados dos resíduos**:

$$
\sum_{i=1}^{n} (y_i - \hat{y}_i)^{2}
$$

As soluções explícitas:

$$
\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^{2}}
$$

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \cdot \bar{x}
$$

Repare: a inclinação está **diretamente ligada à covariância** entre $x$ e $y$ (numerador).

## Interpretação

- $\hat{\beta}_1$ é a **mudança esperada em $y$ por unidade de $x$**.
- Se $x$ está em kg e $y$ em mmHg, $\hat{\beta}_1$ está em "mmHg por kg".

> A reta passa **sempre pelo ponto $(\bar{x}, \bar{y})$**.

## Coeficiente de determinação $R^{2}$

$$
R^{2} = 1 - \frac{\sum (y_i - \hat{y}_i)^{2}}{\sum (y_i - \bar{y})^{2}}
$$

Em palavras: a fração da variabilidade de $y$ "explicada" pelo modelo.

| $R^{2}$ | Interpretação |
| --- | --- |
| 1 | Reta passa por todos os pontos |
| 0,8 | Modelo captura 80% da variabilidade |
| 0 | Modelo não é melhor que a média de $y$ |

## Significância da inclinação

Pacotes (como `scipy.stats.linregress`) testam:

$$
H_0: \beta_1 = 0 \quad \text{vs.} \quad H_1: \beta_1 \neq 0
$$

Se rejeitamos H₀, há evidência de que $x$ está linearmente associado a $y$.

## Suposições

1. **Linearidade**: a relação entre $x$ e $y$ é razoavelmente linear.
2. **Independência** das observações.
3. **Homocedasticidade**: a variabilidade dos resíduos é constante ao longo de $x$.
4. **Normalidade dos resíduos** (necessário só para testes de hipótese e ICs).
5. **Sem outliers extremos** que distorçam o ajuste.

## Diagnóstico do modelo

Olhe sempre:

- **Diagrama de dispersão** dos dados originais — a relação parece linear?
- **Gráfico de resíduos** vs. $x$ — há padrão (curva, leque)?
- **Q-Q plot dos resíduos** — são aproximadamente normais?

## Exemplo

Em pinguins, relacionando comprimento da nadadeira ($x$, em mm) com massa corporal ($y$, em g):

$$
\hat{y} = -5800 + 49{,}7 \cdot x
$$

Interpretação:

- Cada 1 mm adicional de nadadeira está associado a 49,7 g a mais de massa.
- O intercepto (-5800 g) é só uma extrapolação matemática — não tem significado biológico, pois nenhum pinguim tem nadadeira zero.

## Predição

O modelo pode ser usado para prever $y$ dado um novo $x$:

$$
\hat{y}_{\text{novo}} = \hat{\beta}_0 + \hat{\beta}_1 \cdot x_{\text{novo}}
$$

> Cuidado: **não extrapole** muito além do intervalo dos dados originais. O modelo não tem informação sobre o que acontece fora do range observado.

## Regressão múltipla

Generalização para vários preditores:

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2 + \cdots + \hat{\beta}_k x_k
$$

Cada coeficiente é o efeito de seu preditor **mantendo os outros constantes**. Para isso, normalmente usa-se `statsmodels` ou `scikit-learn` (fora do escopo desta introdução).

## Erros comuns

1. **Reportar $R^2$ alto como prova de causalidade.** $R^2$ mede ajuste, não causalidade.
2. **Confundir correlação com regressão.** A correlação é simétrica ($r_{xy} = r_{yx}$); a regressão não — a inclinação de $y$ em $x$ não é igual à de $x$ em $y$.
3. **Não verificar suposições** antes de interpretar.
4. **Extrapolar** além dos dados observados.
