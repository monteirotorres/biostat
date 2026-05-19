# Variância

A medida de dispersão mais usada em estatística clássica. Em vez de tirar o módulo das diferenças, **elevamos ao quadrado**.

## Fórmulas

### Variância populacional

$$
\sigma^{2} = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^{2}
$$

### Variância amostral

$$
s^{2} = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^{2}
$$

A pequena diferença: dividimos por $n - 1$ em vez de $n$. Isso se chama **correção de Bessel** e existe porque, ao usar $\bar{x}$ (calculada da própria amostra) em vez de $\mu$ (verdadeira mas desconhecida), subestimaríamos a variância sem essa correção.

## Exemplo

Dados: $2, 4, 4, 4, 5, 5, 7, 9$. $\bar{x} = 5$.

| $x_i$ | $(x_i - \bar{x})^2$ |
| --- | --- |
| 2 | 9 |
| 4 | 1 |
| 4 | 1 |
| 4 | 1 |
| 5 | 0 |
| 5 | 0 |
| 7 | 4 |
| 9 | 16 |

Soma dos quadrados = 32.

- Variância populacional: $32 / 8 = 4{,}0$.
- Variância amostral: $32 / 7 \approx 4{,}57$.

## Por que elevar ao quadrado?

1. **Elimina o sinal** — todas as parcelas viram positivas.
2. **Penaliza desvios grandes**: um desvio de 4 contribui muito mais (16) que dois desvios de 2 (4+4=8).
3. **Tem propriedades matemáticas convenientes**: diferenciável em todo lugar, comporta-se bem em operações.

## O problema da unidade

Se $x$ está em quilogramas, $\sigma^2$ está em **quilogramas ao quadrado** — uma unidade sem significado físico. Por isso, na prática, costuma-se tirar a raiz quadrada e reportar o **desvio padrão** $\sigma$, na mesma unidade dos dados.

## Identidade útil

A variância também pode ser escrita como:

$$
\sigma^{2} = \overline{x^{2}} - (\bar{x})^{2}
$$

Em palavras: **a média dos quadrados menos o quadrado da média**.

## Propriedades importantes

| Propriedade | Fórmula |
| --- | --- |
| Soma de uma constante | $\text{Var}(X + c) = \text{Var}(X)$ |
| Multiplicação por constante | $\text{Var}(c \cdot X) = c^{2} \cdot \text{Var}(X)$ |
| Soma de variáveis independentes | $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ |

A última é a base de muitos resultados em estatística — **variâncias se somam** quando as variáveis são independentes.

## Por que isso aparece no denominador de testes?

Em estatística inferencial, a variância aparece dividindo a diferença observada — basicamente para perguntar:

> "Essa diferença é grande **comparada à variabilidade natural** dos dados?"

Essa é a ideia por trás de praticamente todos os testes paramétricos (t, z, ANOVA, F).
