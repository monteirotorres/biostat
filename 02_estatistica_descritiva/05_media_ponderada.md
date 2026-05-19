# Média ponderada

Cada valor recebe um **peso** diferente, refletindo sua importância relativa.

## Fórmula

$$
\bar{x}_w = \frac{\sum_{i=1}^{n} w_i \cdot x_i}{\sum_{i=1}^{n} w_i}
$$

Onde:

- $x_i$ são os valores;
- $w_i$ são os pesos (todos positivos).

> Quando todos os pesos são iguais, a média ponderada vira a **média aritmética comum**.

## Exemplo clássico — nota final

Uma disciplina tem três avaliações:

| Avaliação | Nota | Peso |
| --- | --- | --- |
| P1 | 7,0 | 2 |
| P2 | 6,0 | 3 |
| Trabalho | 9,0 | 1 |
| Prova final | 8,0 | 4 |

$$
\bar{x}_w = \frac{7 \cdot 2 + 6 \cdot 3 + 9 \cdot 1 + 8 \cdot 4}{2 + 3 + 1 + 4} = \frac{14 + 18 + 9 + 32}{10} = \frac{73}{10} = 7{,}3
$$

A média aritmética simples daria 7,5 — mas como a prova final pesa mais e a P2 (pior nota) também tem peso alto, a média ponderada fica em 7,3.

## Em biologia e medicina

A média ponderada aparece em:

- **Meta-análises**: estudos com amostras maiores recebem peso maior, porque suas estimativas são mais confiáveis.
- **Cálculo de IDH ou IDS**: cada indicador entra com peso definido pela metodologia.
- **Sistemas de pontuação clínica**: cada sinal/sintoma tem peso clínico diferente.

## Pesos normalizados

Se preferimos pesos que somam 1 (probabilidades, frações), a fórmula vira:

$$
\bar{x}_w = \sum_{i=1}^{n} w_i \cdot x_i \quad \text{com} \quad \sum_{i=1}^{n} w_i = 1
$$

Esse formato aparece muito em **expectativa matemática** — a média ponderada nada mais é do que o valor esperado quando os pesos representam probabilidades.

## Detalhe importante

Os pesos representam **importância relativa**, não probabilidades de erro ou qualidade absoluta. Se eu der peso 10 a um valor mal medido e peso 1 ao bem medido, vou puxar a média para o errado. Os pesos precisam ser escolhidos **antes** de olhar os dados, com base em um critério justificável.
