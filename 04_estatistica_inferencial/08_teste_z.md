# Teste z para uma amostra

O teste z é o teste mais simples para comparar uma média amostral com um **valor de referência**. Usa-se quando o **desvio padrão da população ($\sigma$) é conhecido**.

## Quando usar

| Condição | Necessária? |
| --- | --- |
| Variável quantitativa | sim |
| População aproximadamente normal **ou** $n$ grande (TLC) | sim |
| $\sigma$ conhecido | sim |

> Na prática biomédica, $\sigma$ é raramente conhecido. Por isso o teste z para uma amostra é mais comum em **controle de qualidade industrial** ou quando há um padrão histórico bem estabelecido. Em pesquisa, usamos o **teste t** (próximo tópico).

## Hipóteses

$$
H_0: \mu = \mu_0
$$

$$
H_1: \mu \neq \mu_0 \quad (\text{bilateral})
$$

## Estatística do teste

$$
z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
$$

Sob H₀ verdadeira, $z$ segue uma distribuição **normal padrão**.

## Decisão

- **Pelo valor-p**:
  - Bilateral: $p = 2 \cdot P(Z > |z|)$.
  - Rejeitar H₀ se $p < \alpha$.

- **Pela região crítica**:
  - Rejeitar H₀ se $|z| > z^{*}_{1 - \alpha/2}$.
  - Para $\alpha = 0{,}05$: $|z| > 1{,}96$.

## Exemplo

A glicemia média em jejum na população é conhecida: $\mu_0 = 90$ mg/dL, $\sigma = 12$ mg/dL.

Coletamos $n = 40$ pacientes com fator de risco e obtemos $\bar{x} = 95$ mg/dL.

$$
z = \frac{95 - 90}{12 / \sqrt{40}} = \frac{5}{1{,}897} \approx 2{,}635
$$

Valor-p bilateral: $p \approx 0{,}008$. Rejeitamos H₀: a média do grupo de risco é diferente.

## IC associado

O IC de $(1 - \alpha) \cdot 100\%$ correspondente:

$$
\bar{x} \pm z^{*}_{1 - \alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
$$

No exemplo: $95 \pm 1{,}96 \cdot 1{,}897 = [91{,}3;\, 98{,}7]$. Como $\mu_0 = 90$ está fora do IC, rejeitamos (mesma conclusão).

## Suposições

1. Observações **independentes**.
2. Variável aproximadamente **normal**, ou $n \geq 30$ (TLC).
3. $\sigma$ **conhecido**.

Se $\sigma$ for desconhecido, substituímos pelo desvio padrão amostral $s$ e usamos o **teste t** em vez de z.

## Teste z para proporções

Há uma versão para comparar proporções. A proporção amostral $\hat{p}$ tem distribuição aproximadamente normal para $n$ grande:

$$
z = \frac{\hat{p} - p_0}{\sqrt{p_0(1 - p_0) / n}}
$$

Aplicação típica: comparar a proporção de sucesso de um tratamento com um padrão histórico.

## Teste z para duas amostras

Generaliza para comparar duas médias quando ambos $\sigma_1$ e $\sigma_2$ são conhecidos:

$$
z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}}
$$

> Na prática, raramente conhecemos os $\sigma$s. Por isso, o teste t de duas amostras (próximos tópicos) é muito mais usado.
