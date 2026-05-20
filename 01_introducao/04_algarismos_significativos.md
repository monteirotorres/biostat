# Algarismos significativos

São os dígitos de uma medida que carregam **informação real** — refletem a precisão do instrumento usado.

## A ideia

Escrever "a massa é 4,2371928 g" quando a balança só mede até décimos de grama é **mentir** sobre a precisão. Os dígitos sobrando não vieram da medida — são lixo.

## Regras práticas

1. **Todos os dígitos diferentes de zero são significativos.**
   - `1234` tem 4 significativos.

2. **Zeros entre dígitos significativos contam.**
   - `1002` tem 4 significativos.

3. **Zeros à esquerda NÃO contam.** Servem só de preenchimento.
   - `0,0034` tem 2 significativos (o 3 e o 4).

4. **Zeros à direita após a vírgula contam.**
   - `1,200` tem 4 significativos.

5. **Zeros à direita sem vírgula são ambíguos.** Use notação científica para deixar claro.
   - `1500` pode ter 2, 3 ou 4 significativos.
   - `1,5 \times 10^3` tem 2.
   - `1,50 \times 10^3` tem 3.

## Em operações

| Operação | Regra |
| --- | --- |
| Soma/subtração | O resultado tem tantas **casas decimais** quanto o termo com **menos** casas decimais |
| Multiplicação/divisão | O resultado tem tantos **algarismos significativos** quanto o fator com **menos** significativos |

### Exemplos

$$
12{,}11 + 8{,}3 = 20{,}4 \quad (\text{e não } 20{,}41)
$$

$$
3{,}24 \times 5{,}6 = 18 \quad (\text{e não } 18{,}144)
$$

## Em bioestatística

Quando reportamos resultados:

- Médias e desvios padrão: normalmente **1 a 2 casas além do dado bruto** já é o limite razoável.
- Valor-p: até 3 casas (`p = 0,032`), ou notação científica para muito pequenos (`p < 0,001`).
- Porcentagens: 1 casa decimal costuma ser suficiente (`32,5%`).
