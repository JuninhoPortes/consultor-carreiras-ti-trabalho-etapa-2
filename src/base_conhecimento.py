
"""Carregamento e validação da base de conhecimento externa."""

import json
from pathlib import Path


CAMINHO_PADRAO = (
    Path(__file__).resolve().parent.parent
    / "dados"
    / "regras_carreiras.json"
)


def validar_base_conhecimento(base: dict) -> None:
    """Verifica a estrutura e as referências da base de conhecimento."""

    def exigir(condicao, mensagem):
        if not condicao:
            raise ValueError(f"Base de conhecimento inválida: {mensagem}")

    exigir(isinstance(base, dict), "a raiz deve ser um objeto JSON")

    campos = {
        "metadados", "escalas", "dimensoes",
        "perguntas_afinidade", "carreiras",
        "regras_ponderadas", "competencias",
        "requisitos_junior", "roadmaps"
    }

    exigir(campos <= base.keys(), "existem seções obrigatórias ausentes")

    dimensoes = base["dimensoes"]
    perguntas = base["perguntas_afinidade"]
    carreiras = base["carreiras"]
    regras = base["regras_ponderadas"]
    competencias = base["competencias"]
    requisitos = base["requisitos_junior"]
    roadmaps = base["roadmaps"]

    exigir(isinstance(dimensoes, dict) and len(dimensoes) == 10,
           "devem existir 10 dimensões")
    exigir(isinstance(perguntas, list) and len(perguntas) == 10,
           "devem existir 10 perguntas de afinidade")
    exigir(isinstance(carreiras, list) and len(carreiras) == 10,
           "devem existir 10 carreiras")
    exigir(isinstance(regras, list) and len(regras) >= 20,
           "devem existir pelo menos 20 regras ponderadas")
    exigir(isinstance(competencias, dict) and competencias,
           "catálogo de competências ausente")
    exigir(isinstance(requisitos, dict),
           "requisitos Júnior inválidos")
    exigir(isinstance(roadmaps, dict),
           "estrutura de roadmaps inválida")

    # Perguntas e dimensões
    ids_perguntas = [p["id"] for p in perguntas]
    exigir(len(set(ids_perguntas)) == len(ids_perguntas),
           "IDs de perguntas duplicados")

    for pergunta in perguntas:
        exigir(pergunta["dimensao"] in dimensoes,
               f"dimensão desconhecida em {pergunta['id']}")

    # Carreiras e pesos
    ids_carreiras = [c["id"] for c in carreiras]
    exigir(len(set(ids_carreiras)) == len(ids_carreiras),
           "IDs de carreiras duplicados")

    for carreira in carreiras:
        pesos = carreira["pesos"]
        exigir(isinstance(pesos, dict) and pesos,
               f"pesos ausentes em {carreira['id']}")

        for dimensao, peso in pesos.items():
            exigir(dimensao in dimensoes,
                   f"dimensão desconhecida: {dimensao}")
            exigir(type(peso) is int and 1 <= peso <= 5,
                   f"peso inválido: {carreira['id']}/{dimensao}")

    # Regras de bônus e penalidades
    ids_regras = [r["id"] for r in regras]
    exigir(len(set(ids_regras)) == len(ids_regras),
           "IDs de regras duplicados")

    for regra in regras:
        exigir(regra["carreira"] in ids_carreiras,
               f"carreira desconhecida em {regra['id']}")

        tipo = regra["tipo"]
        ajuste = regra["ajuste_percentual"]

        exigir(tipo in {"bonus", "penalidade"},
               f"tipo inválido em {regra['id']}")
        exigir(type(ajuste) in {int, float},
               f"ajuste inválido em {regra['id']}")
        exigir(0 < abs(ajuste) <= 100,
               f"magnitude inválida em {regra['id']}")
        exigir(
            (tipo == "bonus" and ajuste > 0)
            or (tipo == "penalidade" and ajuste < 0),
            f"sinal do ajuste inconsistente em {regra['id']}"
        )

        condicoes = regra["condicoes"]
        exigir(isinstance(condicoes, list) and len(condicoes) >= 2,
               f"regra sem condições cruzadas: {regra['id']}")

        for condicao in condicoes:
            exigir(condicao["dimensao"] in dimensoes,
                   f"dimensão desconhecida em {regra['id']}")
            exigir(condicao["operador"] in {">=", "<=", ">", "<", "=="},
                   f"operador inválido em {regra['id']}")
            valor = condicao["valor"]
            exigir(type(valor) is int and 1 <= valor <= 5,
                   f"limiar inválido em {regra['id']}")

    # Competências exigidas para cada carreira
    exigir(set(requisitos) == set(ids_carreiras),
           "requisitos Júnior não correspondem às carreiras")

    for carreira, habilidades in requisitos.items():
        exigir(isinstance(habilidades, dict) and habilidades,
               f"competências ausentes em {carreira}")

        for competencia, nivel in habilidades.items():
            exigir(competencia in competencias,
                   f"competência desconhecida: {competencia}")
            exigir(type(nivel) is int and 0 <= nivel <= 5,
                   f"nível inválido: {carreira}/{competencia}")

    # Integridade dos roadmaps
    exigir(
        {"estudos_por_competencia", "por_carreira"} <= roadmaps.keys(),
        "estrutura incompleta de roadmaps"
    )

    estudos = roadmaps["estudos_por_competencia"]
    planos = roadmaps["por_carreira"]

    exigir(set(estudos) == set(competencias),
           "nem todas as competências possuem conteúdos de estudo")
    exigir(set(planos) == set(ids_carreiras),
           "nem todas as carreiras possuem roadmap")

    for competencia, conteudos in estudos.items():
        exigir(
            isinstance(conteudos, list)
            and bool(conteudos)
            and all(isinstance(item, str) and item.strip()
                    for item in conteudos),
            f"estudos inválidos: {competencia}"
        )

    for carreira, plano in planos.items():
        exigidas = set(requisitos[carreira])
        certificacoes = plano["certificacoes"]
        portfolio = plano["portfolio"]

        exigir(isinstance(certificacoes, list) and certificacoes,
               f"certificações ausentes em {carreira}")

        for certificacao in certificacoes:
            exigir(bool(certificacao["nome"].strip()),
                   f"certificação sem nome em {carreira}")
            exigir(
                bool(certificacao["competencias"])
                and set(certificacao["competencias"]) <= exigidas,
                f"competências inválidas em certificação de {carreira}"
            )

        exigir(bool(portfolio["titulo"].strip()),
               f"projeto sem título em {carreira}")
        exigir(bool(portfolio["descricao"].strip()),
               f"projeto sem descrição em {carreira}")
        exigir(
            bool(portfolio["competencias"])
            and set(portfolio["competencias"]) <= exigidas,
            f"competências inválidas no portfólio de {carreira}"
        )


def carregar_base_conhecimento(caminho=None) -> dict:
    """Carrega o JSON e devolve somente dados validados."""

    arquivo = Path(caminho) if caminho is not None else CAMINHO_PADRAO

    try:
        with arquivo.open("r", encoding="utf-8") as origem:
            base = json.load(origem)

    except FileNotFoundError as erro:
        raise FileNotFoundError(
            f"Arquivo da base de conhecimento não encontrado: {arquivo}"
        ) from erro

    except json.JSONDecodeError as erro:
        raise ValueError(
            f"JSON inválido na linha {erro.lineno}: {erro.msg}"
        ) from erro

    validar_base_conhecimento(base)
    return base
