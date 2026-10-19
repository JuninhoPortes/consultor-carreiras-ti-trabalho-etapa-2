
# Relatório de Validação — Sistema Especialista de Carreiras em TI

## 1. Objetivo

Documentar os testes realizados para verificar a precisão
das recomendações do sistema especialista, considerando
perfis profissionais distintos e situações de ambiguidade.

A validação contempla a interface Streamlit, o motor de
inferência Experta, as pontuações e as justificativas
apresentadas ao usuário.

## 2. Metodologia

Foram utilizados cinco cenários de avaliação:

- Persona Analítica.
- Persona de Segurança.
- Persona Visual.
- Persona de Negócios.
- Perfil Ambíguo com perguntas complementares.

Os cenários foram executados pela interface web,
utilizando as alternativas do questionário.

## 3. Respostas Utilizadas

As alternativas estão apresentadas na ordem Q01 a Q10.

| Persona | Respostas |
|---|---|
| Analítica | C, C, A, C, C, A, C, D, C, D |
| Segurança | B, F, E, E, E, C, C, D, A, D |
| Visual | A, B, B, B, B, C, C, B, C, D |
| Negócios | B, G, J, F, F, C, C, D, C, A |
| Ambígua | A, C, C, C, B, B, B, B, B, B |

## 4. Resultados da Validação

| Persona | Carreira recomendada | Pontos | Regras | Status |
|---|---|---|---|---|
| Analítica | Ciência de Dados e ML | 8 | R05, R06 | Aprovado |
| Segurança | Cibersegurança | 7 | R09, R10 | Aprovado |
| Visual | Front-end & UI/UX | 7 | R03, R04 | Aprovado |
| Negócios | Gestão de Produtos | 6 | R19, R20 | Aprovado |

Os resultados apresentados pela interface corresponderam
às recomendações esperadas para as quatro personas.

## 5. Validação do Perfil Ambíguo

O quinto cenário utilizou respostas distribuídas entre
diferentes especialidades.

Na avaliação inicial, o sistema não identificou uma
carreira predominante.

O sistema apresentou perguntas complementares,
permitindo uma investigação mais específica.

Respostas adicionais:

- Q11: Engenharia de Dados.
- Q12: Construir pipelines de dados.

Resultado:

- Carreira: Engenharia de Dados.
- Pontuação: 8 pontos.
- Regra complementar: R26.
- Status: Aprovado.

O resultado confirmou que a análise complementar
consegue utilizar evidências anteriores e novas
preferências para fundamentar uma recomendação.

## 6. Validação da Interface

Durante os testes manuais, foram verificados:

- Apresentação das 10 perguntas obrigatórias.
- Avisos para respostas incompletas.
- Remoção dos avisos ao alterar respostas.
- Rolagem automática até o resultado.
- Exibição da carreira e pontuação.
- Apresentação das justificativas das regras.
- Funcionamento do botão Refazer questionário.
- Apresentação das perguntas complementares.
- Preservação da identidade visual da aplicação.

Os comportamentos avaliados funcionaram conforme
o esperado nos cenários executados.

## 7. Testes Automatizados

Além dos testes manuais, o projeto possui testes
automatizados utilizando unittest.

A última bateria executada registrou:

- 17 métodos de teste.
- Resultado: OK.
- Validação das regras de inferência.
- Validação das recomendações profissionais.
- Testes de desempate e informações insuficientes.
- Validação das personas.
- Testes das perguntas complementares.

## 8. Conclusão

Os testes realizados apresentaram resultados
compatíveis com os critérios definidos na matriz
de decisão.

As quatro personas obrigatórias receberam as
recomendações esperadas, e o cenário ambíguo
foi tratado por meio da entrevista complementar.

A validação demonstra o funcionamento dos cenários
testados, sem garantir precisão para todos os
perfis profissionais possíveis.

O sistema atende aos cenários de validação
estabelecidos para esta etapa do projeto.
