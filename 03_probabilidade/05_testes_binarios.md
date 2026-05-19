# Testes binários

Um teste binário é qualquer procedimento diagnóstico cujo resultado tem **apenas duas possibilidades**: positivo ou negativo.

## Exemplos

- Teste de COVID (PCR ou antígeno);
- Sorologia para HIV;
- Mamografia (alterada ou normal);
- Verificação se um marcador está acima de um valor de corte.

## Os quatro cenários possíveis

Comparando o resultado do teste com a **verdade** (o paciente realmente tem ou não a doença), surgem 4 combinações:

|   | Tem doença | Não tem doença |
| --- | --- | --- |
| **Teste positivo** | Verdadeiro Positivo (VP) | Falso Positivo (FP) |
| **Teste negativo** | Falso Negativo (FN) | Verdadeiro Negativo (VN) |

Essa tabela é a base de tudo que vem a seguir:

- **Sensibilidade e especificidade** (próximo tópico): medem qualidades do **teste**.
- **Valor preditivo positivo e negativo**: respondem à pergunta do paciente: "meu teste deu positivo, qual a chance de eu ter mesmo a doença?".
- **Matriz de confusão**: forma de visualizar os 4 resultados.
- **Curva ROC**: descreve o teste sob diferentes pontos de corte.

## A tensão entre os erros

Todo teste binário tem que decidir como tratar a incerteza. Existem dois tipos de erro:

| Erro | O que é | Consequência |
| --- | --- | --- |
| **Falso positivo** | Teste positivo em quem **não** tem a doença | Ansiedade, exames adicionais, custos |
| **Falso negativo** | Teste negativo em quem **tem** a doença | Atraso no tratamento, doença não detectada |

> Reduzir um tipo de erro tipicamente **aumenta** o outro. Por isso, na prática, escolhemos onde colocar o ponto de corte dependendo do contexto clínico.

## Quando minimizar cada tipo de erro

- **Triagem de doenças graves**: priorizamos **alta sensibilidade** (não perder nenhum doente), aceitando mais falsos positivos. Ex.: triagem neonatal, mamografia.
- **Confirmação diagnóstica**: priorizamos **alta especificidade** (não dar falso positivo), aceitando perder alguns. Ex.: teste confirmatório de HIV após triagem positiva.

## Por que isso é tão estatístico?

Porque cada teste tem **probabilidades** associadas a cada cenário, e essas probabilidades dependem:

- da **qualidade do teste** (sensibilidade e especificidade);
- da **prevalência da doença** na população testada;
- do **valor de corte** escolhido.

Nos próximos tópicos, vamos quantificar cada um desses elementos.
