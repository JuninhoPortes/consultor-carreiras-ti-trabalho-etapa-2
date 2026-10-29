# Fase 5 — Validação de robustez e casos-limite

## 1. Objetivo

Registrar a validação do motor de inferência ponderado e da geração de roadmaps do **Consultor Inteligente de Carreiras em TI**, especialmente em situações ambíguas, valores-limite e perfis extremos, conforme o escopo da Fase 5 do trabalho acadêmico.

Os cenários desta fase complementam os testes já existentes para a base de conhecimento, o ranking Top 3, as regras de bônus e penalidade, o diagnóstico de perfis e a análise de lacunas de competências.

## 2. Critérios verificados

A base de conhecimento externa estabelece os seguintes critérios de diagnóstico:

- **Inconclusivo:** maior compatibilidade inferior a 55%.
- **Multifacetado:** maior compatibilidade de pelo menos 55% e diferença entre a primeira e a segunda carreiras de até 10 pontos percentuais, inclusive.
- **Predominante:** maior compatibilidade de pelo menos 55% e diferença superior a 10 pontos percentuais.

Os resultados de compatibilidade permanecem limitados ao intervalo de **0% a 100%**. A cobertura dos requisitos Júnior também não ultrapassa 100%, mesmo quando o nível informado é superior ao exigido.

## 3. Novos cenários automatizados

Os sete casos abaixo estão implementados em `tests/test_robustez.py`.

| Teste | Entrada / condição | Comportamento esperado |
|---|---|---|
| `test_limite_inclusivo_de_dez_pontos` | Duas compatibilidades simuladas de 55% e 45% | Perfil **multifacetado**; diferença de 10,00 p.p. |
| `test_diferenca_acima_de_dez_pontos` | Duas compatibilidades simuladas de 55% e 44,99% | Perfil **predominante**; diferença de 10,01 p.p. |
| `test_abaixo_do_minimo_mesmo_em_empate` | Duas compatibilidades simuladas de 54,99% | Perfil **inconclusivo**, apesar do empate |
| `test_todas_afinidades_no_minimo` | Todas as dez afinidades iguais a 1 | Dez resultados de 0%; diagnóstico inconclusivo |
| `test_todas_afinidades_no_maximo` | Todas as dez afinidades iguais a 5 | Dez resultados limitados a 100%; diagnóstico multifacetado |
| `test_fluxo_completo_do_perfil_backend` | Lógica e Back-end com afinidade 5; demais dimensões com 1; competências Júnior informadas | Back-end em 1º com 59,56%, RP01, cobertura Júnior de 60% e lacunas em APIs REST e SQL |
| `test_roadmap_sem_lacunas_mesmo_acima_do_junior` | Todas as competências Back-end informadas com nível 5 | Cobertura de 100%, nenhuma lacuna, nenhum estudo pendente e sugestão de portfólio preservada |

**Nota metodológica:** os três primeiros testes utilizam rankings simulados para isolar os valores-limite do método de diagnóstico; os demais executam o motor ou o gerador de roadmap com entradas completas.

## 4. Execução dos testes

Na raiz do projeto, com as dependências instaladas, executar:

```powershell
python -m unittest discover -s tests -p "test_robustez.py" -v
```

Para verificar toda a aplicação:

```powershell
python -m unittest discover -s tests -v
```

**Resultado informado na validação da Fase 5:** sete testes adicionais aprovados e suíte completa com **61 testes aprovados (54 anteriores + 7 novos)**, sem falhas ou erros.

## 5. Conclusão

A bateria adicional evidencia o tratamento consistente de limiares de classificação, empates, afinidades extremas e conhecimentos acima dos requisitos Júnior. O cenário integrado de Back-end também demonstra a continuidade entre recomendação, aplicação da regra RP01, avaliação das competências e geração do roadmap.

Esses testes não substituem as validações visuais e manuais da interface Streamlit, registradas no relatório técnico ilustrado. Em conjunto, as evidências demonstram a aderência aos requisitos de **tratamento de incerteza, compatibilidade ponderada, skill gaps e planos personalizados** do trabalho.
