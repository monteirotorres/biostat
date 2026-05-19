# Sensibilidade e especificidade

São as duas propriedades fundamentais de um teste diagnóstico binário. Ambas são **propriedades do teste**, não do paciente — não dependem da prevalência da doença.

## Sensibilidade

Probabilidade do teste dar **positivo entre os doentes**.

$$
\text{Sensibilidade} = P(\text{teste +} \mid \text{doente}) = \frac{\text{VP}}{\text{VP} + \text{FN}}
$$

> "Dos que têm a doença, quantos o teste detecta?"

Um teste com sensibilidade de 95% detecta 95 de cada 100 pessoas doentes.

## Especificidade

Probabilidade do teste dar **negativo entre os saudáveis**.

$$
\text{Especificidade} = P(\text{teste --} \mid \text{saudável}) = \frac{\text{VN}}{\text{VN} + \text{FP}}
$$

> "Dos que não têm a doença, quantos o teste descarta corretamente?"

Um teste com especificidade de 98% dá negativo em 98 de cada 100 pessoas saudáveis.

## Visualizando

Lembrando a tabela 2x2:

|   | Doente | Saudável |
| --- | --- | --- |
| Teste + | VP | FP |
| Teste − | FN | VN |
| **Total** | **VP+FN** | **FP+VN** |

| Medida | Denominador | Frase |
| --- | --- | --- |
| Sensibilidade | Coluna dos doentes | "verdadeiros positivos entre os doentes" |
| Especificidade | Coluna dos saudáveis | "verdadeiros negativos entre os saudáveis" |

## A regra mnemônica clássica

- **SnNOut**: um teste com alta **S**ensibilidade que dá **N**egativo → afasta a doença (rule **out**).
- **SpPIn**: um teste com alta esp**P**ecificidade que dá **P**ositivo → confirma a doença (rule **in**).

## Trade-off

Em testes que usam um **valor de corte** numérico (ex.: PSA, glicemia, troponina), mover o corte muda sensibilidade e especificidade em sentidos opostos:

| Corte | Sensibilidade | Especificidade |
| --- | --- | --- |
| Mais baixo | ↑ | ↓ |
| Mais alto | ↓ | ↑ |

A **curva ROC** (próximo tópico) mostra essa relação.

## O que NÃO está incluído

Sensibilidade e especificidade **não dizem** a probabilidade de o paciente ter a doença depois de um resultado de teste. Para isso, precisamos do **valor preditivo**, que depende também da **prevalência**.

## Exemplo numérico

Aplicamos um teste a 1.000 pessoas. Sabemos (por padrão-ouro) que 100 são doentes:

|   | Doente | Saudável |
| --- | --- | --- |
| Teste + | 85 | 45 |
| Teste − | 15 | 855 |

- Sensibilidade = $85 / (85 + 15) = 0{,}85$.
- Especificidade = $855 / (855 + 45) = 0{,}95$.
