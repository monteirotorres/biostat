# Lógica da inferência e intervalo de confiança

Exercícios sobre o raciocínio inferencial, significância e estimação por intervalo.

## Exercício 1 — Descritiva ou inferencial?

Um professor pergunta à própria turma a opinião sobre a pena de morte e compara as proporções entre homens e mulheres, concluindo que os homens da turma têm maior aceitação. Esse é um exemplo de estatística descritiva ou inferencial?

<details markdown="1">
<summary>Mostrar resposta</summary>

É estatística descritiva. O professor apenas resumiu os dados da própria turma, sem nenhuma tentativa de generalizar o resultado para um grupo maior. A conclusão vale exclusivamente para aquele conjunto de alunos. Seria inferencial se ele usasse a turma como amostra para tirar conclusões sobre estudantes em geral, e aí precisaria lidar com a incerteza da generalização.

</details>

## Exercício 2 — Significância e relevância

Qual a diferença entre uma diferença significativa e uma diferença relevante?

<details markdown="1">
<summary>Mostrar resposta</summary>

Uma diferença significativa é aquela grande o suficiente para ser detectada pelo desenho do experimento, o que depende do tamanho da amostra, do pareamento e da variabilidade. Com um experimento muito potente, é possível detectar diferenças minúsculas.

Uma diferença relevante é aquela grande o suficiente para ter utilidade prática. As duas coisas não andam necessariamente juntas. Existe, por exemplo, um estudo com milhares de crianças que detectou uma diferença significativa de QI entre primogênitos e filhos seguintes, com o primeiro ligeiramente acima. A diferença é real e significativa, mas tão pequena diante da variabilidade natural que não tem qualquer utilidade prática para os pais. O mesmo raciocínio vale para um antitérmico que reduz a febre em 0,1 grau: pode ser detectável, mas é clinicamente inútil. Por isso um resultado deve sempre ser acompanhado da discussão sobre o tamanho do efeito.

</details>

## Exercício 3 — Intervalo de confiança

A partir da amostra 5, 3, 4, 2, 3, 4, 2, 3, 4, 5, extraída de uma população normal, encontre o intervalo de confiança de 95% para a média e interprete-o.

<details markdown="1">
<summary>Mostrar resposta</summary>

A média da amostra é 3,5 e o desvio padrão amostral é cerca de 1,08. Como o desvio populacional é desconhecido e a amostra é pequena, usamos a distribuição t com nove graus de liberdade, cujo valor crítico para 95% é 2,262. O intervalo é a média mais ou menos o valor crítico vezes o erro padrão:

$$
\bar{x} \pm t^{*}\,\frac{s}{\sqrt{n}} = 3{,}5 \pm 2{,}262 \times \frac{1{,}08}{\sqrt{10}} = 3{,}5 \pm 0{,}77 \;\Rightarrow\; [2{,}7;\; 4{,}3]
$$

A interpretação correta é que, se repetíssemos o experimento muitas vezes e construíssemos um intervalo a cada vez, cerca de 95% desses intervalos conteriam a verdadeira média da população. Não se deve dizer que há 95% de probabilidade de a média estar neste intervalo específico, pois a média é um número fixo; quem varia de amostra para amostra é o intervalo.

</details>

## Exercício 4 — Moeda viciada pela lógica binomial

Para testar se uma moeda é viciada, jogamos vinte vezes e contamos as caras. Usando a distribuição binomial e a lógica inferencial, quais proporções levam a concluir que a moeda é viciada, com 95% de confiança?

<details markdown="1">
<summary>Mostrar resposta</summary>

Sob a hipótese de moeda honesta, o número de caras em vinte lançamentos segue uma binomial com p igual a 0,5, simétrica em torno de dez. Para um teste bilateral com 5% de significância, somamos as probabilidades das caudas até atingir no máximo esse valor.

As caudas formadas por cinco caras ou menos, de um lado, e quinze caras ou mais, do outro, somam

$$
P(X \le 5) + P(X \ge 15) \approx 0{,}021 + 0{,}021 = 0{,}041
$$

abaixo dos 5%. Então esses são os resultados que levam a rejeitar a hipótese de moeda honesta. Se exigíssemos 99% de confiança, os valores cinco e quinze deixariam de ser suficientes, e só resultados ainda mais extremos levariam à rejeição. Esse mesmo problema reaparece, de outra forma, no teste do qui-quadrado.

</details>
