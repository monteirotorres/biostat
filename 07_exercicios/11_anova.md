# ANOVA

Exercícios sobre comparação de três ou mais grupos.

## Exercício 1 — Drogas A, B e placebo

Avalia-se a contagem de linfócitos sob duas drogas e um placebo, usando sete ninhadas de camundongos, com animais da mesma ninhada distribuídos entre os três tratamentos. Os pesquisadores querem saber se as drogas diferem do placebo. Que análise usar?

<details markdown="1">
<summary>Mostrar resposta</summary>

O fato de os animais virem da mesma ninhada cria um pareamento natural, porque irmãos respondem de forma mais parecida entre si. Isso indica uma ANOVA de medidas repetidas, que controla a variabilidade entre ninhadas, em vez da ANOVA comum.

A pergunta "as drogas diferem do placebo" pede comparações de cada tratamento contra um grupo de referência, e não de todos contra todos. O pós-teste apropriado é o de Dunnett, que compara cada grupo com o controle. Na prática, o teste global retorna um valor-p de cerca de 0,002, e o pós-teste de Dunnett encontra diferença significativa apenas entre a droga A e o placebo.

</details>

## Exercício 2 — Concurso na UFRJ

Seis candidatos foram avaliados por cinco membros de uma banca. Pergunta-se se a banca consegue de fato diferenciar os candidatos e se há empates estatísticos que tornariam a classificação um sorteio.

<details markdown="1">
<summary>Mostrar resposta</summary>

Os avaliadores diferem em rigor, então cada candidato é avaliado pelos mesmos cinco juízes, o que configura um delineamento de medidas repetidas. A pergunta sobre diferenciar candidatos se traduz em comparar a variabilidade entre candidatos com a variabilidade entre avaliadores.

A variabilidade entre os candidatos supera a variabilidade entre os avaliadores, o que indica que a banca de fato consegue distinguir os candidatos. Ao mesmo tempo, candidatos com médias muito próximas ficam estatisticamente empatados, e nesses casos diferentes bancas poderiam produzir classificações distintas. O fator sorte, portanto, tem um papel real quando as notas são próximas, embora o processo como um todo tenha poder de resolução adequado para separar candidatos de níveis distintos.

</details>
