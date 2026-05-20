# Técnicas de amostragem

Exercícios sobre desenho de estudos, variáveis de confusão e pareamento.

## Exercício 1 — Motoristas e cobradores de ônibus

Um estudo de 1961 comparou a incidência de doença cardíaca entre motoristas e cobradores de ônibus de Londres. Os cobradores, que andavam o dia todo, tiveram menos doença que os motoristas, sentados.

a) Quais são as variáveis e seus níveis? b) É um estudo de correlação ou um experimento controlado? c) Por que os pesquisadores se preocuparam com idade e tempo de serviço? d) Há associação entre as variáveis? e) Que outras variáveis de confusão poderiam explicar o resultado?

<details markdown="1">
<summary>Mostrar resposta</summary>

A variável de tratamento é a quantidade de exercício, com dois níveis, muito e pouco, correspondentes a cobradores e motoristas. A variável de desfecho é a ocorrência de doença cardíaca, com os níveis sim e não.

É um estudo de correlação, não um experimento controlado, porque ninguém foi sorteado para uma profissão; as pessoas escolheram livremente seus empregos. Esse é um caso típico em que um experimento verdadeiro seria inviável.

A preocupação com idade e tempo de serviço se deve às variáveis de confusão. Uma variável de confusão precisa afetar o desfecho por si só e, ao mesmo tempo, estar distribuída de forma diferente entre os grupos. A idade satisfaz os dois critérios, pois aumenta o risco cardíaco e poderia diferir entre motoristas e cobradores. Igualar a idade dos grupos neutraliza essa explicação alternativa.

Há, sim, associação entre exercício e doença cardíaca, já que o grupo de mais exercício teve menos doença. Mas associação não prova causa. Outras confusões possíveis são o estado de saúde prévio, pois pessoas que se sentem menos aptas podem escolher ser motoristas, e o estresse do trabalho. De fato, observou-se depois que os motoristas já eram mais pesados no momento da contratação.

</details>

## Exercício 2 — Treinamento de lavagem das mãos

Um hospital quer testar um programa de lavagem das mãos. Cem funcionários voluntários recebem o treinamento e são comparados com os demais. Critique e proponha uma alternativa.

<details markdown="1">
<summary>Mostrar resposta</summary>

O estudo é inválido porque os participantes são voluntários. Justamente as pessoas mais preocupadas com higiene tendem a se voluntariar, e elas já adotam boas práticas. O resultado ficaria artificialmente positivo, e não se saberia se a melhora veio do treinamento ou do perfil de quem se inscreveu.

A correção é introduzir o acaso na formação dos grupos: sortear quem recebe o treinamento, de modo que a própria escolha dos participantes não influencie o resultado. A aleatorização distribui de forma equilibrada tanto as características conhecidas quanto as desconhecidas, e é o que torna a comparação confiável.

</details>

## Exercício 3 — Filhotes de rato e ninhadas

Filhotes de cinco ninhadas foram misturados ao acaso e divididos em quatro amostras, cada uma recebendo uma dose diferente de uma droga, para avaliar o efeito sobre a hemoglobina. A técnica de amostragem é correta?

<details markdown="1">
<summary>Mostrar resposta</summary>

A técnica tem um defeito grave. A concentração de hemoglobina é mais parecida entre filhotes da mesma ninhada do que entre ninhadas diferentes. Ao misturar os filhotes ao acaso, a variação natural entre ninhadas pode se confundir com o efeito da droga. Se, por acaso, os filhotes de uma dose vierem de uma ninhada com tendência a menos hemoglobina, poderíamos concluir erroneamente que a droga reduziu o valor.

A correção é parear: pegar um filhote de cada ninhada para cada dose, de modo que todas as ninhadas estejam representadas em todas as doses. Assim a variação entre ninhadas é controlada e o que sobra reflete o efeito da droga. Esse é um exemplo de amostragem em blocos, que leva a uma análise pareada e mais potente.

</details>
