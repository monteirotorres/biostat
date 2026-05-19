# Probabilidade de eventos compostos

Eventos compostos envolvem **dois ou mais eventos** combinados pelas operações **e**, **ou**, **não**.

## União: $A \cup B$ (ao menos um deles)

A probabilidade de **A ou B** ocorrerem:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

> Subtraímos $P(A \cap B)$ para não contar duas vezes os casos em que ambos ocorrem.

### Exemplo

Em um dado:

- $A$ = par → $\{2, 4, 6\}$, $P(A) = 3/6$.
- $B$ = maior que 3 → $\{4, 5, 6\}$, $P(B) = 3/6$.
- $A \cap B$ = par e maior que 3 → $\{4, 6\}$, $P(A \cap B) = 2/6$.

$$
P(A \cup B) = \frac{3}{6} + \frac{3}{6} - \frac{2}{6} = \frac{4}{6}
$$

Confere com $\{2, 4, 5, 6\}$, que tem 4 elementos.

## Interseção: $A \cap B$ (ambos)

A probabilidade de **A e B** ocorrerem juntos depende se os eventos são independentes.

### Eventos independentes

Quando saber que $A$ ocorreu **não muda** a probabilidade de $B$:

$$
P(A \cap B) = P(A) \cdot P(B)
$$

Exemplo: lançar duas moedas. $P(\text{cara na 1ª} \cap \text{cara na 2ª}) = 0{,}5 \cdot 0{,}5 = 0{,}25$.

### Eventos dependentes

Usamos a probabilidade condicional (próximo tópico):

$$
P(A \cap B) = P(A) \cdot P(B \mid A)
$$

## Complemento: $A^{c}$ (não A)

$$
P(A^{c}) = 1 - P(A)
$$

Esse atalho é poderoso. Em vez de calcular "pelo menos um sucesso", calcula-se "**nenhum** sucesso" e subtrai-se de 1.

### Exemplo

Em 5 lançamentos de uma moeda, qual a probabilidade de pelo menos uma cara?

- $P(\text{nenhuma cara}) = (1/2)^5 = 1/32$.
- $P(\text{pelo menos uma cara}) = 1 - 1/32 = 31/32 \approx 0{,}97$.

## Eventos mutuamente exclusivos

Se $A$ e $B$ não podem ocorrer ao mesmo tempo:

- $P(A \cap B) = 0$.
- $P(A \cup B) = P(A) + P(B)$.

Exemplo: ao lançar um dado, "sair 2" e "sair 5" são mutuamente exclusivos — não há como sair os dois ao mesmo tempo.

## Diagrama de Venn

| Região | Probabilidade |
| --- | --- |
| Só A | $P(A) - P(A \cap B)$ |
| Só B | $P(B) - P(A \cap B)$ |
| Ambos | $P(A \cap B)$ |
| Nenhum | $1 - P(A \cup B)$ |

## Resumo

| Pergunta | Operação | Quando se aplica |
| --- | --- | --- |
| "A ou B?" | $\cup$ | sempre |
| "A e B, independentes?" | $\cap$, multiplicar | quando os eventos não interferem |
| "A e B, dependentes?" | $\cap$, com condicional | quando interferem (probabilidade condicional) |
| "Pelo menos um?" | usar complemento | em geral simplifica |
