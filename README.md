# Consultor Inteligente de Carreiras em TI

**Trabalho da Etapa 2 — Inteligência Artificial**

Sistema especialista acadêmico de orientação profissional em Tecnologia da Informação. Desenvolvido em Python com interface Streamlit, utiliza uma **base de conhecimento externa em JSON** e um **motor de inferência ponderado** para analisar afinidades técnicas, recomendar carreiras e propor planos de desenvolvimento baseados em lacunas de competências (*skill gaps*).

Esta versão evolui o projeto original da AECO, preservado separadamente, e amplia o diagnóstico para incluir **ranking Top 3**, comparação entre dez carreiras, avaliação de requisitos de nível Júnior e **roadmap personalizado**.

## 1. Objetivo

Apoiar pessoas que desejam conhecer ou desenvolver uma carreira em TI por meio de recomendações explicáveis e critérios explícitos. O sistema:

- avalia afinidades técnicas em uma escala de 1 a 5;
- calcula percentuais de compatibilidade com dez trilhas profissionais;
- apresenta três recomendações com justificativas e um gráfico comparativo;
- identifica competências que precisam ser desenvolvidas para o nível Júnior da carreira escolhida;
- sugere estudos prioritários, certificações opcionais e um projeto de portfólio.

**Importante:** os percentuais indicam compatibilidade com o modelo de regras adotado. Não representam probabilidades de sucesso ou uma avaliação profissional definitiva.

## 2. Carreiras contempladas

1. Desenvolvimento Back-end
2. Front-end & UI/UX
3. Ciência de Dados e Machine Learning
4. Engenharia de Dados
5. Cibersegurança
6. DevOps & SRE
7. Cloud Architecture
8. Desenvolvimento Mobile
9. Engenharia de Qualidade (QA)
10. Gestão de Produtos

## 3. Tecnologias

- **Python 3.11:** implementação do sistema.
- **Streamlit:** interface web, questionário em etapas, gráficos e apresentação dos resultados.
- **JSON:** armazenamento externo das carreiras, pesos, regras, requisitos e sugestões de desenvolvimento.
- **`unittest`:** testes automatizados.
- **Git e GitHub:** versionamento do projeto.
- **Experta:** biblioteca utilizada no motor de inferência do projeto original, mantido no repositório como referência histórica. **O fluxo principal desta versão utiliza `MotorPonderado`, não Experta.**

As dependências instaláveis estão declaradas em `requirements.txt`.

## 4. Funcionamento da aplicação

A interface oficial é executada pelo arquivo `app.py` e apresenta um questionário em três etapas.

### Etapa 1 — Perfil pessoal

O usuário informa sua situação profissional e experiência com tecnologia. Esses dados contextualizam a experiência de orientação e **não modificam os pesos do motor ponderado**.

### Etapa 2 — Afinidades técnicas

O usuário avalia dez dimensões de interesse técnico, com valores inteiros de **1 a 5**:

- **1:** nenhuma afinidade;
- **3:** afinidade moderada;
- **5:** afinidade muito alta.

As perguntas e as dimensões são carregadas da base de conhecimento em JSON.

### Etapa 3 — Objetivos de carreira

O usuário seleciona seu objetivo profissional e seu foco de desenvolvimento. Essas respostas contextualizam a orientação, mas **não alteram o cálculo dos percentuais**.

Ao selecionar **Analisar meu perfil**, a interface consulta o motor ponderado e apresenta:

- diagnóstico do perfil: **predominante, multifacetado ou inconclusivo**;
- **Top 3** com percentuais de compatibilidade;
- pontuação-base, ajustes de regras e justificativas;
- gráfico de barras horizontais comparando as dez carreiras.

Em seguida, o usuário pode selecionar uma das três carreiras recomendadas, avaliar suas competências e gerar o roadmap.

## 5. Motor de compatibilidade ponderada

O módulo `src/motor_ponderado.py` utiliza os pesos e regras definidos em `dados/regras_carreiras.json`.

Para cada carreira, o percentual-base é calculado pela expressão:

```text
compatibilidade_base = 100 × Σ[peso × (afinidade − 1)] / (4 × Σ[pesos])
```

Depois são aplicados bônus e penalidades das regras cujas condições forem satisfeitas. O percentual final é limitado ao intervalo **0% a 100%**.

O ranking é ordenado por percentual final decrescente, seguido de pontuação-base e identificador da carreira, para assegurar desempates determinísticos.

A base de conhecimento contém **20 regras ponderadas (RP01 a RP20)**: dez regras de bônus e dez de penalidade.

### Classificação do perfil

Os limites são configuráveis na própria base JSON. Na configuração atual:

- **Inconclusivo:** maior compatibilidade inferior a 55%.
- **Multifacetado:** maior compatibilidade de pelo menos 55%, com diferença entre primeiro e segundo colocados de até 10 pontos percentuais.
- **Predominante:** maior compatibilidade de pelo menos 55%, com diferença superior a 10 pontos percentuais.

Esses critérios descrevem o funcionamento do modelo acadêmico, não limiares estatísticos validados externamente.

## 6. Skill gaps e roadmap personalizado

Após selecionar uma carreira do Top 3, o usuário informa seu nível atual de conhecimento em cada competência exigida para o nível **Júnior**, em escala de **0 a 5**. A resposta 0 significa nenhum conhecimento; campos ainda não respondidos não são tratados automaticamente como 0.

O módulo `src/analise_gaps.py` compara cada nível informado com o requisito definido no JSON. A lacuna de uma competência é:

```text
gap = máximo(0, nível_júnior − nível_atual)
```

A **cobertura dos requisitos** é a proporção entre a soma dos níveis atendidos (limitados a seus requisitos) e a soma dos níveis Júnior exigidos, expressa em percentual.

O módulo `src/roadmap.py` organiza a orientação em função das lacunas identificadas:

- estudos prioritários para competências abaixo do nível exigido;
- conteúdos e tecnologias associados a essas competências;
- certificações **opcionais**, quando relacionadas às lacunas;
- proposta de projeto de portfólio para aplicar os conhecimentos;
- resumo de cobertura e quantidade de lacunas.

O sistema utiliza os dados cadastrados na base JSON; não gera cursos, certificações ou projetos por meio de um modelo generativo.

## 7. Base de conhecimento externa

O arquivo `dados/regras_carreiras.json` reúne:

- dez dimensões e perguntas de afinidade;
- dez carreiras e seus pesos;
- regras de bônus e penalidade;
- limites para diagnóstico de perfis;
- catálogo de competências e requisitos Júnior;
- conteúdos de estudo, certificações e projetos de portfólio.

O módulo `src/base_conhecimento.py` carrega e valida a estrutura e as referências internas do arquivo. Alterações válidas nesse JSON podem modificar regras, limites e recomendações **sem reescrever os cálculos da interface**.

## 8. Instalação

### Pré-requisitos

- Python 3.11;
- `pip`;
- Git, caso deseje clonar o repositório.

Na pasta raiz do projeto, execute os comandos abaixo.

**Criar o ambiente virtual:**

```powershell
python -m venv .venv
```

**Ativar no Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Instalar as dependências:**

```powershell
python -m pip install -r requirements.txt
```

## 9. Executar a aplicação

Com o ambiente configurado:

```powershell
python -m streamlit run app.py
```

O terminal exibirá o endereço local da interface, normalmente `http://localhost:8501`.

## 10. Testes e validação

Execute a suíte de testes automatizados:

```powershell
python -m unittest discover -s tests -v
```

Também é possível verificar a integridade das dependências instaladas:

```powershell
python -m pip check
```

**Status da validação local desta etapa:** 54 testes automatizados aprovados, conforme execução realizada durante o desenvolvimento.

Os testes contemplam carregamento e integridade da base, cálculo ponderado, regras de ajuste, classificação de perfis, casos ambíguos, análise de competências e geração de roadmaps. O fluxo visual foi validado manualmente, incluindo navegação, persistência das respostas, gráfico, seleção de carreira e geração do roadmap.

## 11. Estrutura principal do projeto

```text
.
├── app.py                          # Interface oficial Streamlit
├── assets/
│   └── estilo.css                  # Estilização da interface
├── dados/
│   └── regras_carreiras.json       # Base externa de conhecimento
├── src/
│   ├── base_conhecimento.py        # Carregamento e validação do JSON
│   ├── motor_ponderado.py          # Cálculo do ranking e diagnóstico
│   ├── analise_gaps.py             # Comparação com requisitos Júnior
│   └── roadmap.py                  # Plano de desenvolvimento
├── tests/                          # Testes automatizados
├── docs/                           # Documentação técnica
└── requirements.txt                # Dependências
```

Outros módulos da versão original da AECO continuam no repositório como referência, mas não fazem parte do fluxo principal de análise ponderada.

## 12. Documentação complementar

Os detalhes de modelagem, implementação e validação estão documentados em:

- `docs/modelagem_base_conhecimento.md` — estrutura e integridade dos dados externos;
- `docs/motor_ponderado.md` — pontuação, regras, ranking e diagnóstico;
- `docs/skill_gaps_roadmap.md` — avaliação de competências e geração do plano de desenvolvimento;
- `docs/interface_streamlit_avancada.md` — questionário, apresentação dos resultados e gerenciamento de estado.

O repositório também preserva a documentação das etapas e da versão AECO que originou este trabalho.

## 13. Limitações e finalidade

O sistema é **acadêmico e orientativo**. Suas recomendações são determinadas pelas perguntas, pesos, regras, competências e conteúdos cadastrados. Não substitui orientação profissional individualizada, não comprova proficiência técnica e não garante contratação ou êxito em determinada área.

Os dados pessoais e os objetivos profissionais são utilizados para contextualizar a experiência; na implementação atual, o cálculo ponderado depende das afinidades técnicas, e o roadmap depende dos conhecimentos declarados e dos requisitos da carreira escolhida.
