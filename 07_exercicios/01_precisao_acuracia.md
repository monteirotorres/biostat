# Precisão, acurácia e algarismos significativos

Exercícios sobre medidas, erros e a representação correta de números. Tente resolver a partir do enunciado antes de abrir a resposta.

## Exercício 1 — Calibração de pipeta

Um certificado de conformidade de uma pipeta traz duas séries de pesagens de água. Para o volume nominal de 200 µL foram registrados 198,75 · 198,83 · 198,78 · 198,87 (mg); para 1000 µL, 996,41 · 996,34 · 996,48 · 996,44 (mg).

a) A exatidão está dentro da tolerância (±3,00 µL para 200 µL e ±8,00 µL para 1000 µL)?

b) A precisão está dentro da especificação (desvio padrão < 0,60 µL para 200 µL e < 1,50 µL para 1000 µL)?

c) Costuma-se dizer que "para obter um erro menor, manipule quantidades maiores". No entanto, o desvio padrão de 1000 µL é maior que o de 200 µL. Como conciliar as duas afirmações?

<details markdown="1">
<summary>Mostrar resposta</summary>

A exatidão mede o quanto a média das pesagens se afasta do valor nominal. A média de 200 µL fica em torno de 198,8 mg, o que corresponde a um desvio de aproximadamente −0,5 µL após a conversão; para 1000 µL o desvio é de cerca de −0,3 µL. Os dois valores estão bem dentro das tolerâncias, então a exatidão está aprovada.

A precisão mede a dispersão das pesagens em torno da própria média. Os desvios padrão ficam em torno de 0,05 µL nas duas séries, muito abaixo dos limites de 0,60 e 1,50 µL. A precisão também está aprovada.

A aparente contradição da letra (c) se desfaz quando separamos erro absoluto de erro relativo. Quando manipulamos volumes maiores, o erro absoluto realmente tende a crescer (0,05 µL contra um valor um pouco maior), mas o que interessa na prática é o erro relativo, ou seja, o erro dividido pelo valor medido. Em termos percentuais, a dispersão cai de cerca de 0,027% (para 200 µL) para cerca de 0,006% (para 1000 µL). A frase está correta no sentido relativo: medir quantidades maiores reduz o peso proporcional do erro.

</details>

## Exercício 2 — A mesma balança, "qualidades" diferentes

Uma balança analítica de cinco casas decimais é usada para medir 0,00103 g e, em outra ocasião, 0,00003 g. Por que dizemos que a primeira medida tem "qualidade" melhor, se a balança é a mesma?

<details markdown="1">
<summary>Mostrar resposta</summary>

A balança tem sempre o mesmo erro absoluto, da ordem de cinco microgramas, porque essa é a sua resolução. O que muda entre as duas medidas é o quanto esse erro representa em relação ao valor medido.

Para 0,00103 g, cinco microgramas correspondem a cerca de 0,5% do valor. Para 0,00003 g, os mesmos cinco microgramas correspondem a cerca de 17%. A segunda medida está sendo feita perto do limite de operação da balança, e por isso carrega muito mais incerteza relativa. A "qualidade" de uma medida é justamente o seu erro relativo, e não a balança em si.

</details>

## Exercício 3 — Escrevendo com dois algarismos significativos

Escreva com apenas dois algarismos significativos: 2,36 · 0,999999… · 0,395 · 0,125 · 0,00000236. Em seguida, reescreva os valores ambíguos 1300 g, 250 mg e 395000 µg de duas formas que eliminem a ambiguidade: escolhendo uma unidade apropriada e usando notação científica.

<details markdown="1">
<summary>Mostrar resposta</summary>

Arredondando para dois algarismos significativos: 2,36 vira 2,4; o número próximo de 1 vira 1,0; 0,395 vira 0,40; 0,125 vira 0,12 (regra do dígito par) ou 0,13 conforme a convenção do software; e 0,00000236 vira 2,4×10⁻⁶.

Um número como 1300 g é ambíguo porque não dá para saber se os zeros são significativos. Escrevendo 1,3×10³ g ou 1,3 kg, fica claro que há dois algarismos significativos. Da mesma forma, 250 mg com dois algarismos vira 2,5×10² mg ou 0,25 g, e 395000 µg com três algarismos vira 3,95×10⁵ µg ou 395 mg. A notação científica e a troca de unidade resolvem a ambiguidade porque deixam explícito quais dígitos foram realmente medidos.

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

Trocar a unidade para microgramas não altera nada: o número de algarismos significativos é uma propriedade da medida, não da unidade escolhida. Tanto 0,00025 g quanto 250 µg representam a mesma informação, com os mesmos dois algarismos significativos.

Quanto às condições de instalação, uma superfície inclinada introduz um erro sistemático e faz a balança perder acurácia, porque todas as leituras ficam deslocadas na mesma direção. Vibrações fazem o valor oscilar de forma aleatória e prejudicam a precisão. Correntes de ar podem causar tanto deslocamentos sistemáticos quanto oscilações, afetando as duas propriedades ao mesmo tempo.

</details>

## Exercício 5 — Béqueres

Um lote de béqueres foi planejado para pesar em torno de 35 g. Uma amostra de dez unidades pesou 33,45 · 35,21 · 35,77 · 35,20 · 34,72 · 33,81 · 33,91 · 34,54 · 34,63 · 34,12 g. Calcule a precisão e a exatidão (esta em porcentagem) e avalie se há variação relevante em relação ao previsto.

<details markdown="1">
<summary>Mostrar resposta</summary>

A média da amostra fica em torno de 34,5 g. A exatidão é a diferença entre essa média e o valor previsto de 35 g, ou seja, cerca de −0,5 g, o que equivale a aproximadamente −1,3% em termos relativos. Existe, portanto, um pequeno viés: os béqueres tendem a pesar um pouco menos que o planejado.

A precisão é o desvio padrão da amostra, em torno de 0,73 g. Essa dispersão é considerável diante do desvio do alvo, o que sugere que o processo de fabricação tem variabilidade própria que merece investigação, e não apenas um deslocamento constante.

</details>
