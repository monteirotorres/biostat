# Tabelas de contingência

Exercícios sobre associação entre variáveis categóricas.

## Exercício 1 — Mortalidade entre anestésicos

Comparam-se as mortes em dois grupos: 8 de 61 pacientes anestesiados com Halotano e 10 de 61 com Morfina. As proporções diferem significativamente?

<details markdown="1">
<summary>Mostrar resposta</summary>

Os dados formam uma tabela dois por dois, com mortos e sobreviventes em cada anestésico. A análise apropriada é o teste do qui-quadrado de independência, ou o teste exato de Fisher quando alguma contagem é pequena.

As proporções de 13,1% e 16,4% são próximas e, com apenas sessenta e um pacientes por grupo, a diferença observada está bem dentro do que o acaso produziria. Não se rejeita a hipótese nula, ou seja, não há evidência de que os dois anestésicos resultem em taxas de fatalidade diferentes.

</details>

## Exercício 2 — Medicamento e efeito colateral

Como testar se há associação entre usar um medicamento e apresentar um efeito colateral, a partir de uma tabela com presença ou ausência do efeito nos grupos que usaram e não usaram?

<details markdown="1">
<summary>Mostrar resposta</summary>

A tabela cruza duas variáveis categóricas, uso do medicamento e ocorrência do efeito, formando quatro caselas. O teste do qui-quadrado de independência compara as contagens observadas com as que seriam esperadas caso as duas variáveis fossem independentes.

Se o valor-p resultante for suficientemente baixo, rejeita-se a hipótese de independência e conclui-se que existe associação entre o medicamento e o efeito colateral. Vale lembrar que associação não é o mesmo que causa, e que convém acompanhar o resultado de uma medida de tamanho de efeito, como a razão de chances, para avaliar a força da associação.

</details>
