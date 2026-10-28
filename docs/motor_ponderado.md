# Motor de Inferência com Pontuação Ponderada

## 1. Objetivo

Documentar o funcionamento do motor de compatibilidade profissional desenvolvido para o Trabalho da Etapa 2 da disciplina de Inteligência Artificial.

O sistema utiliza um mecanismo próprio de inferência ponderada, baseado em uma base de conhecimento externa, para avaliar afinidades profissionais e apresentar um ranking das dez carreiras de Tecnologia da Informação.

## 2. Arquitetura

O processamento utiliza três componentes principais:

- `dados/regras_carreiras.json`: armazena carreiras, dimensões, pesos, regras e critérios de diagnóstico.
- `src/base_conhecimento.py`: carrega e valida a integridade da base de conhecimento.
- `src/motor_ponderado.py`: calcula as compatibilidades, aplica as regras e produz o ranking profissional.

Essa organização permite modificar os pesos e as condições das regras no JSON sem alterar diretamente o algoritmo de inferência.

O novo motor foi desenvolvido separadamente do sistema Experta da AECO, preservando sua implementação original.

## 3. Entrada de Dados

O motor recebe dez respostas graduais, representando as afinidades do usuário com diferentes dimensões profissionais.

Cada resposta utiliza uma escala de 1 a 5:

| Valor | Interpretação |
|---|---|
| 1 | Nenhuma afinidade |
| 2 | Pouca afinidade |
| 3 | Afinidade moderada |
| 4 | Alta afinidade |
| 5 | Afinidade muito alta |

O motor valida os valores recebidos e rejeita respostas ausentes, dimensões desconhecidas ou valores fora da escala.

## 4. Cálculo da Compatibilidade

Cada carreira possui pesos que indicam a importância relativa de determinadas dimensões profissionais.

A compatibilidade-base é calculada por uma média ponderada normalizada:

**Compatibilidade-base (%) = [Σ peso × (afinidade − 1) / (4 × Σ pesos)] × 100**

Essa fórmula produz resultados de 0% a 100%.

Uma afinidade moderada (3) em todas as dimensões corresponde a uma compatibilidade-base de 50% para todas as carreiras.

Os percentuais representam aderência aos critérios definidos pelo sistema, não probabilidades estatísticas de sucesso profissional.

## 5. Regras Ponderadas

A base de conhecimento contém 20 regras cruzadas, distribuídas entre as dez carreiras:

- Dez regras de bônus.
- Dez regras de penalidade.

Cada regra possui identificador, carreira associada, condições, ajuste percentual e justificativa.

As condições são avaliadas conjuntamente. Uma regra é acionada somente quando todas as suas condições são satisfeitas.

Após o cálculo inicial, os ajustes das regras acionadas são somados à compatibilidade-base.

**Compatibilidade final = Compatibilidade-base + Bônus − Penalidades**

O resultado é limitado ao intervalo de 0% a 100%.

As regras acionadas são registradas para permitir a apresentação de justificativas rastreáveis.

## 6. Ranking Profissional

O motor calcula a compatibilidade com todas as dez carreiras.

Os resultados são ordenados pelos seguintes critérios:

1. Maior compatibilidade final.
2. Maior compatibilidade-base.
3. Identificador da carreira, para desempate determinístico.

A resposta contém o ranking completo e as três carreiras mais bem posicionadas.

Cada resultado apresenta:

- Identificador e nome da carreira.
- Pontuação-base.
- Soma dos ajustes aplicados.
- Compatibilidade percentual final.
- Regras acionadas e respectivas justificativas.

## 7. Tratamento de Ambiguidade

Para evitar interpretações excessivamente conclusivas, o motor também classifica o perfil profissional.

Os critérios são configurados externamente em `criterios_diagnostico`.

| Classificação | Critério |
|---|---|
| Predominante | Compatibilidade máxima de pelo menos 55%, com vantagem superior a 10 pontos percentuais |
| Multifacetado | Compatibilidade máxima de pelo menos 55%, com diferença de até 10 pontos percentuais entre as duas primeiras |
| Inconclusivo | Compatibilidade máxima inferior a 55% |

A classificação complementa o ranking, mas não altera seus percentuais.

Um perfil inconclusivo continua recebendo o ranking para fins exploratórios, acompanhado de uma mensagem explicativa.

Os limites utilizados são parâmetros de modelagem acadêmica e podem ser ajustados após novas validações.

## 8. Testes e Validação

Foram implementados testes automatizados para verificar:

- Cálculo da compatibilidade ponderada.
- Aplicação de bônus e penalidades.
- Ordenação do ranking e seleção do Top 3.
- Tratamento determinístico de empates.
- Respostas inválidas e incompletas.
- Limites percentuais.
- Independência entre análises.
- Personas profissionais distintas.
- Perfis híbridos e conflitantes.
- Diagnósticos de predominância, multiplicidade de afinidades e inconclusão.

A bateria completa do projeto registrou 40 testes aprovados ao final da implementação desta fase.

## 9. Limitações

O sistema utiliza pesos, regras e limites definidos como parte da modelagem acadêmica.

Esses parâmetros não foram calibrados com uma amostra estatística de profissionais.

Portanto, os resultados devem ser interpretados como recomendações informativas baseadas nas preferências declaradas, não como avaliações definitivas de aptidão profissional.

A avaliação das competências técnicas, a identificação de lacunas e a geração de roadmaps serão implementadas em módulos específicos nas próximas fases.

## 10. Conclusão

O motor ponderado permite analisar respostas graduais, combinar evidências, aplicar ajustes lógicos, calcular compatibilidades e produzir recomendações rastreáveis.

A implementação fornece a base necessária para a evolução do sistema com análise de competências e orientação personalizada de desenvolvimento profissional.