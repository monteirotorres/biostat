# Distribuição amostral

Exercícios sobre somas e médias de variáveis aleatórias.

## Exercício 1 — Caixa de produtos

Um produto pesa em média 10 g, com desvio de 2 g, e é embalado em caixas de cinquenta unidades. As caixas vazias pesam em média 500 g, com desvio de 25 g. Supondo independência e distribuições normais, qual a probabilidade de uma caixa cheia pesar mais de 1050 g?

<details markdown="1">
<summary>Mostrar resposta</summary>

O peso da caixa cheia é a soma do peso da caixa vazia com os pesos dos cinquenta produtos. A média da soma é

$$
\mu = 500 + 50 \times 10 = 1000 \text{ g}
$$

A variância da soma é a soma das variâncias, porque as variáveis são independentes:

$$
\sigma^2 = 25^2 + 50 \times 2^2 = 625 + 200 = 825 \quad\Rightarrow\quad \sigma = \sqrt{825} \approx 28{,}7 \text{ g}
$$

Pesar mais de 1050 g corresponde a

$$
z = \frac{1050 - 1000}{28{,}7} \approx 1{,}74 \quad\Rightarrow\quad P(\text{peso} > 1050) = 1 - \Phi(1{,}74) \approx 0{,}041
$$

Note que somamos as variâncias, e não os desvios padrão; por isso o desvio da caixa cheia, 28,7 g, é bem menor que a soma ingênua dos desvios.

</details>
