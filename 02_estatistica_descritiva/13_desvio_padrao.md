# Desvio padrão

A raiz quadrada da variância. É a medida de dispersão mais reportada em ciência.

## Fórmulas

### População

$$
\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^{2}}
$$

### Amostra

$$
s = \sqrt{\frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^{2}}
$$

A correção $(n-1)$ no denominador é a mesma da variância amostral.

## Por que tirar a raiz?

Para voltar à **unidade original** dos dados. Se $x$ está em kg, $s$ também está em kg — e podemos dizer coisas como "o peso médio é $70 \pm 5$ kg" de forma direta.

## Interpretação

> Em média, os dados se afastam $s$ unidades da média.

Em uma distribuição **aproximadamente normal**, vale a regra 68–95–99,7:

| Intervalo | % dos dados |
| --- | --- |
| $\bar{x} \pm s$ | ~68% |
| $\bar{x} \pm 2s$ | ~95% |
| $\bar{x} \pm 3s$ | ~99,7% |

Em distribuições não-normais, essas porcentagens são apenas aproximadas. Mas vale uma garantia mais fraca, válida para qualquer distribuição:

### Desigualdade de Chebyshev

$$
P(|X - \mu| < k\sigma) \geq 1 - \frac{1}{k^{2}}
$$

Por exemplo, **pelo menos 75%** dos dados estão dentro de $\mu \pm 2\sigma$, mesmo que a distribuição seja muito esquisita.

## Erro padrão da média

Cuidado para não confundir:

- **Desvio padrão** ($s$): variabilidade dos **dados** individuais.
- **Erro padrão da média** (SEM): variabilidade da **média amostral**.

$$
\text{SEM} = \frac{s}{\sqrt{n}}
$$

O SEM **sempre é menor** que $s$ e diminui à medida que aumentamos a amostra. É o desvio padrão da distribuição amostral da média (vem do TLC).

| Quando reportar | Por quê |
| --- | --- |
| Desvio padrão | Para descrever a **variabilidade dos indivíduos** |
| SEM | Para descrever a **precisão da estimativa da média** |

> Atenção: o SEM é menor, então faz a barra de erro parecer pequena. Mas isso **não significa** menos variabilidade nos dados — só significa que com $n$ grande estimamos a média com mais precisão.

## Em artigos científicos

A convenção mais comum é reportar:

- **Variável contínua e simétrica**: $\bar{x} \pm s$.
- **Em gráficos com barras de erro**: especificar se a barra é desvio padrão, SEM ou IC 95%. **Nunca** deixe ambíguo.
