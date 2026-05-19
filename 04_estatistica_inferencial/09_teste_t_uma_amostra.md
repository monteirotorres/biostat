# Teste t para uma amostra

Compara a média de uma amostra com um **valor de referência**, quando o desvio padrão da população **não é conhecido** (caso quase universal em pesquisa).

## Hipóteses

$$
H_0: \mu = \mu_0
$$

$$
H_1: \mu \neq \mu_0 \quad (\text{bilateral})
$$

## Estatística do teste

$$
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
$$

A diferença para o teste z é que **usamos o desvio padrão amostral** $s$ em vez do populacional $\sigma$.

Sob H₀, $t$ segue uma **distribuição t de Student** com $n - 1$ graus de liberdade.

## A distribuição t

A distribuição t é como uma normal, mas com **caudas mais pesadas** para amostras pequenas. Isso reflete a incerteza extra de estimar $\sigma$ a partir dos próprios dados.

| Graus de liberdade | Cauda |
| --- | --- |
| Pequenos ($n \approx 5$) | Bem mais pesada que a normal |
| Médios ($n \approx 30$) | Já bem parecida com a normal |
| Grandes ($n > 100$) | Praticamente normal |

Para $n \to \infty$, a t **converge para a normal padrão**.

## Decisão

- **Valor-p**: $p = 2 \cdot P(T > |t_{\text{obs}}|)$ com $n - 1$ gl.
- **Região crítica**: rejeitar H₀ se $|t| > t^{*}_{n-1,\,1-\alpha/2}$.

## Exemplo

Suspeita-se que um determinado grupo de pacientes tem colesterol maior que a média geral ($\mu_0 = 200$ mg/dL).

Amostra de $n = 25$ pacientes: $\bar{x} = 215$, $s = 30$.

$$
t = \frac{215 - 200}{30 / \sqrt{25}} = \frac{15}{6} = 2{,}5
$$

Para 24 gl, valor-p bilateral $\approx 0{,}020$. **Rejeitamos H₀**.

## IC associado

$$
\bar{x} \pm t^{*}_{n-1,\,1-\alpha/2} \cdot \frac{s}{\sqrt{n}}
$$

No exemplo, com $t^{*}_{24} \approx 2{,}064$:

$$
215 \pm 2{,}064 \cdot 6 \approx [202{,}6;\; 227{,}4]
$$

Como $\mu_0 = 200$ está fora do IC, rejeitamos (mesma conclusão).

## Suposições

1. Observações **independentes**.
2. Variável **aproximadamente normal**, ou $n \geq 30$ (TLC).
3. Variável quantitativa.

## Robustez

O teste t é **bastante robusto** a desvios moderados da normalidade — especialmente com $n \geq 30$. Para amostras muito pequenas e dados muito enviesados, prefira o equivalente não paramétrico (teste de Wilcoxon do sinal).

## Teste unilateral

Se a direção do efeito é pré-especificada:

- $H_1: \mu > \mu_0$ (direita): $p = P(T > t_{\text{obs}})$.
- $H_1: \mu < \mu_0$ (esquerda): $p = P(T < t_{\text{obs}})$.

> Atenção: a escolha da direção deve ser **antes** de ver os dados.

## Quando NÃO usar

- Dados muito enviesados em amostra pequena → use **Wilcoxon do sinal**.
- Dados categóricos → use teste qui-quadrado ou binomial.
- Várias medidas no mesmo indivíduo → use **teste t pareado** ou modelos mistos.
