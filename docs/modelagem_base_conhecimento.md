# Modelagem da Base de Conhecimento — Trabalho Etapa 2

## 1. Objetivo

Definir a estrutura da base de conhecimento do Sistema Especialista Inteligente para Mapeamento, Compatibilidade e Trilha de Carreira em TI.

A modelagem busca separar os conhecimentos sobre as carreiras da implementação do motor de inferência, possibilitando a manutenção e a expansão das regras sem modificar diretamente a lógica principal da aplicação.

## 2. Organização dos Dados

A base de conhecimento será armazenada em um arquivo JSON externo, denominado `dados/regras_carreiras.json`.

Sua estrutura deverá contemplar:

| Componente | Responsabilidade |
|---|---|
| Metadados | Identificação e versão da base |
| Escalas | Definição dos níveis de afinidade e conhecimento |
| Perguntas | Questões utilizadas na avaliação profissional |
| Dimensões | Áreas de interesse avaliadas pelo questionário |
| Carreiras | Identificação das dez trilhas profissionais |
| Pesos | Importância relativa das dimensões para cada carreira |
| Regras | Condições de inferência, ajustes e justificativas |
| Competências | Conhecimentos necessários para cada carreira |
| Níveis Júnior | Proficiência esperada em cada competência |
| Roadmaps | Tecnologias, certificações e sugestões de projetos |

## 3. Dimensões de Afinidade

A avaliação considerará inicialmente dez dimensões:

1. Lógica e resolução de problemas.
2. Desenvolvimento de interfaces e experiência do usuário.
3. Dados, matemática e estatística.
4. Desenvolvimento de sistemas e APIs.
5. Infraestrutura e computação em nuvem.
6. Segurança da informação.
7. Automação, operações e confiabilidade.
8. Desenvolvimento para dispositivos móveis.
9. Qualidade e testes de software.
10. Gestão de produtos e visão de negócio.

Cada dimensão será avaliada em escala de 1 a 5.

Uma dimensão poderá contribuir para diferentes carreiras, com pesos distintos.

## 4. Compatibilidade Ponderada

Cada carreira possuirá pesos associados às dimensões de afinidade.

As respostas serão normalizadas e combinadas utilizando média ponderada.

O resultado será convertido para a escala percentual de 0% a 100%.

Regras adicionais poderão aplicar bônus ou penalidades conforme combinações de respostas, desde que suas condições e valores estejam definidos na base de conhecimento.

A aplicação deverá apresentar um ranking com as três carreiras mais compatíveis.

Os percentuais indicam compatibilidade dentro do modelo implementado, não probabilidades estatísticas.

## 5. Análise de Competências

O usuário também informará seu conhecimento atual em competências técnicas relevantes.

A escala de conhecimento será de 0 a 5, sendo:

- 0: nenhum conhecimento.
- 1: conhecimento inicial.
- 2: conhecimento básico.
- 3: conhecimento intermediário.
- 4: conhecimento avançado.
- 5: domínio elevado.

A base de conhecimento definirá o nível esperado para atuação Júnior em cada competência.

A lacuna será calculada pela diferença positiva entre o nível esperado e o nível informado pelo usuário.

Lacuna = máximo(0, nível esperado - nível atual).

Os níveis esperados representam referências adotadas pelo sistema, não requisitos universais do mercado.

## 6. Roadmap Personalizado

O plano de desenvolvimento deverá considerar a carreira escolhida e as lacunas identificadas.

As recomendações serão organizadas por prioridade e poderão incluir:

- Tecnologias e conhecimentos a estudar.
- Certificações pertinentes à carreira.
- Projetos práticos para o portfólio GitHub.

As recomendações deverão estar vinculadas às competências cadastradas na base de conhecimento.

## 7. Motor de Inferência

O motor deverá carregar dinamicamente as informações do JSON, validar sua estrutura e processar as respostas do usuário.

A lógica geral de avaliação será implementada em Python, enquanto os parâmetros específicos das carreiras, os pesos e as condições das regras ficarão armazenados externamente.

A solução deverá permitir a identificação de evidências favoráveis, conflitos entre preferências e justificativas rastreáveis.

## 8. Validação

A implementação deverá possuir testes que verifiquem:

- Integridade do arquivo JSON.
- Existência das dez carreiras.
- Validade dos pesos e das escalas.
- Cálculo das compatibilidades percentuais.
- Ordenação do ranking.
- Aplicação de bônus e penalidades.
- Identificação de lacunas de competências.
- Personalização do roadmap.
- Tratamento de perfis ambíguos e casos limite.

## 9. Considerações

Esta modelagem constitui a proposta inicial da nova base de conhecimento.

Os pesos, as regras específicas, os níveis de proficiência e os conteúdos dos roadmaps serão definidos e validados durante as etapas seguintes do desenvolvimento, conforme os requisitos do trabalho acadêmico.