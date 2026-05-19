# Teste do qui-quadrado ($\chi^2$)

Testa **associação entre variáveis categóricas** comparando contagens observadas com as que esperaríamos sob H₀.

## Quando usar

- **Variáveis categóricas** (sexo, tipo sanguíneo, presença/ausência de doença, etc.).
- Contagens, não médias.
- Cada observação cai em **uma única categoria**.

## Duas variantes principais

### 1. Teste de aderência (*goodness-of-fit*)

Compara as frequências observadas em **uma variável** com uma distribuição teórica esperada.

$$
H_0: \text{os dados seguem a distribuição esperada}
$$

Exemplo: testar se a proporção observada de tipos sanguíneos em uma amostra corresponde às proporções nacionais.

### 2. Teste de independência (mais comum)

Verifica se **duas variáveis categóricas** são independentes.

$$
H_0: \text{as variáveis são independentes}
$$

Exemplo: existe associação entre sexo e desfecho clínico?

## A estatística qui-quadrado

$$
\chi^{2} = \sum_{i} \frac{(O_i - E_i)^{2}}{E_i}
$$

Onde:

- $O_i$: frequência **observada** em cada célula;
- $E_i$: frequência **esperada** sob H₀.

Quanto maior $\chi^2$, maior a discrepância entre o que vimos e o que esperaríamos. Sob H₀, ele segue a distribuição **qui-quadrado** com $(r-1)(c-1)$ graus de liberdade (onde $r$ e $c$ são linhas e colunas da tabela).

## Frequência esperada

Para o teste de independência, a frequência esperada de cada célula é:

$$
E_{ij} = \frac{(\text{total da linha } i) \cdot (\text{total da coluna } j)}{\text{total geral}}
$$

## Exemplo — Titanic

Sobrevivência por sexo:

|   | Sobreviveu | Morreu | Total |
| --- | --- | --- | --- |
| Mulheres | 233 | 81 | 314 |
| Homens | 109 | 468 | 577 |
| **Total** | 342 | 549 | 891 |

Frequência esperada (independência):

$$
E_{\text{mulher, sobrev.}} = \frac{314 \cdot 342}{891} \approx 120{,}5
$$

$$
\chi^{2} = \frac{(233 - 120{,}5)^{2}}{120{,}5} + \cdots \approx 261{,}6
$$

Com 1 grau de liberdade, $p$ é praticamente zero. Sexo e sobrevivência **não são independentes**.

## Suposições

| Suposição | Verificação |
| --- | --- |
| Observações independentes | Desenho do estudo |
| Cada observação em uma única célula | Categorias mutuamente exclusivas |
| Frequência esperada $\geq 5$ em cada célula | Olhar a tabela de esperados |

> Se mais de 20% das células têm $E < 5$, o qui-quadrado pode ser inadequado — use o **teste exato de Fisher**.

## Variações importantes

### Teste exato de Fisher

Quando a amostra é **pequena** ou alguma célula tem expectativa baixa. Calcula a probabilidade exata, sem aproximação.

### Correção de Yates

Pequena correção para tabelas 2x2 com $n$ pequeno. Em geral, usá-la torna o teste levemente mais conservador.

### Teste de McNemar

Para dados pareados em tabela 2x2 (ex.: antes vs. depois, com resposta binária).

## Tamanho de efeito

Para associação entre categóricas:

- **V de Cramér** (generaliza para tabelas $r \times c$):

$$
V = \sqrt{\frac{\chi^{2}}{n \cdot \min(r-1, c-1)}}
$$

- **Odds ratio** (para tabelas 2x2):

$$
\text{OR} = \frac{a \cdot d}{b \cdot c}
$$

> O valor-p sozinho não é suficiente — sempre reporte uma medida de tamanho de efeito.

## Em que situações aparece

- **Epidemiologia**: associação entre fator de risco e doença.
- **Genética**: associação entre alelos e fenótipos (testes de Hardy–Weinberg).
- **Ensaios clínicos**: comparar taxas de cura ou de eventos adversos entre grupos.
- **Estudos de qualidade**: testar se uma característica afeta uma taxa.

## Exemplo de relatório

> "Houve associação significativa entre sexo e sobrevivência ($\chi^{2}(1) = 261{,}6$, $p < 0{,}001$, V de Cramér = 0,54)."
