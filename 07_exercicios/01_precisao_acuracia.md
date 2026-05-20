# Precisão, acurácia e algarismos significativos

Exercícios sobre medidas, erros e a representação correta de números. Tente resolver a partir do enunciado antes de abrir a resposta.

## Exercício 1 — Calibração de pipeta

Um certificado de conformidade de uma pipeta traz duas séries de pesagens de água. Para o volume nominal de 200 µL foram registrados 198,75 · 198,83 · 198,78 · 198,87 (mg); para 1000 µL, 996,41 · 996,34 · 996,48 · 996,44 (mg).

a) A exatidão está dentro da tolerância (±3,00 µL para 200 µL e ±8,00 µL para 1000 µL)?

b) A precisão está dentro da especificação (desvio padrão < 0,60 µL para 200 µL e < 1,50 µL para 1000 µL)?

c) Costuma-se dizer que "para obter um erro menor, manipule quantidades maiores". No entanto, o desvio padrão de 1000 µL é maior que o de 200 µL. Como conciliar as duas afirmações?

<details markdown="1">
<summary>Mostrar resposta</summary>

A exatidão é a diferença entre a média das pesagens e o valor nominal. Para a série de 200 µL,

$$
\bar{x}_{200} = \frac{198{,}75 + 198{,}83 + 198{,}78 + 198{,}87}{4} = 198{,}808 \text{ mg}
$$

Após a conversão de massa para volume (que usa o fator Z, próximo de 1), isso corresponde a um desvio de cerca de $-0{,}5$ µL em relação a 200 µL. Para a série de 1000 µL a média é $996{,}418$ mg, um desvio de cerca de $-0{,}3$ µL. Ambos estão muito abaixo das tolerâncias de ±3,00 e ±8,00 µL, então a exatidão está aprovada.

A precisão é o desvio padrão de cada série. Tomando a série de 200 µL,

$$
s_{200} = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}} \approx 0{,}053 \text{ µL}
$$

e o desvio da série de 1000 µL é cerca de $0{,}059$ µL. Os dois ficam muito abaixo dos limites de 0,60 e 1,50 µL, então a precisão também está aprovada.

A aparente contradição da letra (c) se desfaz separando erro absoluto de erro relativo. O erro relativo é o desvio padrão dividido pelo valor medido:

$$
\text{CV}_{200} = \frac{0{,}053}{200} \approx 0{,}027\% \qquad \text{CV}_{1000} = \frac{0{,}059}{1000} \approx 0{,}006\%
$$

Embora o desvio absoluto seja um pouco maior em 1000 µL, o erro relativo cai bastante. A frase está certa no sentido relativo: medir quantidades maiores reduz o peso proporcional do erro.

</details>

## Exercício 2 — A mesma balança, "qualidades" diferentes

Uma balança analítica de cinco casas decimais é usada para medir 0,00103 g e, em outra ocasião, 0,00003 g. Por que dizemos que a primeira medida tem "qualidade" melhor, se a balança é a mesma?

<details markdown="1">
<summary>Mostrar resposta</summary>

A balança tem sempre o mesmo erro absoluto, cerca de cinco microgramas, que é a sua resolução. O que muda é o quanto esse erro representa em relação ao valor medido:

$$
\text{CV}_1 = \frac{5 \times 10^{-6}}{1{,}03 \times 10^{-3}} \approx 0{,}49\% \qquad \text{CV}_2 = \frac{5 \times 10^{-6}}{3 \times 10^{-5}} \approx 17\%
$$

A segunda medida está sendo feita perto do limite de operação da balança, e por isso carrega muito mais incerteza relativa. A "qualidade" de uma medida é o seu erro relativo, não a balança em si.

</details>

## Exercício 3 — Escrevendo com dois algarismos significativos

Escreva com apenas dois algarismos significativos: 2,36 · 0,999999… · 0,395 · 0,125 · 0,00000236. Em seguida, reescreva os valores ambíguos 1300 g, 250 mg e 395000 µg de duas formas que eliminem a ambiguidade: escolhendo uma unidade apropriada e usando notação científica.

<details markdown="1">
<summary>Mostrar resposta</summary>

Arredondando para dois algarismos significativos: 2,36 vira 2,4; o número próximo de 1 vira 1,0; 0,395 vira 0,40; 0,125 vira 0,12 (regra do dígito par) ou 0,13 conforme a convenção do software; e 0,00000236 vira $2{,}4 \times 10^{-6}$.

Um número como 1300 g é ambíguo porque não dá para saber se os zeros são significativos. As duas formas padrão de resolver são:

$$
1300 \text{ g} = 1{,}3 \times 10^{3} \text{ g} = 1{,}3 \text{ kg}
$$

$$
250 \text{ mg} = 2{,}5 \times 10^{2} \text{ mg} = 0{,}25 \text{ g}
$$

$$
395000 \text{ µg} = 3{,}95 \times 10^{5} \text{ µg} = 395 \text{ mg}
$$

A notação científica e a troca de unidade deixam explícito quais dígitos foram realmente medidos.

</details>

## Exercício 4 — Leitura de 0,00025 g

Uma balança de cinco casas decimais mostra 0,00025 g.

a) Quantos algarismos significativos tem essa leitura?

b) Se a balança estiver mal instalada e a última casa não estabilizar, quantos algarismos significativos restam?

c) O mesmo valor escrito em microgramas é 250 µg. O número de algarismos significativos muda?

d) Como vibração, inclinação da superfície e correntes de ar afetam precisão e acurácia?

<details markdown="1">
<summary>Mostrar resposta</summary>

A leitura 0,00025 g tem dois algarismos significativos, porque os zeros à esquerda apenas posicionam a vírgula e não contam. Se a última casa não estabiliza, sobra apenas um algarismo confiável.

Trocar a unidade para microgramas não altera nada: o número de algarismos significativos é uma propriedade da medida, não da unidade. Tanto $0{,}00025$ g quanto $250$ µg representam a mesma informação, com os mesmos dois algarismos.

Quanto às condições, uma superfície inclinada introduz um erro sistemático e faz a balança perder acurácia, porque todas as leituras ficam deslocadas na mesma direção. Vibrações fazem o valor oscilar de forma aleatória e prejudicam a precisão. Correntes de ar podem causar tanto deslocamentos sistemáticos quanto oscilações, afetando as duas propriedades.

</details>

## Exercício 5 — Béqueres

Um lote de béqueres foi planejado para pesar em torno de 35 g. Uma amostra de dez unidades pesou 33,45 · 35,21 · 35,77 · 35,20 · 34,72 · 33,81 · 33,91 · 34,54 · 34,63 · 34,12 g. Calcule a precisão e a exatidão (esta em porcentagem) e avalie se há variação relevante em relação ao previsto.

<details markdown="1">
<summary>Mostrar resposta</summary>

A média da amostra é

$$
\bar{x} = \frac{33{,}45 + 35{,}21 + \cdots + 34{,}12}{10} = 34{,}536 \text{ g}
$$

A exatidão é a diferença em relação ao valor previsto:

$$
\text{viés} = 34{,}536 - 35 = -0{,}464 \text{ g} \quad\Rightarrow\quad \frac{-0{,}464}{35} \approx -1{,}3\%
$$

A precisão é o desvio padrão amostral,

$$
s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}} \approx 0{,}73 \text{ g}
$$

Existe um pequeno viés (os béqueres pesam um pouco menos que o previsto) e uma dispersão considerável de 0,73 g, que sugere variabilidade própria do processo de fabricação e merece investigação.

</details>
