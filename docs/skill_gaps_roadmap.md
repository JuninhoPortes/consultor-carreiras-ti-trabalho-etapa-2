# Análise de Skill Gaps e Roadmap Personalizado

## 1. Objetivo

Documentar a implementação dos módulos de análise de lacunas de competências e geração de planos personalizados de desenvolvimento profissional do Sistema Especialista Inteligente para Carreiras em TI.

Essas funcionalidades ampliam o sistema de recomendação, permitindo identificar conhecimentos que o usuário precisa desenvolver para alcançar os níveis de referência Júnior definidos para determinada carreira.

## 2. Arquitetura

A implementação utiliza três componentes principais:

| Componente | Responsabilidade |
|---|---|
| `dados/regras_carreiras.json` | Armazena competências, níveis Júnior e recomendações de desenvolvimento |
| `src/analise_gaps.py` | Identifica lacunas e calcula a cobertura dos requisitos |
| `src/roadmap.py` | Gera recomendações personalizadas de estudo e portfólio |

Os módulos utilizam a base de conhecimento externa, mantendo separadas as informações profissionais e a lógica de processamento.

## 3. Avaliação de Competências

O sistema utiliza uma escala de conhecimento de 0 a 5.

Cada carreira possui competências específicas e níveis de referência para atuação Júnior, definidos no JSON.

A análise compara os conhecimentos declarados pelo usuário com os níveis esperados para a carreira selecionada.

### 3.1. Cálculo das lacunas

A lacuna de uma competência é calculada pela fórmula:

**Gap = máximo(0, nível Júnior − nível atual)**

Quando o nível atual é igual ou superior ao esperado, não existe lacuna naquela competência.

### 3.2. Cobertura dos requisitos

O sistema também calcula a cobertura dos requisitos utilizando:

**Cobertura (%) = [Σ mínimo(nível atual, nível Júnior) / Σ nível Júnior] × 100**

O resultado é limitado a 100%, impedindo que conhecimentos superiores ao nível esperado aumentem artificialmente a cobertura.

Esse percentual não representa garantia de empregabilidade ou certificação profissional.

## 4. Priorização das Lacunas

As competências pendentes são organizadas considerando:

1. Maior diferença entre o nível atual e o nível Júnior.
2. Maior nível Júnior exigido, em caso de gaps iguais.
3. Identificador da competência, para desempate determinístico.

Essa estratégia permite apresentar primeiro as competências com maiores deficiências segundo os critérios adotados pelo sistema.

## 5. Geração do Roadmap Personalizado

O módulo `GeradorRoadmap` recebe a carreira selecionada e os conhecimentos informados pelo usuário.

Inicialmente, executa o `AnalisadorGaps` para identificar as competências pendentes.

Em seguida, consulta o JSON para construir três componentes.

### 5.1. Plano de estudos

Os conteúdos são selecionados a partir das competências identificadas como lacunas.

Cada etapa apresenta:

- Prioridade.
- Competência.
- Nível atual.
- Nível Júnior esperado.
- Diferença de proficiência.
- Conteúdos recomendados.

Competências cujos níveis de referência já foram atendidos não são incluídas como lacunas no plano de estudos.

### 5.2. Certificações

O sistema identifica certificações relacionadas às competências pendentes, utilizando os relacionamentos cadastrados na base de conhecimento.

As certificações são sugestões opcionais de desenvolvimento e poderão exigir conhecimentos e experiências adicionais.

O sistema não verifica automaticamente os pré-requisitos oficiais dos exames nem garante que o usuário esteja preparado para realizá-los.

### 5.3. Projetos de portfólio

Cada carreira possui uma proposta de projeto prático cadastrada no JSON.

O sistema identifica quais competências pendentes poderão ser desenvolvidas durante a implementação desse projeto.

Mesmo quando não existem lacunas, o sistema mantém uma sugestão de portfólio para consolidar e demonstrar conhecimentos.

## 6. Exemplo de Validação — Desenvolvimento Back-end

Foi testado um perfil com os seguintes conhecimentos:

| Competência | Nível atual | Referência Júnior | Gap |
|---|---:|---:|---:|
| Programação | 3 | 3 | 0 |
| APIs REST | 1 | 3 | 2 |
| SQL | 0 | 2 | 2 |
| Git | 2 | 2 | 0 |

### Resultado

- Carreira: Desenvolvimento Back-end.
- Cobertura dos requisitos: 60%.
- Lacunas identificadas: 2.
- Primeira prioridade: Desenvolvimento de APIs REST.
- Segunda prioridade: Bancos de dados relacionais e SQL.

O roadmap recomendou estudos relacionados às duas competências pendentes e o projeto de portfólio denominado "API REST de gerenciamento de tarefas".

Também apresentou uma sugestão de certificação relacionada às competências identificadas.

Os resultados corresponderam aos critérios estabelecidos na base de conhecimento.

## 7. Testes Automatizados

Foram desenvolvidos testes com o framework `unittest`.

### Análise de Skill Gaps

Foram implementados seis testes para verificar:

- Identificação das lacunas de Back-end.
- Conhecimentos suficientes.
- Ausência de conhecimentos prévios.
- Conhecimentos superiores aos níveis exigidos.
- Entradas inválidas.
- Análise de outra carreira.

### Roadmap Personalizado

Foram implementados oito testes para verificar:

- Geração de roadmap com lacunas.
- Ordenação das prioridades.
- Seleção de certificações relacionadas.
- Carregamento dos conteúdos diretamente do JSON.
- Geração de roadmaps para as dez carreiras.
- Perfis que já atendem aos requisitos.
- Tratamento de entradas inválidas.
- Independência entre análises consecutivas.

Ao final dessa etapa, a bateria completa do projeto registrou **54 testes automatizados aprovados**.

## 8. Limitações

As competências e os níveis de referência Júnior são critérios definidos para fins acadêmicos.

O sistema depende das informações declaradas pelo usuário, sem realizar avaliações práticas de conhecimento.

Os planos de estudos são personalizados conforme as lacunas identificadas, mas não consideram automaticamente disponibilidade de tempo, orçamento ou oportunidades específicas de emprego.

As sugestões de certificações não substituem a consulta aos requisitos oficiais de cada instituição certificadora.

## 9. Conclusão

A implementação da análise de Skill Gaps e do Roadmap Personalizado permite complementar o ranking profissional com orientações práticas de desenvolvimento.

O sistema passa a identificar lacunas, priorizar competências, selecionar conteúdos de estudo e sugerir certificações e projetos de portfólio a partir das informações cadastradas em uma base de conhecimento externa.

Os módulos estão preparados para integração à interface Streamlit na próxima fase do desenvolvimento.