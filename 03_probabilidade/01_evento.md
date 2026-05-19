# Evento — definição

A probabilidade é a linguagem matemática para falar de **incerteza**. Antes de calcular probabilidades, precisamos definir alguns termos.

## Experimento aleatório

É qualquer processo cujo resultado **não pode ser previsto com certeza**, mas cujos resultados possíveis são conhecidos.

Exemplos:

- Lançar uma moeda.
- Sortear uma carta de um baralho.
- Aplicar um teste diagnóstico em um paciente.
- Medir a glicemia no sangue após uma refeição.

## Espaço amostral ($\Omega$)

É o **conjunto de todos os resultados possíveis** do experimento.

| Experimento | $\Omega$ |
| --- | --- |
| Lançar uma moeda | $\{\text{cara}, \text{coroa}\}$ |
| Lançar um dado | $\{1, 2, 3, 4, 5, 6\}$ |
| Resultado de um teste de COVID | $\{\text{positivo}, \text{negativo}\}$ |
| Medir a temperatura corporal | qualquer valor entre 34 °C e 42 °C |

## Evento

Um **evento** é um **subconjunto** do espaço amostral — um ou mais resultados que nos interessam.

| Experimento | Evento de interesse |
| --- | --- |
| Lançar um dado | "sair número par" → $A = \{2, 4, 6\}$ |
| Sortear uma carta | "sair um ás" → $A = \{\text{A}\heartsuit, \text{A}\diamondsuit, \text{A}\clubsuit, \text{A}\spadesuit\}$ |
| Diagnóstico | "ter a doença" |

## Probabilidade

A probabilidade de um evento $A$, escrita $P(A)$, é um número entre 0 e 1:

$$
0 \leq P(A) \leq 1
$$

- $P(A) = 0$: evento **impossível**.
- $P(A) = 1$: evento **certo**.
- $P(A) = 0{,}5$: 50% de chance.

## Como calcular?

### Definição clássica (resultados equiprováveis)

Quando todos os resultados de $\Omega$ têm a mesma chance:

$$
P(A) = \frac{|A|}{|\Omega|} = \frac{\text{nº de resultados favoráveis}}{\text{nº total de resultados}}
$$

Exemplo: $P(\text{par em um dado}) = 3/6 = 0{,}5$.

### Definição frequentista

Em situações em que não temos simetria, definimos $P(A)$ como a **frequência relativa** com que $A$ ocorre em muitas repetições do experimento:

$$
P(A) = \lim_{n \to \infty} \frac{n_A}{n}
$$

Exemplo: em 10.000 pacientes diabéticos, 320 tiveram complicações cardiovasculares em 5 anos. $P(\text{complicação}) \approx 320/10\,000 = 0{,}032$.

## Propriedades fundamentais

1. **Evento complementar** $A^{c}$ (não $A$):

$$
P(A^{c}) = 1 - P(A)
$$

2. **União** (ao menos um deles ocorre):

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

3. **Eventos mutuamente exclusivos** (não podem ocorrer juntos): $P(A \cap B) = 0$, logo

$$
P(A \cup B) = P(A) + P(B)
$$

4. **Eventos independentes** (a ocorrência de um não afeta o outro):

$$
P(A \cap B) = P(A) \cdot P(B)
$$

Voltaremos a essas regras nos próximos tópicos.
