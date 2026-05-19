# Valor preditivo positivo e negativo

Sensibilidade e especificidade descrevem o **teste**. Mas o paciente está fazendo outra pergunta:

> "Meu teste deu positivo. Qual a chance de eu **realmente** ter a doença?"

Quem responde isso é o **valor preditivo**.

## Valor preditivo positivo (VPP)

$$
\text{VPP} = P(\text{doente} \mid \text{teste +}) = \frac{\text{VP}}{\text{VP} + \text{FP}}
$$

> Dos que tiveram teste positivo, quantos têm de fato a doença?

## Valor preditivo negativo (VPN)

$$
\text{VPN} = P(\text{saudável} \mid \text{teste --}) = \frac{\text{VN}}{\text{VN} + \text{FN}}
$$

> Dos que tiveram teste negativo, quantos estão de fato sem a doença?

## Detalhe crucial: VPP e VPN dependem da prevalência

Diferentemente de sensibilidade e especificidade, o VPP e o VPN **mudam** conforme a doença é mais ou menos prevalente na população.

## O famoso paradoxo do teste

Imagine um teste com:

- Sensibilidade = 99%;
- Especificidade = 99%.

Aplicado em uma doença **rara** (prevalência 0,1%) em 100.000 pessoas:

|   | Doente | Saudável |
| --- | --- | --- |
| Teste + | 99 | 999 |
| Teste − | 1 | 98.901 |
| **Total** | 100 | 99.900 |

$$
\text{VPP} = \frac{99}{99 + 999} \approx 9\%
$$

**Apenas 9%** dos testes positivos correspondem a doentes reais! Apesar de o teste ser excelente, a doença é tão rara que a maioria dos positivos são falsos positivos.

## Por que isso acontece?

Porque o número de **saudáveis** é tão maior que o de doentes que, mesmo com poucos erros percentuais nos saudáveis, o número absoluto de falsos positivos supera o de verdadeiros positivos.

## Cálculo via Bayes

A relação formal vem do **Teorema de Bayes**:

$$
\text{VPP} = \frac{\text{Sens.} \cdot \text{Prev.}}{\text{Sens.} \cdot \text{Prev.} + (1 - \text{Esp.}) \cdot (1 - \text{Prev.})}
$$

$$
\text{VPN} = \frac{\text{Esp.} \cdot (1 - \text{Prev.})}{\text{Esp.} \cdot (1 - \text{Prev.}) + (1 - \text{Sens.}) \cdot \text{Prev.}}
$$

Onde **Prev.** é a prevalência da doença.

## Como aumentar o VPP

1. **Testar populações com maior prevalência** (por isso fazemos testes de COVID em pessoas com sintomas, não em qualquer um).
2. **Aumentar a especificidade** do teste.
3. **Confirmar positivos** com um segundo teste mais específico.

## Resumo prático

| Medida | Depende da prevalência? | Pergunta |
| --- | --- | --- |
| Sensibilidade | não | "O teste pega os doentes?" |
| Especificidade | não | "O teste descarta os saudáveis?" |
| VPP | sim | "Sou doente, sabendo que dei positivo?" |
| VPN | sim | "Sou saudável, sabendo que dei negativo?" |

## Lições para o clínico

- Testes de **triagem** ganham VPP em populações de **alto risco**.
- Testes **muito específicos** são bons para **confirmação**, mesmo em doenças raras.
- A interpretação de um resultado **depende do contexto** clínico — não só do número que aparece no laudo.
