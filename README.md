# Consultor Inteligente de Carreiras em TI

Sistema especialista desenvolvido em Python para recomendar carreiras na área de Tecnologia da Informação, utilizando regras de inferência e respostas fornecidas pelo usuário.

O projeto foi desenvolvido como atividade acadêmica da disciplina de Inteligência Artificial, com o objetivo de aplicar conceitos de sistemas especialistas, representação do conhecimento e inferência baseada em regras.

## 1. Objetivo

Auxiliar pessoas interessadas em Tecnologia da Informação a identificar carreiras compatíveis com suas habilidades, interesses e preferências profissionais.

A aplicação apresenta um questionário interativo, processa as respostas por meio de um motor de inferência e exibe uma recomendação acompanhada de pontuação e justificativas.

## 2. Carreiras contempladas

O sistema considera dez especialidades:

1. Back-end
2. Front-end & UI/UX
3. Ciência de Dados e Machine Learning
4. Engenharia de Dados
5. Cibersegurança
6. DevOps & SRE
7. Computação em Nuvem
8. Desenvolvimento Mobile
9. Engenharia de Qualidade (QA)
10. Gestão de Produtos

## 3. Tecnologias utilizadas

- **Python 3.11:** linguagem principal do projeto.
- **Experta:** implementação do sistema especialista e das regras de inferência.
- **Streamlit:** desenvolvimento da interface web interativa.
- **unittest:** implementação e execução dos testes automatizados.
- **Git e GitHub:** versionamento e organização do desenvolvimento.

## 4. Funcionamento do sistema

O usuário responde a um questionário com dez perguntas obrigatórias, relacionadas a conhecimentos técnicos, interesses e preferências profissionais.

As respostas são convertidas em fatos analisados pelo motor de inferência Experta.

A base de conhecimento contém **26 regras**, organizadas em:

- **R01–R20:** identificação de afinidades com as dez carreiras.
- **R21–R25:** diferenciação e análise complementar das evidências.
- **R26:** confirmação de afinidade por meio de perguntas complementares.

O sistema também utiliza uma matriz de pontuação e critérios de desempate para selecionar a carreira predominante.

Quando não existem evidências suficientes para uma recomendação conclusiva, a aplicação pode apresentar duas perguntas adicionais:

- **Q11:** preferência entre carreiras candidatas.
- **Q12:** atividade profissional específica relacionada à carreira escolhida.

As novas respostas são verificadas em conjunto com as evidências anteriores.

A recomendação final apresenta a carreira identificada, sua pontuação de compatibilidade e as regras que fundamentaram a conclusão.

**Observação:** a pontuação representa compatibilidade segundo os critérios da base de conhecimento, não uma probabilidade estatística nem uma avaliação profissional definitiva.

## 5. Instalação

### Pré-requisitos

- Python 3.11
- pip
- Git (para clonar o repositório)

### Preparação do ambiente

Após obter o projeto, abra um terminal na pasta raiz e execute os comandos abaixo.

**1. Criar o ambiente virtual:**

`python -m venv .venv`

**2. Ativar o ambiente virtual (Windows PowerShell):**

`.\.venv\Scripts\Activate.ps1`

**3. Instalar as dependências:**

`python -m pip install -r requirements.txt`

## 6. Executar a aplicação

Com o ambiente virtual ativado, execute:

`python -m streamlit run app.py`

O Streamlit disponibilizará o endereço local da aplicação no terminal, normalmente `http://localhost:8501`.

Abra o endereço no navegador para acessar o questionário.

## 7. Testes automatizados

O projeto utiliza o framework `unittest` para verificar o funcionamento do motor de inferência, das regras, das recomendações e dos cenários de validação.

Para executar todos os testes:

`python -m unittest discover -s tests -v`

Na conclusão da Fase 4, a bateria de testes registrou **17 testes aprovados**.

Também foram realizados testes manuais pela interface, contemplando quatro personas profissionais e um cenário de respostas ambíguas.

Os resultados estão documentados em `docs/validacao_personas.md`.

## 8. Estrutura do projeto

| Diretório ou arquivo | Finalidade |
|---|---|
| `app.py` | Interface principal desenvolvida em Streamlit |
| `src/fatos.py` | Definição dos fatos utilizados pelo motor |
| `src/motor_inferencia.py` | Regras e execução da inferência |
| `src/pontuacao.py` | Cálculo das pontuações |
| `src/recomendacao.py` | Seleção e desempate das recomendações |
| `src/complementares.py` | Tratamento das perguntas complementares |
| `src/compatibilidade.py` | Compatibilidade de dependências |
| `assets/estilo.css` | Estilização da interface |
| `.streamlit/config.toml` | Configurações do Streamlit |
| `tests/` | Testes automatizados |
| `docs/` | Documentação técnica e resultados de validação |
| `requirements.txt` | Dependências do projeto |

## 9. Documentação complementar

A pasta `docs/` reúne os materiais produzidos durante o desenvolvimento:

- `arquitetura.md` — organização e arquitetura do sistema.
- `perfis_carreiras.md` — características das carreiras contempladas.
- `questionario.md` — perguntas e alternativas do questionário.
- `matriz_decisao.md` — matriz de pontuação e regras de inferência.
- `validacao_personas.md` — cenários e resultados da validação.

## 10. Considerações finais

O projeto demonstra a aplicação prática de técnicas de Inteligência Artificial simbólica na orientação de carreiras em TI.

A combinação de regras explícitas, pontuação de compatibilidade e justificativas permite apresentar recomendações transparentes e rastreáveis.

O sistema tem finalidade acadêmica e informativa, não substituindo processos completos de orientação profissional.