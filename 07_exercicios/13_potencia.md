# Potência

Exercícios sobre poder estatístico e tamanho de amostra.

## Exercício 1 — Tamanho da amostra e precisão

De uma população normal de média e desvio padrão iguais a 1, tomaram-se cem amostras de cada tamanho (2, 3, 4, 6, 10 e 20) e calcularam-se as médias do desvio da média e do desvio padrão estimado, resumidas abaixo. Como variam o desvio da média, o desvio padrão estimado, o erro padrão da média e o intervalo de confiança com o tamanho da amostra?

| n | 2 | 3 | 4 | 6 | 10 | 20 |
| --- | --- | --- | --- | --- | --- | --- |
| desvio da média | 0,573 | 0,454 | 0,439 | 0,310 | 0,239 | 0,187 |
| desvio padrão estimado | 1,269 | 1,196 | 1,116 | 1,049 | 1,033 | 1,027 |

<details markdown="1">
<summary>Mostrar resposta</summary>

À medida que a amostra cresce, o desvio padrão estimado se aproxima do valor da população, com flutuações menores. O erro padrão da média segue

$$
\text{EP} = \frac{\sigma}{\sqrt{n}}
$$

Completando a tabela com o erro padrão (s/√n) e a largura do intervalo de confiança (usando o valor crítico t para cada n):

| n | 2 | 3 | 4 | 6 | 10 | 20 |
| --- | --- | --- | --- | --- | --- | --- |
| erro padrão (SEM) | 0,897 | 0,691 | 0,558 | 0,428 | 0,327 | 0,230 |
| t (5%; n−1) | 12,71 | 4,30 | 3,18 | 2,57 | 2,26 | 2,09 |
| meia-largura do IC 95% | 11,40 | 2,97 | 1,77 | 1,10 | 0,74 | 0,48 |

A precisão melhora com a raiz do tamanho da amostra, não de forma proporcional: para reduzir o erro padrão pela metade é preciso quadruplicar $n$. Repare como o IC despenca de n = 2 para n = 3 (o valor t cai de 12,71 para 4,30) e depois melhora cada vez mais devagar — os ganhos de precisão ficam progressivamente mais caros.

</details>

## Exercício 2 — Escolha do sexo da prole

Dois casais submetidos a um tratamento para escolher o sexo do bebê tiveram, cada um, dois meninos. O tratamento funciona?

<details markdown="1">
<summary>Mostrar resposta</summary>

Sob a hipótese nula de que o tratamento não funciona, vale a distribuição binomial com probabilidade 1/2 para cada nascimento. A probabilidade de quatro meninos seguidos é

$$
P = \left(\frac{1}{2}\right)^{4} = 0{,}0625
$$

pouco acima dos 5% usuais. Como esse menor valor possível de p já ultrapassa o nível de significância, o teste não tem como rejeitar a hipótese nula, mesmo no resultado mais extremo. Com apenas quatro crianças, a potência do teste é praticamente zero: o problema não é o tratamento, mas o tamanho ridículo da amostra. O teste é inconclusivo, e não uma demonstração de que o tratamento funcione.

</details>

## Exercício 3 — Potência da comparação de pressão

Os dados populacionais de pressão sistólica (estudo NHANES, exercício 4 de "Testes de dois grupos") são: homens com µ ≈ 122 mmHg, σ ≈ 17, n = 3241; mulheres com µ ≈ 119 mmHg, σ ≈ 21, n = 3427. A diferença real entre as médias é, portanto, cerca de 3 mmHg.

a) Qual a potência de um teste com os 24 dados simulados (12 por grupo)? b) Quantos dados seriam necessários para 80% de potência? c) E usando toda a amostra do estudo?

<details markdown="1">
<summary>Mostrar resposta</summary>

Com apenas 24 dados, a potência fica em torno de 7%, um valor irrisório. Isso significa que, mesmo existindo a diferença, o teste quase nunca a detectaria.

Para atingir 80% de potência, seriam necessários cerca de 568 indivíduos por grupo, dada a combinação de efeito pequeno e variabilidade grande. Usando as amostras completas, com milhares de pessoas, a potência se aproxima de 1, e a diferença é detectada com facilidade. O exemplo deixa claro que detectar efeitos pequenos exige amostras grandes.

</details>

## Exercício 4 — Trocando tamanho de amostra por tamanho de efeito

Numa situação com desvios iguais a 1 e amostras de 17 por grupo, uma diferença de 1 produz potência de 81%. Mantendo os mesmos desvios e a mesma potência, mas com 25 por grupo, a diferença detectável será maior ou menor que 1?

<details markdown="1">
<summary>Mostrar resposta</summary>

Será menor que 1. Aumentar a amostra dá mais poder ao teste, e esse poder extra pode ser convertido na capacidade de detectar diferenças menores mantendo a mesma potência. Com 25 por grupo em vez de 17, conseguimos enxergar um efeito mais sutil. Existe sempre esse balanço entre tamanho de amostra, tamanho de efeito, variabilidade e potência: fixados três deles, o quarto fica determinado.

</details>
