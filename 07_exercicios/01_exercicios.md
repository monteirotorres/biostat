# Exercícios

Coletânea de exercícios resolvidos de bioestatística, organizados por tema, baseada na planilha de exercícios do curso (Prof. Gilberto Weissmüller).

> **Como estudar:** matemática não se aprende só lendo. Tente resolver cada exercício **a partir do enunciado**, antes de olhar a resposta. Abra uma planilha (Google Sheets, Excel) ou o notebook que acompanha esta seção e refaça os cálculos.

---

## 1. Precisão, acurácia e algarismos significativos

### 1.1 — Calibração de pipeta

Um certificado de conformidade de uma pipeta traz duas séries de pesagens (volume nominal 200 µL e 1000 µL):

- 200 µL: 198,75 · 198,83 · 198,78 · 198,87 (mg)
- 1000 µL: 996,41 · 996,34 · 996,48 · 996,44 (mg)

**a)** A **exatidão** está dentro da tolerância (±3,00 µL para 200; ±8,00 para 1000)?
**b)** A **precisão** está dentro da especificação (DP < 0,60 µL para 200; < 1,50 para 1000)?
**c)** "Para obter um erro menor, manipule quantidades maiores." Mas o DP de 1000 µL é maior que o de 200 µL. Explique.

**Resposta:** (a) As diferenças em relação ao nominal (~−0,54 e −0,29 µL) são menores que as tolerâncias → exatidão OK. (b) Os desvios padrão (~0,05 µL) são bem menores que os limites → precisão OK. (c) O que cai com quantidades maiores é o **erro relativo** (coeficiente de variação), não o absoluto. Em %, o desvio cai de ~0,027% para ~0,006%. A afirmação procede no sentido relativo.

### 1.2 — Mesma balança, "qualidades" diferentes

Uma balança de 5 casas mede 0,00103 g e 0,00003 g. Por que dizemos que a primeira medida tem "melhor qualidade"?

**Resposta:** É a mesma balança (mesmo erro absoluto, ±5 µg). O que muda é o **erro relativo**: ~0,49% para 0,00103 g contra ~17% para 0,00003 g. No segundo caso, a balança opera perto do seu limite.

### 1.3 — Algarismos significativos

Escreva com 2 algarismos significativos: 2,36 · 0,999999… · 0,395 · 0,125 · 0,00000236. Depois, reescreva valores ambíguos (1300 g; 250 mg; 395000 µg) sem ambiguidade, com unidade apropriada **e** notação científica.

**Resposta:** 2,4 · 1,0 · 0,40 · 0,12 (ou 0,13) · 2,4×10⁻⁶. Ambíguos: 1300 g = 1,3×10³ g = 1,3 kg; 250 mg = 2,5×10² mg = 0,25 g; 395000 µg = 3,95×10⁵ µg = 395 mg.

### 1.4 — Leitura de 0,00025 g

Numa balança de 5 casas lê-se 0,00025 g. (a) Quantos a.s.? (b) Se a última casa não estabiliza? (c) Em µg (250 µg)? (d) Como vibração, inclinação e correntes de ar afetam precisão e acurácia?

**Resposta:** (a) 2 a.s. (b) 1 a.s. (c) O nº de a.s. é propriedade da **medida**, não da unidade → continua 2. (d) Superfície inclinada → perde **acurácia**; vibração → perde **precisão**; corrente de ar → afeta ambas.

### 1.5 — Béqueres (precisão e exatidão)

Lote previsto para ~35 g. Amostra de 10 béqueres: 33,45 · 35,21 · 35,77 · 35,20 · 34,72 · 33,81 · 33,91 · 34,54 · 34,63 · 34,12 g. Calcule precisão e exatidão (esta em %) e avalie a variação.

**Resposta:** Média ≈ 34,54 g → exatidão (viés) ≈ −0,46 g ≈ −1,3%. DP ≈ 0,73 g (precisão). A variação é maior que a esperada para um processo bem controlado — investigar.

---

## 2. Probabilidade e intuição

### 2.1 — Reformular a definição de "ganhar na Megasena"

Qual das reformulações é equivalente a "ganhar na Megasena"? (a) acertar os 6 números; (b) ganhar o prêmio; (c) ficar rico; (d) acertar e ter o dinheiro na conta; (e) nenhuma.

**Resposta:** (e). Toda reformulação muda sutilmente o sentido (você pode acertar e perder o bilhete; outra pessoa pode ganhar e te doar; etc.). Lição: reformular probabilidades é traiçoeiro — prefira a definição original.

### 2.2 — Problema do aniversário

Em uma sala com 40 pessoas, qual a probabilidade de ao menos duas fazerem aniversário no mesmo dia?

**Resposta:** ~89% (alternativa "muito grande"). Calcula-se por $1 - \frac{365!}{(365-40)!\,365^{40}}$. Resultado contraintuitivo — o famoso *paradoxo do aniversário*.

### 2.3 — O andar do bêbado (random walk)

Gerando passos aleatórios +1/−1 e somando recursivamente, obtém-se uma caminhada aleatória. (Veja a simulação no notebook.)

**Resposta:** A posição após $n$ passos tem média 0 e desvio padrão $\sqrt{n}$ — o bêbado se afasta da origem proporcionalmente à **raiz** do número de passos.

---

## 3. Probabilidade

### 3.1 — O problema de Chevalier de Méré

O que é mais provável: ao menos um 6 em 4 lançamentos de um dado, ou ao menos um duplo-6 em 24 lançamentos de dois dados?

**Resposta:** Caso 1: $1 - (5/6)^4 = 0{,}518$. Caso 2: $1 - (35/36)^{24} = 0{,}491$. O primeiro é **mais provável**. O raciocínio de Méré (número médio = 2/3 em ambos) confunde **valor esperado** com **probabilidade**.

### 3.2 — Megasena

Probabilidade de ganhar com o jogo mínimo?

**Resposta:** $1/\binom{60}{6} = 1/50\,063\,860 \approx 2{,}0\times10^{-8}$. Pode-se pensar como combinação $C(60,6)$ ou como $\frac{6}{60}\cdot\frac{5}{59}\cdots\frac{1}{55}$.

### 3.3 — Cientista consciencioso

Com $\alpha = 5\%$ e confirmação independente: (a) probabilidade de uma publicação falso-positivo? (b) Se $P(\text{FP}\mid\text{FP}) = 30\%$?

**Resposta:** (a) $0{,}05 \times 0{,}05 = 0{,}0025$ (0,25%). (b) $0{,}05 \times 0{,}30 = 0{,}015$ (1,5%). Confirmar reduz falsos positivos, mas a dependência entre experimentos piora muito o número.

---

## 4. Probabilidade condicional

### 4.1 — Rastreio de doença rara

Incidência 0,01%; sensibilidade 99%; especificidade 95%. Teste deu positivo — qual a probabilidade de ter a doença?

**Resposta:** Por Bayes: $P(D\mid+) = \frac{0{,}0001\cdot0{,}99}{0{,}0001\cdot0{,}99 + 0{,}9999\cdot0{,}05} \approx 0{,}2\%$. Apesar de baixíssimo, é 20× maior que a prevalência inicial. Doença rara → muitos falsos positivos.

### 4.2 — Previsão do tempo

Acerta 80% dos dias de chuva e 90% dos de bom tempo; chove em 10% dos dias. Se previu chuva, qual a probabilidade de chover?

**Resposta:** Sensibilidade 0,8; especificidade 0,9; prevalência 0,1 → $P(D\mid+) = \frac{0{,}1\cdot0{,}8}{0{,}1\cdot0{,}8 + 0{,}9\cdot0{,}1} = \frac{8}{17} \approx 47{,}1\%$.

### 4.3 — AVC e pressão alta

10% dos idosos terão AVC em 5 anos; 40% dos que tiveram AVC tinham PA elevada; 20% dos que não tiveram AVC tinham PA elevada aos 70. Qual a probabilidade de um idoso com PA alta sofrer AVC?

**Resposta:** Prevalência 10%, sensibilidade 40%, especificidade 80% → tabela 2×2 (por 100 pessoas): VP=4, FP=18 → $P = 4/22 \approx 18{,}2\%$.

---

## 5. Estatística descritiva

### 5.1 — Quando usar média, mediana, DP, IQR?

**Resposta:** Distribuição ~normal → média e DP bastam. Assimétrica → média **e** mediana (carregam informações diferentes: renda → mediana mostra concentração, média mostra total) + quantis/IQR. Tempo de sobrevida → mediana e quantis.

### 5.2 — Salários

10 mil empregados: 1000 ganham 2 SM, 3000 ganham 3 SM, 6000 ganham 4 SM. Média e mediana?

**Resposta:** Mediana = 4 SM (o valor central cai na faixa dos 4 SM). Média = $(1000\cdot2 + 3000\cdot3 + 6000\cdot4)/10000 = 3{,}5$ SM. Mediana > média: assimetria à esquerda.

### 5.3 — Salário mediano (PNAD)

Distribuição por faixas (menos de 1 SM: 24,1%; 1–1,5: 20,6%; 1,5–3: 28,5%; …). Qual a faixa mediana?

**Resposta:** Acumulando: 24,1% + 20,6% = 44,7% (até 1,5 SM); +28,5% = 73,2% (até 3 SM). O 50% cai na faixa **1,5–3,0 SM**.

---

## 6. Distribuição binomial

### 6.1 — Falsos positivos acumulados

Com $\alpha=5\%$, qual a probabilidade de ao menos um falso positivo ao repetir o teste $k$ vezes?

**Resposta:** $1 - 0{,}95^k$. Para $k=3$: 14,3%; $k=10$: 40,1%; $k=50$: 92,3%. Consequência: comparar 3+ grupos par a par com teste t infla $\alpha$ → use **ANOVA**.

### 6.2 — Pôquer

4 jogadores de igual habilidade, 10 partidas, aposta fixa. Probabilidade de **não** perder dinheiro?

**Resposta:** Não perder = vencer ≥ 3 das 10 (cada vitória com $p=1/4$). $P(X \ge 3) = 1 - P(X \le 2) \approx 0{,}474$.

### 6.3 — Mudas e fungos

Contaminação $p=0{,}06$; custo R$1,20; venda R$3,50; lote de 50. (a) lucro previsto; (b) P(nenhuma contaminação); (c) P(menos de 10 contaminadas).

**Resposta:** (a) ~50·0,94·3,50 − 50·1,20 ≈ R$104,50. (b) $0{,}94^{50} \approx 0{,}045$. (c) $P(X \le 9) \approx 0{,}9993$.

### 6.4 — Prova de múltipla escolha

5 opções, 1 correta. Probabilidade de passar (nota ≥ 5) só no chute, com (a) 10 questões; (b) 20 questões?

**Resposta:** (a) $P(X \ge 5)$ em Binomial(10; 0,2) $\approx 0{,}033$. (b) Binomial(20; 0,25), $P(X \ge 10) \approx 0{,}0026$. A nota mais provável em (a) é 2.

### 6.5 — Controle de qualidade

Máquina com 0,5% de defeito. Amostra de 10; desliga se > 1 defeituosa. Probabilidade de desligar à toa?

**Resposta:** $P(X > 1) = 1 - P(0) - P(1) \approx 0{,}0011$.

### 6.6 — Genética mendeliana

Cruzamento 3:1 (amarelo:verde). Em 100 sementes, P(80 ou mais amarelas)?

**Resposta:** Binomial(100; 0,75), $P(X \ge 80) \approx 0{,}149$.

---

## 7. Distribuição normal

### 7.1 — Regra 68–95–99,7

Percentuais em ±1, ±2, ±3 desvios padrão?

**Resposta:** 68,3%; 95,4%; 99,7%. Vale para **qualquer** μ e σ.

### 7.2 — Normal para variáveis só positivas

Como aplicar a normal (que vai de −∞ a +∞) a alturas?

**Resposta:** A normal é "localizada": 170 ± 15 cm praticamente não chega a valores negativos. Ela descreve bem a **massa** dos dados; extremos (nanismo, gigantismo) são tratados como subpopulações separadas.

### 7.3 — Elevador

Capacidade 500 kg; pesos N(70, 10). (a) P(7 passageiros ultrapassarem)? (b) E 6?

**Resposta:** Distribuição amostral da soma. (a) soma ~ N(490, 10√7) → $P(\text{soma}>500) \approx 0{,}353$. (b) N(420, 10√6) → $\approx 0{,}0005$.

### 7.4 — Pressão arterial

PA ~ N(100, 10). (a) % entre 80 e 120? (b) faixa central com 95%? (c) acima de qual valor está só 1%?

**Resposta:** (a) ±2σ ≈ 95,4%. (b) 100 ± 1,96·10 ≈ [80,4; 119,6]. (c) $100 + 2{,}33\cdot10 \approx 123{,}3$ mmHg.

### 7.5 — Média de 4 pessoas

Mesma PA ~ N(100,10), amostra de 4. (a) P(média entre 80 e 120)? (b) faixa com 95% das médias? (c) e se σ for desconhecido (s = 7,8)?

**Resposta:** Erro padrão = 10/√4 = 5. (a) ±4σ_média ≈ 99,99%. (b) 100 ± 1,96·5 ≈ [90,2; 109,8]. (c) usar **t**: 100 ± t(5%,3)·7,8/√4 = 100 ± 3,18·3,9 ≈ ±12,4.

### 7.6 — Garantia de lavadoras

Vida útil N(1,5; 0,3) anos. % que falha antes de 1 ano (garantia)?

**Resposta:** $z = (1-1{,}5)/0{,}3 = -1{,}67$ → $P \approx 4{,}8\%$.

### 7.7 — Temperatura corporal

T ~ N(36,8; 0,15). (a) De 1000 homens, quantos entre 36,8 e 37,0? (b) Faixa central com 50%?

**Resposta:** (a) $P(36{,}8<T<37{,}0) = \Phi(1{,}33)-0{,}5 \approx 0{,}409$ → ~409 indivíduos. (b) ±0,674σ → [36,70; 36,90] °C.

---

## 8. Distribuição amostral

### 8.1 — Caixa de produtos

Produto ~ 10 g (DP 2 g), 50 por caixa; caixa vazia 500 g (DP 25 g). P(caixa cheia > 1050 g)?

**Resposta:** Média da caixa cheia = 500 + 50·10 = 1000 g. Variância = 25² + 50·2² = 625 + 200 = 825 → DP ≈ 28,7 g. $z = (1050-1000)/28{,}7 \approx 1{,}74$ → $P \approx 0{,}041$.

---

## 9. Lógica da inferência e intervalo de confiança

### 9.1 — Descritiva ou inferencial?

Professor compara proporções pró-pena de morte na **própria** turma. Que tipo de estatística?

**Resposta:** **Descritiva** — não há tentativa de generalizar além da turma estudada.

### 9.2 — Significância × relevância

**Resposta:** Significância = diferença detectável pelo design (depende de n, pareamento, variabilidade). Relevância = utilidade prática. Com n grande, detecta-se diferenças mínimas e irrelevantes (ex.: 0,1 ponto de QI entre irmãos).

### 9.3 — Intervalo de confiança

Amostra (de população normal): 5,3,4,2,3,4,2,3,4,5. (a) IC 95%; (b) interprete.

**Resposta:** Média = 3,5; s ≈ 1,08; t(5%,9) = 2,262 → 3,5 ± 2,262·1,08/√10 ≈ [2,7; 4,3]. (b) Se repetíssemos o experimento muitas vezes, 95% dos intervalos conteriam a média populacional.

### 9.4 — Moeda viciada (lógica binomial)

20 lançamentos, $\alpha = 5\%$. Quais proporções levam a rejeitar "moeda honesta"?

**Resposta:** ≤ 5 caras ou ≥ 15 caras (área bilateral ≈ 4,1% < 5%). Com $\alpha = 1\%$, só ≤ 4 ou ≥ 16.

---

## 10. Testes de dois grupos

### 10.1 — Anatomia de um teste

**Resposta:** Defina **hipóteses** (paramétrico? lateralidade?) e **design** (pareado? α?). Calcule o valor-p e compare com α: $p<\alpha$ → significativo.

### 10.2 — Besouros em duas florestas

Amostra 1: 8,12,15,21,25,44,44,60; Amostra 2: 2,4,5,9,12,17,19. Qual teste? Conclusão (P = 2,8%)?

**Resposta:** Contagens baixas → assimétrico → **não paramétrico**; sem pareamento; bilateral; α=5% → **Mann–Whitney**. Como $p=0{,}028<0{,}05$, há diferença significativa (mais besouros na floresta 1).

### 10.3 — Halotano vs. Morfina

PA média: Halotano 66,9 (DP 12,2; n=61); Morfina 73,2 (DP 14,4; n=61). (a) Diferença significativa? (b) Estime a diferença real. (c) Mortalidade 8/61 vs 10/61 difere?

**Resposta:** (a) Teste t não pareado bilateral → $p \approx 0{,}010$ → significativo. (b) IC 95% da diferença ≈ [−11; −1,5] mmHg. (c) Tabela de contingência (qui-quadrado/Fisher) → não significativo.

### 10.4 — Pressão arterial homens × mulheres

Dados simulados (12 por grupo) a partir do Wolfram|Alpha. Teste t indica diferença?

**Resposta:** Com n pequeno e diferença real pequena (≈3 mmHg) ante DP grande (~17–21), o teste tende a **não** detectar — poder baixíssimo (veja exercício de potência).

### 10.5 — Teste t "à mão" vs. software

A1 (n=10, m=4,5, s=3,03) vs A2 (n=10, m=7,5, s=3,03). Há diferença?

**Resposta:** $t = (4{,}5-7{,}5)/(3{,}03\cdot\sqrt{2/10}) \approx -2{,}22$, gl=18. Como $|t|=2{,}22 > t_{crit}=2{,}10$ → diferença **significativa**.

### 10.6 — Hemoglobina antes/depois (pareado)

Hb medida em 8 indivíduos antes e depois da droga. Avalie a eficácia.

**Resposta:** Como é o **mesmo** indivíduo medido 2×, use **teste t pareado** sobre as diferenças. Se $p<0{,}05$, a droga altera a Hb.

---

## 11. ANOVA (um fator)

### 11.1 — Drogas A, B e placebo

Contagem de linfócitos em 7 ninhadas, 3 tratamentos (animais da mesma ninhada). As drogas diferem do placebo?

**Resposta:** Como os animais vêm da **mesma ninhada** (pareamento), use **ANOVA de medidas repetidas**. "Diferem do placebo" → pós-teste de **Dunnett** (compara com controle). Resultado: $p \approx 0{,}002$; só A difere de P.

### 11.2 — Concurso na UFRJ

6 candidatos, 5 avaliadores. A banca diferencia candidatos? Há empates estatísticos?

**Resposta:** Avaliadores diferem em rigor → **medidas repetidas**. A variabilidade **entre candidatos** supera a **entre avaliadores** → a banca consegue diferenciar. Porém candidatos próximos ficam empatados estatisticamente — o fator sorte é real.

---

## 12. Correlação e regressão

### 12.1 — Peso × altura

Dados (altura cm, peso kg): (152,38)…(193,68). (a) r; (b) R² e interpretação; (c) reta; (d) crítica.

**Resposta:** (a) $r \approx 0{,}77$. (b) $R^2 \approx 0{,}59$ → 59% da variação do peso "explicada" pela altura. (c) $y \approx 0{,}89x - 91$. (d) Há relação plausível, mas muitos fatores afetam o peso; a reta serve mais para descrever que para prever indivíduos.

### 12.2 — Experimento vs. estudo de correlação

**Resposta:** No experimento verdadeiro, manipula-se a variável independente com tudo sob controle → permite **causa-efeito**. No estudo de correlação, nada é controlado → revela **associação**, base para formular hipóteses, mas não prova causalidade.

### 12.3 — As 4 explicações de uma correlação

Se $r \ne 0$, quais explicações são possíveis?

**Resposta:** (i) X causa Y; (ii) Y causa X; (iii) uma terceira variável causa ambos; (iv) acaso (o valor-p mede a frequência do acaso). Veja exemplos de correlações espúrias (tylervigen.com).

---

## 13. Potência

### 13.1 — Tamanho da amostra × precisão

Para n = 2, 3, 4, 6, 10, 20 (população N(1,1)), como variam desvio da média, DP, SEM e IC?

**Resposta:** O **SEM** e a largura do IC caem com $1/\sqrt{n}$; o DP estimado se aproxima de 1; o erro da média diminui. Dobrar a precisão exige **quadruplicar** n.

### 13.2 — Escolha do sexo da prole

Dois casais, ambos com 2 meninos. O tratamento funciona?

**Resposta:** Sob $H_0$ (não funciona, binomial), $P = (1/2)^4 = 0{,}0625 > 0{,}05$. Com só 4 crianças, o menor p possível já é 6,25% → **poder zero**, teste inconclusivo.

### 13.3 — Potência da PA homens × mulheres

Diferença real ≈ 3 mmHg, σ ~ 17–21. (a) Poder com n=24? (b) n para 80%? (c) Poder com toda a amostra?

**Resposta:** (a) ~6,8% (ridículo). (b) ~568 por grupo. (c) Com n nas milhares, poder ≈ 1.

### 13.4 — Trocando n por δ

Situação A: σ=1, n=17, δ=1 → poder 81%. Situação B: mesmo σ e poder, n=25, δ=? Maior ou menor que 1?

**Resposta:** **Menor** que 1 — com amostra maior, detecta-se um efeito menor mantendo o mesmo poder.

---

## 14. Qui-quadrado

### 14.1 — Dado honesto

60 lançamentos, frequências 8,11,7,12,15,7. O dado é honesto? E se multiplicarmos tudo por 10?

**Resposta:** Esperado = 10/face. $\chi^2 = 5{,}2$, 5 gl → $p \approx 0{,}39$ → **não** rejeita (honesto). Com frequências ×10 (mesma tendência), $\chi^2 = 52$ → $p \approx 5\times10^{-10}$ → rejeita. Lição: o qui-quadrado depende do **n absoluto**, não só das proporções.

### 14.2 — Mendel 9:3:3:1

Observados 315/108/101/32 (total 556). O modelo 9:3:3:1 explica? E um modelo linear?

**Resposta:** Mendel: $\chi^2 \approx 0{,}47$ → $p \approx 0{,}93$ → não rejeita (ótimo ajuste). Linear: $\chi^2 \approx 62{,}6$ → $p \approx 0$ → rejeita. O modelo de Mendel descreve muito melhor.

---

## 15. Tabelas de contingência

### 15.1 — Mortalidade Halotano × Morfina

8/61 mortes (Halotano) vs 10/61 (Morfina). As proporções diferem?

**Resposta:** Tabela 2×2 → qui-quadrado (ou Fisher). Não se rejeita $H_0$ → as taxas de fatalidade não diferem significativamente.

### 15.2 — Efeito colateral × medicamento

Tabela 2×2 (usou/não usou × efeito presente/ausente). Como testar associação?

**Resposta:** Qui-quadrado de independência. Se $p$ for baixo, rejeita-se a independência → há associação entre o medicamento e o efeito colateral.

---

## 16. Técnicas de amostragem

### 16.1 — Motoristas × cobradores de ônibus

Cobradores (mais exercício) têm menos doença cardíaca que motoristas. (a) Variáveis e níveis; (b) correlação ou experimento? (c) por que controlar idade/tempo de serviço? (d) há associação? (e) outros confundidores?

**Resposta:** (a) Tratamento = exercício (muito/pouco); desfecho = doença cardíaca (sim/não). (b) **Estudo de correlação** — ninguém foi sorteado para a profissão. (c) Idade é confundidor (afeta o desfecho e pode diferir entre grupos). (d) Sim, há **associação** — mas não causa. (e) Saúde prévia, estresse do trabalho (motoristas já eram mais pesados ao serem contratados).

### 16.2 — Treinamento de lavagem das mãos

100 voluntários recebem treinamento e são comparados com os demais. Critique e proponha alternativa.

**Resposta:** Inválido: voluntários já são mais cuidadosos (viés de autosseleção) → resultado artificialmente positivo. Solução: **sortear** quem recebe o treinamento (aleatorização).

### 16.3 — Filhotes de rato e ninhadas

Filhotes misturados ao acaso e divididos em 4 doses. A amostragem é correta?

**Resposta:** Não. A Hb é homogênea **dentro** da ninhada. Misturar permite que diferenças de ninhada se confundam com o efeito da droga. Correto: pegar um filhote de **cada ninhada** para **cada dose** (amostragem em blocos/pareada).
