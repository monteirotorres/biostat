# Precisão e acurácia

São conceitos parecidos no dia-a-dia, mas significam coisas bem distintas em estatística e ciência.

## Acurácia

**Acurácia** mede quão perto as medidas estão do **valor verdadeiro** — ou seja, o quanto elas estão **certas em média**.

## Precisão

**Precisão** mede quão **consistentes** as medidas são entre si — ou seja, o quão **próximas umas das outras** estão. Pouco importa se estão certas ou erradas em relação ao valor verdadeiro, basta que sejam parecidas.

## A clássica analogia do alvo

Imagine quatro atiradores disparando contra um alvo. O centro do alvo é o "valor verdadeiro":

| Cenário | Acurado | Preciso |
| --- | --- | --- |
| Tiros agrupados no centro | sim | sim |
| Tiros agrupados, mas fora do centro | não | sim |
| Tiros espalhados, mas centrados no alvo | sim | não |
| Tiros espalhados e longe do centro | não | não |

## Aplicação prática

- Um instrumento **calibrado** é acurado.
- Um instrumento **de boa qualidade** é preciso.
- O ideal é ter os dois.

| Problema | Solução |
| --- | --- |
| Falta de acurácia (viés) | calibrar o equipamento, controle interno |
| Falta de precisão (ruído) | tomar mais medidas e usar a média; melhorar o método |

## Em termos estatísticos

Se $\mu$ é o valor verdadeiro e fazemos várias medidas $x_1, x_2, \ldots, x_n$:

- **Acurácia** está relacionada ao **viés**: $\bar{x} - \mu$.
- **Precisão** está relacionada à **variância**: $\text{Var}(x)$.

> Repare: a média de muitas medidas precisas mas inacuradas continua inacurada. Aumentar o número de medições resolve a precisão, mas não corrige um viés sistemático.
