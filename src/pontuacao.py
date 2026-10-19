
"""Configuração dos critérios de pontuação das carreiras."""

# Pesos definidos na matriz de decisão.
PESO_SINAL_PRINCIPAL = 3
PESO_SINAL_COMPLEMENTAR = 1


# Mapeamento das respostas principais (Q06 a Q10).
SINAIS_PRINCIPAIS = {
    ("Q06", "A"): "Ciência de Dados e ML",
    ("Q06", "B"): "Engenharia de Dados",

    ("Q07", "A"): "DevOps & SRE",
    ("Q07", "B"): "Computação em Nuvem",

    ("Q08", "A"): "Back-end",
    ("Q08", "B"): "Front-end & UI/UX",
    ("Q08", "C"): "Desenvolvimento Mobile",

    ("Q09", "A"): "Cibersegurança",
    ("Q09", "B"): "Engenharia de Qualidade (QA)",

    ("Q10", "A"): "Gestão de Produtos"
}


# Mapeamento dos sinais complementares (Q01 a Q05).
# Uma resposta pode favorecer mais de uma carreira.

SINAIS_COMPLEMENTARES = {
    # Q01 — Afinidade matemática
    ("Q01", "C"): ("Ciência de Dados e ML",),

    # Q02 — Atividade profissional
    ("Q02", "A"): ("Back-end", "Desenvolvimento Mobile"),
    ("Q02", "B"): ("Front-end & UI/UX", "Desenvolvimento Mobile"),
    ("Q02", "C"): ("Ciência de Dados e ML",),
    ("Q02", "D"): ("Engenharia de Dados",),
    ("Q02", "E"): ("DevOps & SRE", "Computação em Nuvem"),
    ("Q02", "F"): ("Cibersegurança", "Engenharia de Qualidade (QA)"),
    ("Q02", "G"): ("Gestão de Produtos",),

    # Q03 — Conhecimentos e ferramentas
    ("Q03", "A"): (
        "Back-end", "Ciência de Dados e ML", "Engenharia de Dados"
    ),
    ("Q03", "B"): ("Front-end & UI/UX",),
    ("Q03", "C"): ("Back-end",),
    ("Q03", "D"): (
        "Back-end", "Ciência de Dados e ML", "Engenharia de Dados"
    ),
    ("Q03", "E"): (
        "Cibersegurança", "DevOps & SRE", "Computação em Nuvem"
    ),
    ("Q03", "F"): ("DevOps & SRE",),
    ("Q03", "G"): ("Computação em Nuvem",),
    ("Q03", "H"): ("Desenvolvimento Mobile",),
    ("Q03", "I"): ("Engenharia de Qualidade (QA)",),

    # Q04 — Entrega de valor
    ("Q04", "A"): ("Back-end", "Desenvolvimento Mobile"),
    ("Q04", "B"): ("Front-end & UI/UX",),
    ("Q04", "C"): ("Ciência de Dados e ML", "Engenharia de Dados"),
    ("Q04", "D"): ("DevOps & SRE", "Computação em Nuvem"),
    ("Q04", "E"): ("Cibersegurança", "Engenharia de Qualidade (QA)"),
    ("Q04", "F"): ("Gestão de Produtos",),

    # Q05 — Ambiente de atuação
    ("Q05", "A"): ("Back-end",),
    ("Q05", "B"): ("Front-end & UI/UX", "Desenvolvimento Mobile"),
    ("Q05", "C"): ("Ciência de Dados e ML", "Engenharia de Dados"),
    ("Q05", "D"): ("DevOps & SRE", "Computação em Nuvem"),
    ("Q05", "E"): (
        "Cibersegurança", "DevOps & SRE", "Engenharia de Qualidade (QA)"
    ),
    ("Q05", "F"): ("Gestão de Produtos",)
}

def calcular_pontuacoes(respostas: dict[str, str]) -> dict[str, int]:
    """
    Calcula a pontuação das 10 carreiras com base
    nas respostas fornecidas pelo usuário.

    Retorna um dicionário contendo a pontuação
    acumulada de cada carreira.
    """

    # Inicializa todas as carreiras com zero pontos.
    pontuacoes = {
        carreira: 0
        for carreira in SINAIS_PRINCIPAIS.values()
    }

    # Analisa cada resposta fornecida pelo usuário.
    for pergunta, alternativa in respostas.items():
        chave = (pergunta, alternativa)

        # Verifica se existe um sinal principal.
        if chave in SINAIS_PRINCIPAIS:
            carreira = SINAIS_PRINCIPAIS[chave]
            pontuacoes[carreira] += PESO_SINAL_PRINCIPAL

        # Verifica os sinais complementares.
        if chave in SINAIS_COMPLEMENTARES:
            carreiras = SINAIS_COMPLEMENTARES[chave]

            for carreira in carreiras:
                pontuacoes[carreira] += PESO_SINAL_COMPLEMENTAR

    return pontuacoes

