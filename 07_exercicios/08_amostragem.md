# Distribuição amostral

Exercícios sobre somas e médias de variáveis aleatórias.

## Exercício 1 — Caixa de produtos

Um produto pesa em média 10 g, com desvio de 2 g, e é embalado em caixas de cinquenta unidades. As caixas vazias pesam em média 500 g, com desvio de 25 g. Supondo independência e distribuições normais, qual a probabilidade de uma caixa cheia pesar mais de 1050 g?

<details markdown="1">
<summary>Mostrar resposta</summary>

O peso da caixa cheia é a soma do peso da caixa vazia com os pesos dos cinquenta produtos. A média da soma é 500 + 50 × 10 = 1000 g.

A variância da soma é a soma das variâncias, porque as variáveis são independentes. A variância da caixa vazia é 25² = 625, e a dos cinquenta produtos é 50 × 2² = 200, totalizando 825. O desvio padrão da soma é a raiz desse valor, cerca de 28,7 g.

Pesar mais de 1050 g corresponde a um afastamento de cerca de 1,74 desvios acima da média, o que dá uma probabilidade de aproximadamente 0,041. Note que somamos as variâncias e não os desvios padrão; é por isso que o desvio da caixa cheia, 28,7 g, é bem menor que a soma ingênua dos desvios.

</details>
