# Técnicas de amostragem

De nada adianta uma análise estatística sofisticada se a **amostra** foi mal coletada. A forma como escolhemos quem entra no estudo determina se podemos (ou não) generalizar os resultados.

> "Garbage in, garbage out." Uma amostra enviesada produz conclusões erradas, por mais correta que seja a matemática aplicada depois.

## O objetivo: representatividade

Uma boa amostra é **representativa** da população — tem, em miniatura, as mesmas características do todo. A melhor forma de conseguir isso é introduzir o **acaso** na seleção.

## Amostragem probabilística

Cada indivíduo tem uma probabilidade **conhecida e não nula** de ser escolhido. São os métodos que permitem inferência estatística válida.

### Amostragem aleatória simples

Todo indivíduo tem a **mesma** chance de ser sorteado, como em um sorteio de loteria.

- **Vantagem:** simples, sem viés.
- **Desvantagem:** pode, por azar, sub-representar subgrupos pequenos.

### Amostragem sistemática

Escolhe-se um a cada $k$ indivíduos de uma lista (ex.: a cada 10º paciente que chega).

- **Vantagem:** prática.
- **Cuidado:** se a lista tiver um padrão periódico, pode introduzir viés.

### Amostragem estratificada

A população é dividida em **estratos** homogêneos (ex.: faixas etárias, sexo) e sorteia-se dentro de cada estrato, proporcionalmente.

- **Vantagem:** garante representação de todos os subgrupos; reduz variabilidade.
- **Uso típico:** quando há subgrupos com características muito diferentes.

### Amostragem por conglomerados (clusters)

Divide-se a população em grupos (ex.: escolas, bairros), sorteiam-se alguns grupos inteiros e estuda-se todos dentro deles.

- **Vantagem:** barata logisticamente quando a população é dispersa.
- **Desvantagem:** menos precisa que a estratificada.

## Amostragem não probabilística

A seleção **não** é aleatória. Útil em estudos exploratórios, mas **não permite generalização estatística válida**.

| Tipo | Como funciona | Problema |
| --- | --- | --- |
| Por conveniência | quem está à mão (voluntários, alunos) | viés de seleção |
| Por julgamento | o pesquisador escolhe quem acha "típico" | subjetivo |
| Bola de neve | participantes indicam outros | redes enviesadas |

## O perigo dos voluntários

Um erro clássico: estudar **voluntários** para avaliar uma intervenção.

> Exemplo (da planilha do curso): um hospital quer testar um treinamento de lavagem das mãos. Se os **100 funcionários voluntários** recebem o treinamento e são comparados com os demais, o estudo é inválido — quem se voluntaria já é, em média, mais cuidadoso. O resultado fica artificialmente positivo.

A solução é **sortear** quem recebe o treinamento (aleatorização), de modo que a própria seleção não influencie o resultado.

## Variáveis de confusão (confounding)

Uma **variável de confusão** afeta o desfecho e, ao mesmo tempo, difere entre os grupos comparados — criando associações enganosas.

> Exemplo clássico (motoristas vs. cobradores de ônibus de Londres, 1961): cobradores andavam o dia todo e tinham menos doença cardíaca que os motoristas, sentados. Mas **idade**, **estado de saúde prévio** e **estresse** são confundidores possíveis. O estudo mostra **associação**, não **causa**.

Para uma variável ser confundidora, ela precisa:

1. afetar o desfecho por si só; e
2. estar distribuída de forma diferente entre os grupos.

A **aleatorização** é a principal arma contra confundidores: distribui-os igualmente entre os grupos, em média.

## Pareamento e blocos

Quando há uma fonte conhecida de variabilidade (ex.: ninhadas de ratos, onde irmãos são parecidos), podemos **parear** ou organizar em **blocos**:

> Exemplo (da planilha): para testar uma droga em filhotes de rato, **não** misture as ninhadas ao acaso entre as doses. Pegue um filhote de **cada ninhada** para **cada dose**. Assim, a variabilidade entre ninhadas não se confunde com o efeito da droga. Isso é amostragem **estratificada/em blocos** e leva a análises pareadas (mais potentes).

## Resumo

| Pergunta | Resposta |
| --- | --- |
| Quero generalizar? | use amostragem **probabilística** |
| Há subgrupos importantes? | **estratifique** |
| A população é dispersa geograficamente? | **conglomerados** |
| Há fonte conhecida de variabilidade? | **pareie / use blocos** |
| Posso usar voluntários? | só para estudos exploratórios, nunca para comparar intervenções |
