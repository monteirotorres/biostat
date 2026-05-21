# Testes de dois grupos

Exercícios sobre teste t e alternativas não paramétricas.

## Exercício 1 — Anatomia de um teste

Descreva os elementos que definem um teste estatístico entre dois grupos.

<details markdown="1">
<summary>Mostrar resposta</summary>

Um teste se define pela combinação das hipóteses com o desenho do experimento. Nas hipóteses, decidimos se o teste é paramétrico, o que supõe que a variável seja aproximadamente normal, ou não paramétrico, quando essa suposição não se sustenta. Decidimos também a lateralidade: se há razão prévia para esperar a diferença em uma direção específica, o teste é unilateral; caso contrário, é bilateral.

No desenho, verificamos se os dados são pareados, ou seja, se há uma correspondência natural entre os elementos dos dois grupos, e escolhemos o nível de significância de acordo com a necessidade prática. Com tudo isso definido, calculamos o valor-p e o comparamos com o nível de significância: se for menor, a diferença é significativa; se for maior, não há evidência suficiente de diferença.

</details>

## Exercício 2 — Besouros em duas florestas

Comparam-se contagens de besouros em armadilhas de duas florestas. Amostra 1: 8, 12, 15, 21, 25, 44, 44, 60. Amostra 2: 2, 4, 5, 9, 12, 17, 19. Qual teste usar e como interpretar um valor-p de 2,8%?

<details markdown="1">
<summary>Mostrar resposta</summary>

Contagens baixas quase sempre produzem distribuições assimétricas, o que afasta o teste paramétrico. Não havia conhecimento prévio sobre qual floresta teria mais besouros, então o teste é bilateral, e não há nenhum pareamento entre as armadilhas. A escolha recai sobre o teste de Mann-Whitney, não paramétrico, bilateral e não pareado.

Com o valor-p de 2,8%, abaixo dos 5% usuais, concluímos que a diferença é significativa: a floresta da Amostra 1 tem mais besouros. A interpretação do valor-p num teste não paramétrico tem uma sutileza. Se colocarmos todos os valores numa única fila ordenada, os da Amostra 2 se concentram à esquerda e os da Amostra 1 à direita. O teste mede o grau dessa separação por postos, e o valor-p é a probabilidade de observar uma separação tão grande ou maior apenas por acaso, sob a hipótese nula. Aqui falamos em medianas, não em médias.

</details>

## Exercício 3 — Halotano contra Morfina

Comparam-se dois anestésicos quanto à pressão arterial média no início da cirurgia. Halotano: média 66,9, desvio 12,2, n igual a 61. Morfina: média 73,2, desvio 14,4, n igual a 61.

a) As diferenças são consistentes com a hipótese de mesmo efeito? b) Se houver diferença, estime-a. c) A mortalidade, 8 de 61 contra 10 de 61, difere?

<details markdown="1">
<summary>Mostrar resposta</summary>

Com amostras grandes de uma variável contínua, sem pareamento e sem direção prévia, o teste indicado é o t não pareado e bilateral. A estatística combina a diferença das médias com o erro padrão da diferença:

$$
t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}} = \frac{66{,}9 - 73{,}2}{\sqrt{\dfrac{12{,}2^2}{61} + \dfrac{14{,}4^2}{61}}} \approx -2{,}61
$$

Com cerca de 117 graus de liberdade, isso dá um valor-p de aproximadamente 0,010, então a diferença na pressão é significativa. A verdadeira diferença é estimada pelo intervalo de confiança da diferença entre as médias, aproximadamente de −11 a −1,5 mmHg. Embora significativa, a diferença pode ser pequena demais para ser clinicamente relevante na extremidade inferior do intervalo.

A comparação de mortalidade envolve proporções, não médias, e por isso usa uma tabela de contingência com o teste do qui-quadrado. As proporções 13,1% e 16,4% não diferem significativamente, ou seja, não há evidência de que um anestésico cause mais fatalidades que o outro.

</details>

## Exercício 4 — Pressão de homens e mulheres

Procurando dados de pressão sistólica de homens e mulheres no Wolfram\|Alpha (estudo NHANES 2006, ponderado para a demografia dos EUA), encontram-se as distribuições populacionais abaixo. A tabela traz 12 valores por sexo, gerados aleatoriamente de acordo com essas distribuições. Use um teste t para verificar se há diferença significativa entre os dois conjuntos.

| Sexo | Intervalo ±1σ | Média (µ) | σ | n (estudo) |
| --- | --- | --- | --- | --- |
| Masculino | 105 a 139 mmHg | ≈ 122 | ≈ 17 | 3241 |
| Feminino | 98 a 140 mmHg | ≈ 119 | ≈ 21 | 3427 |

| Homens | Mulheres |
| --- | --- |
| 72 | 57 |
| 124 | 143 |
| 138 | 112 |
| 84 | 133 |
| 123 | 140 |
| 139 | 156 |
| 128 | 132 |
| 128 | 121 |
| 115 | 140 |
| 107 | 175 |
| 105 | 98 |
| 141 | 142 |

<details markdown="1">
<summary>Mostrar resposta</summary>

A diferença real entre as médias é de apenas cerca de 3 mmHg, enquanto os desvios padrão são grandes, da ordem de 17 a 21 mmHg. Com apenas doze valores por grupo, o teste tem poder muito baixo para detectar um efeito tão pequeno diante de tanta variabilidade.

O resultado provável é não rejeitar a hipótese nula, não porque a diferença não exista, mas porque a amostra é pequena demais. Esse exercício prepara o terreno para a discussão de potência: a ausência de significância não prova ausência de efeito.

</details>

## Exercício 5 — Teste t pela tabela e pelo software

Compare as amostras A1 e A2 abaixo, primeiro pela tabela t e depois com software dedicado.

| A1 | A2 |
| --- | --- |
| 0 | 3 |
| 1 | 4 |
| 2 | 5 |
| 3 | 6 |
| 4 | 7 |
| 5 | 8 |
| 6 | 9 |
| 7 | 10 |
| 8 | 11 |
| 9 | 12 |

As duas têm dez valores; A1 tem média 4,5 e A2 tem média 7,5, ambas com desvio 3,03.

<details markdown="1">
<summary>Mostrar resposta</summary>

A estatística t é a diferença das médias dividida pelo erro padrão da diferença. Com desvios iguais ($s = 3{,}03$) e dez valores em cada grupo:

$$
t = \frac{4{,}5 - 7{,}5}{3{,}03\sqrt{\frac{1}{10} + \frac{1}{10}}} = \frac{-3}{3{,}03 \times 0{,}447} \approx -2{,}22 \qquad \text{gl} = 18
$$

O valor crítico da tabela t para 5% bilateral com dezoito graus de liberdade é 2,10. Como $|{-2{,}22}| > 2{,}10$, a diferença é significativa. Chegar ao mesmo resultado pela tabela e pelo software ajuda a entender o que o programa calcula por baixo dos panos.

</details>

## Exercício 6 — Hemoglobina antes e depois

Mede-se a hemoglobina de oito indivíduos antes e depois de uma droga, e quer-se avaliar sua eficácia. Que teste usar?

<details markdown="1">
<summary>Mostrar resposta</summary>

Como cada indivíduo é medido duas vezes, antes e depois, os dados são naturalmente pareados. O teste indicado é o t pareado, aplicado às diferenças individuais entre depois e antes.

Pareando, eliminamos a variabilidade entre indivíduos e ganhamos poder para detectar a mudança causada pela droga. Se a média das diferenças for grande o bastante em relação à sua dispersão, o valor-p fica abaixo do nível de significância e concluímos que a droga altera a hemoglobina. Caso as diferenças não pareçam normais e a amostra seja pequena, a alternativa é o teste de Wilcoxon pareado.

</details>
