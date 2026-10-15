
# Questionário — Consultor Inteligente de Carreiras em TI

## Objetivo

Coletar informações sobre afinidades, conhecimentos,
preferências e objetivos profissionais para alimentar
o motor de inferência do sistema especialista.

As respostas serão utilizadas em conjunto, evitando
que uma única característica determine a recomendação.

## Bloco 1 — Identificação do Perfil

### Q01 — Afinidade matemática

Qual é seu nível de afinidade com matemática e estatística?

A) Baixo
B) Médio
C) Alto

### Q02 — Atividade profissional

Qual atividade você gostaria de realizar no dia a dia?

A) Desenvolver algoritmos e funcionalidades.
B) Criar interfaces e experiências visuais.
C) Analisar dados e identificar padrões.
D) Organizar e transformar grandes volumes de dados.
E) Configurar servidores e automatizar processos.
F) Investigar falhas, vulnerabilidades e riscos.
G) Planejar funcionalidades e prioridades de produtos.

### Q03 — Conhecimentos e ferramentas

Com qual tecnologia ou ferramenta você possui maior
familiaridade atualmente?

A) Python.
B) JavaScript, HTML e CSS.
C) Java ou C#.
D) SQL e bancos de dados.
E) Linux e redes.
F) Docker e ferramentas de CI/CD.
G) AWS, Azure ou Google Cloud.
H) Flutter, React Native ou desenvolvimento mobile.
I) Ferramentas de testes e automação.
J) Nenhuma — estou começando na área.

### Q04 — Entrega de valor

Qual resultado profissional você considera mais interessante?

A) Desenvolver soluções utilizadas pelas pessoas.
B) Proporcionar experiências visuais intuitivas.
C) Transformar dados em informações úteis.
D) Garantir infraestrutura estável e escalável.
E) Proteger sistemas e garantir sua qualidade.
F) Contribuir para decisões e resultados de negócio.

### Q05 — Ambiente de atuação

Em qual ambiente você gostaria de trabalhar?

A) Aplicações web e APIs.
B) Interfaces e aplicações móveis.
C) Plataformas e ambientes de dados.
D) Servidores, redes e infraestrutura em nuvem.
E) Processos de qualidade, segurança e automação.
F) Planejamento e gestão de produtos.


## Bloco 2 — Identificação de Especialidades

### Q06 — Trabalho com dados

Se fosse trabalhar com dados, qual atividade preferiria?

A) Analisar informações, identificar padrões e criar modelos preditivos.
B) Construir processos para coletar, transformar e disponibilizar dados.
C) Não tenho preferência por essas atividades.

### Q07 — Infraestrutura e operações

Qual atividade relacionada à infraestrutura desperta mais interesse?

A) Automatizar implantações, monitorar aplicações e melhorar sua confiabilidade.
B) Projetar ambientes em nuvem, dimensionar recursos e planejar arquiteturas.
C) Não tenho preferência por essas atividades.

### Q08 — Desenvolvimento de aplicações

Qual tipo de desenvolvimento você considera mais interessante?

A) Implementar APIs, regras de negócio e processamento de informações.
B) Criar interfaces web acessíveis, intuitivas e visualmente agradáveis.
C) Desenvolver aplicativos para smartphones e tablets.
D) Não tenho preferência por essas atividades.

### Q09 — Segurança e qualidade

Qual atividade você considera mais interessante?

A) Investigar vulnerabilidades e proteger sistemas contra ataques.
B) Identificar defeitos e automatizar testes para garantir a qualidade.
C) Não tenho preferência por essas atividades.

### Q10 — Participação em projetos

Em um projeto de tecnologia, qual responsabilidade você preferiria assumir?

A) Definir prioridades, compreender necessidades dos usuários e orientar o produto.
B) Implementar soluções técnicas a partir dos requisitos estabelecidos.
C) Participar das decisões de produto e também da implementação técnica.
D) Ainda não tenho uma preferência definida.


## Bloco 3 — Perguntas Complementares

As perguntas complementares são apresentadas somente
quando o sistema não consegue identificar uma carreira
predominante com as 10 perguntas iniciais.

### Q11 — Preferência entre carreiras

Qual destas áreas mais desperta seu interesse?

As alternativas são geradas dinamicamente, considerando
as carreiras que possuem evidências nas respostas iniciais.

### Q12 — Atividade profissional específica

Qual atividade você preferiria realizar?

As alternativas são definidas conforme a carreira
selecionada na Q11, apresentando duas atividades
representativas daquela especialidade.

## Funcionamento da Análise Complementar

1. O usuário responde às 10 perguntas iniciais.
2. O motor Experta realiza a análise profissional.
3. Se houver recomendação, o resultado é apresentado.
4. Caso contrário, o sistema identifica carreiras candidatas.
5. O usuário responde às perguntas Q11 e Q12.
6. A regra R26 verifica a coerência das novas respostas
   com as evidências coletadas anteriormente.
7. O sistema apresenta uma nova análise.

As perguntas complementares não substituem as respostas
originais e não garantem que uma recomendação seja possível.



## Observações

- Cada pergunta permite selecionar uma alternativa.
- Não existe resposta certa ou errada.
- Não é obrigatório possuir experiência prévia em TI.
- As respostas serão combinadas por regras de inferência.
- O questionário contém 10 perguntas organizadas em dois blocos.
- As perguntas Q06 a Q10 ajudam a diferenciar especialidades semelhantes.
- Respostas neutras não devem gerar recomendações artificiais.
- A recomendação final será determinada pela combinação das regras disparadas.

