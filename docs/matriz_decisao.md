
# Matriz de Decisão — Carreiras em TI

## Objetivo

Relacionar as respostas do questionário às 10 trilhas
profissionais, estabelecendo a base de conhecimento
utilizada pelo motor de inferência Experta.

A recomendação deverá considerar a combinação de
múltiplas respostas, evitando decisões baseadas em
características isoladas.

## 1. Critérios de Avaliação

As respostas serão classificadas conforme sua relevância:

- Sinal principal: indica preferência diretamente
  relacionada às atividades de determinada carreira.
- Sinal complementar: reforça uma preferência já identificada.
- Resposta neutra: não favorece diretamente nenhuma carreira.

As regras definitivas serão construídas posteriormente,
considerando o cruzamento desses sinais.

## 2. Matriz de Sinais Principais

| Carreira | Pergunta | Resposta |
|---|---|---|
| Back-end | Q08 | A |
| Front-end & UI/UX | Q08 | B |
| Ciência de Dados e ML | Q06 | A |
| Engenharia de Dados | Q06 | B |
| Cibersegurança | Q09 | A |
| DevOps & SRE | Q07 | A |
| Computação em Nuvem | Q07 | B |
| Desenvolvimento Mobile | Q08 | C |
| Engenharia de Qualidade (QA) | Q09 | B |
| Gestão de Produtos | Q10 | A |

## 3. Tratamento das Respostas Neutras

As seguintes alternativas não deverão favorecer
diretamente nenhuma carreira:

- Q06-C: sem preferência por atividades de dados.
- Q07-C: sem preferência por infraestrutura.
- Q08-D: sem preferência por desenvolvimento.
- Q09-C: sem preferência por segurança ou qualidade.
- Q10-D: preferência ainda não definida.

As alternativas Q10-B e Q10-C também não determinarão
uma carreira isoladamente, pois representam interesses
que podem estar presentes em diferentes especialidades.

## 4. Regras Gerais

1. Nenhuma carreira será definida por uma única resposta.
2. Sinais principais deverão ser cruzados com outros critérios.
3. Respostas complementares poderão reforçar recomendações.
4. Respostas neutras não deverão gerar evidências artificiais.
5. Perfis com interesses múltiplos deverão ser avaliados
   por critérios de desempate definidos posteriormente.
6. O sistema deverá justificar a recomendação utilizando
   as regras que contribuíram para o resultado.


## 5. Matriz de Sinais Complementares

Os sinais complementares representam características que
reforçam a afinidade do usuário com determinada carreira.

Uma mesma resposta pode favorecer diferentes trilhas,
pois existem conhecimentos e atividades compartilhados
entre as áreas de Tecnologia da Informação.

### 5.1. Mapeamento das Respostas

| Carreira | Q01 | Q02 | Q03 | Q04 | Q05 |
|---|---|---|---|---|---|
| Back-end | — | A | A, C, D | A | A |
| Front-end & UI/UX | — | B | B | B | B |
| Ciência de Dados e ML | C | C | A, D | C | C |
| Engenharia de Dados | — | D | A, D | C | C |
| Cibersegurança | — | F | E | E | E |
| DevOps & SRE | — | E | E, F | D | D, E |
| Computação em Nuvem | — | E | E, G | D | D |
| Desenvolvimento Mobile | — | A, B | H | A | B |
| Engenharia de Qualidade (QA) | — | F | I | E | E |
| Gestão de Produtos | — | G | — | F | F |

### 5.2. Interpretação da Matriz

- Q01: afinidade matemática e estatística.
- Q02: preferência de atividade profissional.
- Q03: conhecimentos e ferramentas.
- Q04: tipo de entrega de valor.
- Q05: ambiente de atuação.
- A, B, C etc.: alternativas do questionário.
- O símbolo "—" indica ausência de evidência específica.

### 5.3. Critérios de Interpretação

1. Respostas complementares não determinam uma carreira
   isoladamente.

2. Uma resposta pode favorecer múltiplas carreiras.

3. A afinidade matemática alta (Q01-C) reforça Ciência
   de Dados, mas não garante essa recomendação.

4. Afinidade matemática baixa ou média não elimina
   nenhuma carreira.

5. A resposta Q03-J (nenhuma ferramenta conhecida)
   será considerada neutra, sem prejudicar iniciantes.

6. As perguntas Q06 a Q10 fornecerão sinais principais,
   enquanto Q01 a Q05 reforçarão as recomendações.

7. A combinação dos sinais deverá ser avaliada antes
   de determinar a carreira mais adequada.


## 6. Sistema de Pontuação

A recomendação será baseada nas evidências identificadas
pelas regras do motor de inferência.

### 6.1. Pesos das Evidências

| Evidência | Pontuação |
|---|---|
| Sinal principal (Q06 a Q10) | +3 pontos |
| Sinal complementar (Q01 a Q05) | +1 ponto |
| Resposta neutra | 0 pontos |

Cada resposta poderá contribuir para diferentes carreiras
conforme o mapeamento estabelecido anteriormente.

Uma mesma resposta não poderá pontuar duas vezes para
a mesma carreira dentro de uma mesma pergunta.

### 6.2. Cálculo da Pontuação

Pontuação final = (3 × sinais principais)
                + (1 × sinais complementares)

A pontuação será calculada individualmente para cada
uma das 10 carreiras.


### 6.3. Critérios de Prioridade

1. O motor Experta avaliará as regras de identificação
   profissional (R01 a R20).

2. Uma carreira somente será elegível para recomendação
   quando pelo menos uma regra de identificação
   correspondente for disparada.

3. Para cada carreira elegível, a pontuação será
   calculada conforme os sinais principais e
   complementares identificados na matriz.

4. Cada resposta poderá pontuar apenas uma vez
   para a mesma carreira, independentemente da
   quantidade de regras disparadas.

5. A carreira elegível com maior pontuação será
   recomendada, respeitando os critérios de desempate.

6. As regras R21 a R25 fornecerão justificativas
   adicionais, sem acrescentar pontos à pontuação.

7. Caso nenhuma regra de identificação seja disparada,
   o sistema solicitará informações adicionais
   antes de apresentar uma recomendação.

## 7. Tratamento de Empates

Quando duas ou mais carreiras apresentarem a mesma
pontuação, aplicar os seguintes critérios:

1. Priorizar a carreira com maior quantidade de
   sinais principais.

2. Persistindo o empate, considerar a compatibilidade
   com a atividade profissional escolhida em Q02.

3. Em seguida, considerar a familiaridade com as
   ferramentas e tecnologias indicadas em Q03.

4. Se o empate continuar, realizar uma pergunta
   adicional direcionada às carreiras empatadas.

A entrevista não deverá ser finalizada com uma escolha
arbitrária entre carreiras indistinguíveis.

## 8. Justificativa da Recomendação

O sistema deverá apresentar:

- Nome da carreira recomendada.
- Pontuação obtida pela carreira.
- Respostas que contribuíram para a recomendação.
- Principais regras de inferência acionadas.
- Indicação de baixa confiança quando as evidências
  forem insuficientes ou pouco diferenciadas.

A pontuação não representa uma probabilidade
estatística de sucesso profissional.

## 9. Integração com o Motor de Inferência

As regras da Experta serão responsáveis por identificar
as evidências presentes nas respostas do usuário.

Cada regra acionada poderá registrar:

- Carreira favorecida.
- Identificador da regra.
- Pontuação atribuída.
- Justificativa da evidência identificada.

Ao término da inferência, as pontuações serão consolidadas
para determinar a recomendação final.

O conjunto de regras será planejado na próxima etapa.


## 10. Catálogo de Regras de Inferência

As regras serão implementadas utilizando a biblioteca
Experta e sua estrutura de inferência SE-ENTÃO.

Cada regra combinará duas ou mais respostas.

### 10.1. Regras de Identificação Profissional

| ID | Condições (SE) | Carreira favorecida (ENTÃO) |
|---|---|---|
| R01 | Q08=A e Q02=A | Back-end |
| R02 | Q08=A e Q03=A/C/D | Back-end |
| R03 | Q08=B e Q02=B | Front-end & UI/UX |
| R04 | Q08=B e Q03=B | Front-end & UI/UX |
| R05 | Q06=A e Q01=C | Ciência de Dados e ML |
| R06 | Q06=A e Q02=C | Ciência de Dados e ML |
| R07 | Q06=B e Q02=D | Engenharia de Dados |
| R08 | Q06=B e Q03=D | Engenharia de Dados |
| R09 | Q09=A e Q02=F | Cibersegurança |
| R10 | Q09=A e Q03=E | Cibersegurança |
| R11 | Q07=A e Q03=F | DevOps & SRE |
| R12 | Q07=A e Q02=E | DevOps & SRE |
| R13 | Q07=B e Q03=G | Computação em Nuvem |
| R14 | Q07=B e Q05=D | Computação em Nuvem |
| R15 | Q08=C e Q03=H | Desenvolvimento Mobile |
| R16 | Q08=C e Q05=B | Desenvolvimento Mobile |
| R17 | Q09=B e Q03=I | Engenharia de Qualidade (QA) |
| R18 | Q09=B e Q04=E | Engenharia de Qualidade (QA) |
| R19 | Q10=A e Q02=G | Gestão de Produtos |
| R20 | Q10=A e Q04=F | Gestão de Produtos |

### 10.2. Regras de Diferenciação

As regras seguintes identificam evidências mais
específicas em perfis com características compartilhadas.

| ID | Condições (SE) | Diferenciação (ENTÃO) |
|---|---|---|
| R21 | Q06=A, Q01=C e Q03=D | Ciência de Dados frente à Engenharia de Dados |
| R22 | Q06=B, Q02=D e Q03=A | Engenharia de Dados frente à Ciência de Dados |
| R23 | Q07=A, Q03=G e Q02=E | DevOps frente à Computação em Nuvem |
| R24 | Q07=B, Q03=F e Q04=D | Computação em Nuvem frente a DevOps |
| R25 | Q09=B, Q02=F e Q03=I | QA frente à Cibersegurança |

### 10.3. Critérios de Execução

1. Todas as regras serão avaliadas pelo motor Experta.

2. Cada regra disparada registrará seu identificador,
   a carreira favorecida e uma justificativa.

3. A pontuação seguirá os pesos definidos na seção 6:
   +3 por sinal principal e +1 por sinal complementar.

4. O disparo de múltiplas regras não duplicará pontos
   de uma mesma resposta para a mesma carreira.

5. As regras R21 a R25 registrarão justificativas
   adicionais, sem acrescentar pontos extras.

6. As regras não excluirão automaticamente outras
   carreiras que também apresentem evidências.

7. Quando nenhuma regra de identificação for disparada,
   o sistema solicitará informações complementares
   antes de finalizar o diagnóstico.

8. A recomendação será definida pela consolidação
   das evidências e pelos critérios de desempate.

## 11. Considerações sobre a Inferência

O sistema utilizará regras cruzadas para reconhecer
características profissionais e gerar justificativas.

A base de conhecimento poderá ser revisada caso os
testes com personas revelem ambiguidades ou resultados
inconsistentes.

O catálogo contém 25 regras planejadas, atendendo à
quantidade estabelecida no enunciado da atividade.


## 12. Validação Lógica Preliminar

Esta etapa verifica manualmente se os critérios da
matriz produzem recomendações coerentes para
diferentes perfis profissionais.

Os resultados representam expectativas teóricas,
que serão confirmadas posteriormente com testes
automatizados do motor de inferência.

### Persona 1 — Perfil Analítico

Respostas:
Q01=C, Q02=C, Q03=A, Q04=C, Q05=C
Q06=A, Q07=C, Q08=D, Q09=C, Q10=D

Resultado esperado:
- Carreira: Ciência de Dados e Machine Learning
- Pontuação: 8 pontos
- Regras identificadas: R05 e R06

### Persona 2 — Perfil de Segurança

Respostas:
Q01=B, Q02=F, Q03=E, Q04=E, Q05=E
Q06=C, Q07=C, Q08=D, Q09=A, Q10=D

Resultado esperado:
- Carreira: Cibersegurança
- Pontuação: 7 pontos
- Regras identificadas: R09 e R10

### Persona 3 — Perfil Visual

Respostas:
Q01=A, Q02=B, Q03=B, Q04=B, Q05=B
Q06=C, Q07=C, Q08=B, Q09=C, Q10=D

Resultado esperado:
- Carreira: Desenvolvimento Front-end & UI/UX
- Pontuação: 7 pontos
- Regras identificadas: R03 e R04

### Persona 4 — Perfil de Negócios

Respostas:
Q01=B, Q02=G, Q03=J, Q04=F, Q05=F
Q06=C, Q07=C, Q08=D, Q09=C, Q10=A

Resultado esperado:
- Carreira: Gestão de Produtos
- Pontuação: 6 pontos
- Regras identificadas: R19 e R20

### Persona 5 — Perfil Indefinido

Respostas:
Q01=B, Q02=G, Q03=J, Q04=A, Q05=A
Q06=C, Q07=C, Q08=D, Q09=C, Q10=D

Resultado esperado:
- Nenhuma carreira recomendada imediatamente.
- Nenhuma regra de identificação disparada.
- Sistema solicita informações adicionais.

## 13. Conclusão da Validação Preliminar

Os cenários foram definidos para verificar:

1. Identificação de perfis profissionais distintos.
2. Coerência entre respostas e regras planejadas.
3. Aplicação dos pesos de pontuação.
4. Comportamento diante de evidências insuficientes.

A validação completa ocorrerá após a implementação
do motor de inferência, incluindo casos de empate
e perfis com interesses profissionais mistos.



## 14. Extensão da Base de Conhecimento — Regra R26

Durante a validação da interface, foi identificada a
necessidade de tratar questionários completos que não
produzem uma recomendação conclusiva.

Para isso, foi implementada uma etapa complementar
de entrevista utilizando as perguntas Q11 e Q12.

### 14.1. Regra Complementar

| Regra | Condições | Resultado |
|---|---|---|
| R26 | Q11 identifica uma carreira candidata, Q12 confirma uma atividade correspondente e existe evidência anterior favorável | Registra evidência complementar para a carreira |

A regra R26 utiliza os recursos MATCH e TEST da Experta
para verificar a combinação das respostas.

### 14.2. Pontuação Complementar

Quando a análise inicial não produz uma recomendação
e a regra R26 é acionada, são considerados:

- Q11: +3 pontos pela preferência profissional.
- Q12: +1 ponto pela atividade específica.
- Evidências anteriores: pontuação já calculada.

A recomendação complementar utiliza a pontuação
original da carreira, acrescida de 4 pontos.

### 14.3. Critérios de Segurança da Recomendação

- A regra R26 exige evidência anterior favorável.
- A escolha da carreira não pode ser completamente
  desconectada do questionário inicial.
- A análise complementar não modifica as regras R01-R25.
- A pontuação não representa probabilidade estatística.
- Caso não existam evidências suficientes, o sistema
  poderá permanecer sem recomendação.

### 14.4. Validação

Foram implementados testes automatizados para:

1. Identificação das carreiras candidatas.
2. Recomendação utilizando Q11, Q12 e R26.
3. Ausência de recomendação sem confirmação complementar.

A base de conhecimento passa a contar com 26 regras,
sendo 20 de identificação profissional, 5 de
diferenciação e 1 de confirmação complementar.

