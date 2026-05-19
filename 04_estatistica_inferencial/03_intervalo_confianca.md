# Intervalos de confiança

Um **intervalo de confiança** (IC) é um intervalo de valores plausíveis para o parâmetro populacional, calculado a partir da amostra.

## A definição correta

Um IC de 95% **não** significa que "há 95% de chance de o parâmetro estar no intervalo".

A interpretação correta é:

> Se repetíssemos o experimento muitas vezes e construíssemos um IC 95% a cada vez, **cerca de 95% desses intervalos** conteriam o parâmetro verdadeiro.

O parâmetro é um número fixo (desconhecido); quem varia é o intervalo, que muda de amostra para amostra.

## IC para a média

A fórmula geral é:

$$
\bar{x} \;\pm\; t^{*} \cdot \frac{s}{\sqrt{n}}
$$

Onde:

- $\bar{x}$: média amostral;
- $s / \sqrt{n}$: erro padrão da média;
- $t^{*}$: valor crítico da distribuição $t$ com $n - 1$ graus de liberdade, correspondente ao nível de confiança escolhido.

> Quando o desvio padrão $\sigma$ da população é **conhecido**, usamos $z^{*}$ da normal padrão em vez de $t^{*}$. Mas, em pesquisa real, $\sigma$ quase sempre é desconhecido.

## Valores críticos comuns

Para o teste bilateral:

| Nível | $z^{*}$ (normal) |
| --- | --- |
| 90% | 1,645 |
| 95% | 1,960 |
| 99% | 2,576 |

Para o $t$, o valor muda com os graus de liberdade — mas se aproxima de $z^{*}$ quando $n$ é grande.

## Exemplo

Pesos (em gramas) de 25 ratos: $\bar{x} = 240{,}2$, $s = 18$.

Erro padrão = $18 / \sqrt{25} = 3{,}6$.

Para 95% de confiança, $t^{*}_{24} \approx 2{,}064$.

$$
\text{IC 95\%} = 240{,}2 \pm 2{,}064 \cdot 3{,}6 \approx [232{,}8;\; 247{,}6] \text{ g}
$$

## O que controla a largura do IC

| Fator | Efeito na largura |
| --- | --- |
| Aumentar $n$ | **reduz** |
| Aumentar $s$ | **aumenta** |
| Aumentar o nível de confiança | **aumenta** |

> Para reduzir a margem de erro pela metade, é preciso **quadruplicar** o tamanho da amostra.

## IC para uma proporção

Para proporções (eleições, ensaios clínicos com desfechos binários):

$$
\hat{p} \;\pm\; z^{*} \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}
$$

> Essa aproximação só vale para $n$ grande e $\hat{p}$ não muito próximo de 0 ou 1. Em caso contrário, usa-se métodos alternativos (Wilson, Clopper–Pearson).

## IC para diferença entre duas médias

$$
(\bar{x}_1 - \bar{x}_2) \;\pm\; t^{*} \cdot \sqrt{\frac{s_1^{2}}{n_1} + \frac{s_2^{2}}{n_2}}
$$

Se o IC para a diferença **não inclui zero**, há evidência de que as médias são diferentes (equivalente a um teste t com $p < \alpha$).

## A relação com testes de hipóteses

Existe uma equivalência direta:

| Resultado do teste | IC do parâmetro |
| --- | --- |
| Rejeita $H_0$: $\mu = \mu_0$ ao nível $\alpha = 0{,}05$ | IC 95% **não contém** $\mu_0$ |
| Não rejeita $H_0$ | IC 95% **contém** $\mu_0$ |

Por isso, em artigos modernos, é cada vez mais comum reportar o **IC junto com o valor-p** — ou até em vez dele. O IC traz a mesma informação do teste, com a vantagem de mostrar **a magnitude** do efeito.

## Cuidados importantes

1. **Interpretação frequentista**: o intervalo cobre o parâmetro em 95% das replicações.
2. **Não confundir** com intervalo de **predição**, que é mais largo e prediz observações individuais.
3. **Dados extremos** podem afetar o IC — verifique a distribuição.
4. **IC muito largo** indica que a amostra é pequena demais para uma estimativa precisa.
