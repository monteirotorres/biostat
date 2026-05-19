# Medidas de tendência central

Quando temos um conjunto de números, é natural perguntar: **qual é o valor "típico"?** As medidas de tendência central respondem a essa pergunta de formas diferentes.

## As três principais

| Medida | O que é | Quando usar |
| --- | --- | --- |
| **Moda** | valor mais frequente | dados categóricos, ou distribuições com picos claros |
| **Média** | soma dividida pela contagem | distribuições simétricas |
| **Mediana** | valor do meio quando os dados estão ordenados | distribuições assimétricas, com outliers |

## A grande lição

Não existe a medida "correta". Cada uma resume os dados de um jeito diferente, e a escolha depende:

- do **tipo** de dados (categórico? numérico?);
- da **forma** da distribuição (simétrica? com outliers?);
- da **pergunta** que se quer responder.

Por isso é comum reportar **mais de uma** ao descrever uma amostra.

## Um exemplo motivador

Imagine os salários (em milhares de reais) de uma empresa pequena:

$$
2{,}5 \quad 2{,}8 \quad 3{,}0 \quad 3{,}2 \quad 3{,}5 \quad 4{,}0 \quad 50
$$

- Moda: não há valor repetido.
- Mediana: 3,2 mil reais (valor do meio).
- Média: ~9,7 mil reais (puxada pelo dono que ganha 50 mil).

Qual deles representa melhor o "funcionário típico"? Claramente a **mediana**, porque a média foi distorcida por um único valor extremo.

## Quando cada uma falha

| Medida | Onde ela falha |
| --- | --- |
| Moda | quando os dados são todos diferentes, ou quando há vários picos parecidos |
| Média | quando há outliers ou a distribuição é muito assimétrica |
| Mediana | em amostras muito pequenas, é instável (mudar 1 valor pode mudar muito) |

Nos próximos tópicos veremos cada medida em detalhes, junto com algumas variações (média cortada, média ponderada, média geométrica).
