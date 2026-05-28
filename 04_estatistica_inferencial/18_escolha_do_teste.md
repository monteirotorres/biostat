# Como escolher o teste (e o pós-teste)

Escolher o teste estatístico certo é, na maior parte das vezes, uma questão de responder a três perguntas sobre o seu problema, antes de qualquer conta.

A primeira pergunta é **o que se quer responder**: comparar grupos ou médias, medir a associação entre duas variáveis quantitativas, ou analisar variáveis categóricas. A segunda é **como os dados foram coletados**: quantos grupos existem e se eles são independentes ou pareados (o mesmo indivíduo medido mais de uma vez, ou pares casados). A terceira é **se a suposição de normalidade se sustenta**, o que decide entre um teste paramétrico e sua versão não-paramétrica.

O guia abaixo resume essas decisões.

![Guia de escolha de testes estatísticos](assets/slides/desenho/guia_testes.jpg)

## Comparar grupos ou médias

Aqui a variável de interesse é quantitativa, e a escolha depende do número de grupos e do pareamento. Quando a variável é aproximadamente normal (ou a amostra é grande o bastante para o teorema do limite central agir), usa-se o teste **paramétrico**; caso contrário, sua alternativa **não-paramétrica**, que trabalha com postos.

| Estrutura dos dados | Paramétrico | Não-paramétrico |
| --- | --- | --- |
| 1 grupo vs. um valor de referência | Teste t de uma amostra | Wilcoxon do sinal |
| 2 grupos independentes | Teste t (Welch) | Mann–Whitney |
| 2 grupos pareados | Teste t pareado | Wilcoxon pareado |
| 3 ou mais grupos independentes | ANOVA one-way | Kruskal–Wallis |
| 3 ou mais grupos pareados | ANOVA de medidas repetidas | Friedman |

Vale lembrar que os testes paramétricos são mais **potentes** quando a normalidade vale, mas os não-paramétricos são mais **robustos** quando ela falha ou quando os dados são ordinais.

## Associação entre duas variáveis quantitativas

Se a relação é razoavelmente **linear** e os dados são aproximadamente normais, usa-se a correlação de **Pearson** e, quando se quer prever uma variável a partir da outra, a **regressão linear**. Se a relação é monotônica mas não linear, ou se os dados são ordinais ou têm outliers, prefere-se a correlação de **Spearman**, calculada sobre os postos.

## Variáveis categóricas

Para testar associação entre duas variáveis categóricas, monta-se uma tabela de contingência e aplica-se o **qui-quadrado**, desde que as frequências esperadas sejam suficientes (em geral ≥ 5 por casela). Quando a amostra é pequena, usa-se o **teste exato de Fisher**. Para dados **pareados** em tabela 2×2 (por exemplo, o mesmo indivíduo antes e depois), o teste apropriado é o de **McNemar**.

## Qual pós-teste escolher

Quando uma ANOVA dá significativa, sabemos que **alguma** média difere, mas não qual. Os pós-testes (comparações múltiplas) respondem a isso controlando o erro tipo I acumulado. A escolha depende de **quais comparações** interessam.

| Situação | Pós-teste recomendado |
| --- | --- |
| Comparar todos os grupos entre si | Tukey HSD |
| Comparar cada grupo com um único controle | Dunnett |
| Poucas comparações planejadas de antemão | Bonferroni ou Šidák |
| Combinações lineares de médias (contrastes) | Scheffé |

Para as alternativas não-paramétricas, após um Kruskal–Wallis significativo usa-se o **teste de Dunn** (com correção de Bonferroni), e após um Friedman, comparações pareadas de Wilcoxon corrigidas.

## Antes de rodar qualquer teste

Nenhum fluxograma substitui olhar os dados. Faça um gráfico (histograma, boxplot, dispersão) antes de decidir, verifique as suposições do teste escolhido (normalidade, independência, variâncias) e, sempre que possível, reporte o **tamanho de efeito** e o **intervalo de confiança** junto com o valor-p — eles dizem o quanto o efeito importa, não apenas se ele é detectável.
