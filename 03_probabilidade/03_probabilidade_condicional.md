# Probabilidade condicional

A **probabilidade condicional** mede a chance de um evento $A$ acontecer **sabendo que** outro evento $B$ já ocorreu.

## Notação

Lê-se "probabilidade de A dado B":

$$
P(A \mid B)
$$

## Fórmula

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0
$$

A intuição: **restringimos o espaço amostral** ao subconjunto em que $B$ é verdade.

## Exemplo

Considere os passageiros do Titanic:

|   | Sobreviveu | Morreu | Total |
| --- | --- | --- | --- |
| Mulheres | 233 | 81 | 314 |
| Homens | 109 | 468 | 577 |
| **Total** | 342 | 549 | 891 |

$P(\text{sobreviver}) = 342/891 \approx 0{,}38$.

$P(\text{sobreviver} \mid \text{mulher}) = 233/314 \approx 0{,}74$.

A probabilidade muda drasticamente quando condicionamos no sexo — os dois eventos **não são independentes**.

## Independência

Dois eventos são **independentes** se:

$$
P(A \mid B) = P(A)
$$

Ou equivalentemente:

$$
P(A \cap B) = P(A) \cdot P(B)
$$

Em palavras: saber que $B$ aconteceu **não muda** a probabilidade de $A$.

## Regra da multiplicação geral

A partir da definição, obtemos:

$$
P(A \cap B) = P(A) \cdot P(B \mid A) = P(B) \cdot P(A \mid B)
$$

Útil quando temos as condicionais e queremos a interseção.

## Teorema de Bayes

Combinando os dois lados da equação acima, chegamos a uma fórmula famosa:

$$
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}
$$

O teorema de Bayes permite **inverter** uma probabilidade condicional. Em outras palavras, se sei $P(B \mid A)$, posso descobrir $P(A \mid B)$ — desde que conheça $P(A)$ e $P(B)$.

### Aplicação clínica

Esse é o princípio por trás de:

- calcular o **valor preditivo positivo** a partir de sensibilidade, especificidade e prevalência;
- atualizar a probabilidade de uma doença depois de receber um resultado de exame;
- raciocínio diagnóstico em geral.

Veremos esse cálculo em detalhes em **Sensibilidade e especificidade** e **Valor preditivo**.

## A simetria que NÃO existe

Um erro muito comum:

$$
P(A \mid B) \neq P(B \mid A)
$$

Por exemplo, $P(\text{sintoma} \mid \text{doença})$ é tipicamente alto, mas $P(\text{doença} \mid \text{sintoma})$ pode ser baixíssimo (se a doença for rara). Confundir esses dois é a base do famoso **paradoxo do teste diagnóstico**.

## Regra prática

Toda vez que você lê uma probabilidade no jornal ou em um artigo, pergunte-se:

> **Condicional a quê?**

A resposta muda completamente o significado do número.
