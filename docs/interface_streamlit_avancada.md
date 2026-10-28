
# Interface Streamlit Avançada

## 1. Visão geral

A interface avançada do Consultor Inteligente de Carreiras em TI
foi desenvolvida com Streamlit para oferecer uma experiência
interativa de orientação profissional.

A aplicação integra o motor de inferência ponderado, a base de
conhecimento em JSON, a análise de competências e a geração
de roadmaps personalizados.

O ponto de entrada oficial da aplicação é `app.py`.

## 2. Estrutura do questionário

O questionário é organizado em três etapas:

### Etapa 1 — Perfil pessoal

Coleta informações sobre a situação profissional e o nível
de experiência do usuário.

Essas informações contextualizam o perfil, sem modificar
diretamente os percentuais de compatibilidade.

### Etapa 2 — Afinidades técnicas

Apresenta dez perguntas relacionadas às dimensões técnicas
utilizadas pelo motor de inferência.

Cada afinidade recebe um valor de 1 a 5:

- 1: nenhuma afinidade;
- 3: afinidade moderada;
- 5: afinidade muito alta.

As respostas são preservadas entre as etapas por meio do
`st.session_state`.

### Etapa 3 — Objetivos de carreira

Coleta o objetivo profissional principal e a prioridade
de desenvolvimento do usuário.

Os objetivos contextualizam a orientação profissional,
sem alterar os pesos de compatibilidade definidos no JSON.

## 3. Análise de compatibilidade

Após o preenchimento do questionário, o usuário pode
selecionar o botão "Analisar meu perfil".

A aplicação utiliza o `MotorPonderado`, implementado em
`src/motor_ponderado.py`, para calcular a compatibilidade
com as dez carreiras da base de conhecimento.

O cálculo considera:

- Afinidades informadas pelo usuário;
- Pesos de cada carreira;
- Bônus e penalidades definidos nas regras ponderadas;
- Limitação do resultado final ao intervalo de 0% a 100%.

A interface apresenta:

- Ranking das três carreiras mais compatíveis;
- Percentuais de compatibilidade;
- Pontuação-base e ajustes aplicados;
- Regras acionadas e justificativas;
- Diagnóstico profissional.

Os diagnósticos possíveis são:

- Predominante;
- Multifacetado;
- Inconclusivo.

Os critérios e limites utilizados estão definidos na
base de conhecimento externa.

## 4. Visualização dos resultados

A aplicação utiliza um gráfico de barras horizontais para
comparar a compatibilidade com as dez carreiras.

O gráfico é apresentado em ordem decrescente de
compatibilidade e utiliza a identidade visual da aplicação.

Os percentuais indicam compatibilidade com os critérios
do sistema, e não probabilidades de sucesso profissional.

## 5. Avaliação de competências

Após visualizar o ranking, o usuário pode selecionar uma
das três carreiras recomendadas.

A aplicação consulta os requisitos de nível Júnior
definidos no JSON e apresenta as competências correspondentes.

Cada conhecimento atual é avaliado de 0 a 5:

- 0: nenhum conhecimento;
- 5: domínio elevado.

O preenchimento completo das competências é necessário
para liberar a geração do roadmap.

## 6. Análise de Skill Gaps

O módulo `src/analise_gaps.py` compara os conhecimentos
informados com os requisitos Júnior da carreira escolhida.

São identificados:

- Competências atendidas;
- Competências com lacunas;
- Diferença entre o nível atual e o nível requerido;
- Percentual de cobertura dos requisitos.

As lacunas são priorizadas conforme os critérios
implementados no módulo de análise.

## 7. Roadmap Personalizado

O módulo `src/roadmap.py` utiliza a análise de gaps e
os dados da base de conhecimento para gerar recomendações
de desenvolvimento profissional.

O roadmap apresenta:

- Estudos prioritários para as competências com lacunas;
- Recomendações de tecnologias e conhecimentos;
- Certificações opcionais, quando pertinentes;
- Projeto de portfólio relacionado à carreira;
- Resumo da cobertura dos requisitos Júnior.

As recomendações são derivadas da base JSON, evitando
a inclusão de conteúdos arbitrários na interface.

## 8. Gerenciamento de estado

O `st.session_state` é utilizado para preservar as respostas
durante a navegação entre as etapas.

Quando o usuário altera uma afinidade ou um objetivo,
a análise anterior é invalidada.

Ao alterar a carreira selecionada, os conhecimentos
avaliados e o roadmap anterior são reiniciados.

Quando um nível de conhecimento é modificado, o roadmap
deve ser gerado novamente.

Esses mecanismos reduzem o risco de apresentar resultados
desatualizados.

## 9. Identidade visual

A interface utiliza o arquivo `assets/estilo.css`.

A identidade visual combina:

- Fundo em tons de azul-marinho;
- Destaques em ciano;
- Botões e elementos de destaque em dourado;
- Layout centralizado;
- Indicadores de progresso;
- Mensagens de orientação e confirmação.

## 10. Execução

A partir da raiz do projeto, com o ambiente virtual
configurado e as dependências instaladas:

```powershell
python -m streamlit run app.py
```

## 11. Testes

A execução dos testes automatizados pode ser realizada com:

```powershell
python -m unittest discover -s tests -v
```

O conjunto de testes abrange os componentes da base de
conhecimento, motor ponderado, diagnóstico, análise de gaps
e geração de roadmaps.

A interface também deve ser validada manualmente, incluindo
navegação, persistência de respostas, cálculo de compatibilidade
e geração do roadmap.

## 12. Organização do código

Os principais componentes são:

- `app.py`: interface Streamlit;
- `assets/estilo.css`: identidade visual;
- `dados/regras_carreiras.json`: base de conhecimento;
- `src/base_conhecimento.py`: carregamento e validação do JSON;
- `src/motor_ponderado.py`: cálculo de compatibilidade;
- `src/analise_gaps.py`: comparação de competências;
- `src/roadmap.py`: geração do plano de desenvolvimento;
- `tests/`: testes automatizados.

A interface atua como camada de apresentação, reutilizando
os módulos responsáveis pelas regras e pelos cálculos.
