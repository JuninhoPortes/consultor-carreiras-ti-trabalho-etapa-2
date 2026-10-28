
"""Geração de roadmaps personalizados para carreiras em TI."""

from src.analise_gaps import AnalisadorGaps


class GeradorRoadmap:
    """Gera planos de desenvolvimento a partir dos skill gaps."""

    def __init__(self):
        self.analisador = AnalisadorGaps()
        self.base = self.analisador.base

    def gerar(self, carreira_id, conhecimentos):
        """Gera um roadmap de acordo com a carreira e as lacunas."""

        # A análise também valida a carreira e os conhecimentos.
        analise = self.analisador.analisar(
            carreira_id,
            conhecimentos
        )

        roadmaps = self.base["roadmaps"]
        plano = roadmaps["por_carreira"][carreira_id]
        estudos = roadmaps["estudos_por_competencia"]
        catalogo = self.base["competencias"]

        lacunas = analise["lacunas"]
        ids_lacunas = {item["id"] for item in lacunas}

        # 1. Plano de estudos organizado por prioridade.
        etapas_estudo = []

        for prioridade, lacuna in enumerate(lacunas, start=1):
            competencia_id = lacuna["id"]

            etapas_estudo.append({
                "prioridade": prioridade,
                "competencia_id": competencia_id,
                "competencia": lacuna["competencia"],
                "nivel_atual": lacuna["nivel_atual"],
                "nivel_junior": lacuna["nivel_junior"],
                "gap": lacuna["gap"],
                "conteudos": list(estudos[competencia_id])
            })

        # 2. Certificações relacionadas às competências pendentes.
        certificacoes = []

        for certificacao in plano["certificacoes"]:
            relacionadas = [
                competencia
                for competencia in certificacao["competencias"]
                if competencia in ids_lacunas
            ]

            if relacionadas:
                certificacoes.append({
                    "nome": certificacao["nome"],
                    "competencias_relacionadas": [
                        catalogo[competencia]
                        for competencia in relacionadas
                    ],
                    "orientacao": (
                        "Considere esta certificação após desenvolver "
                        "os conhecimentos necessários e verificar "
                        "seus pré-requisitos."
                    )
                })

        # 3. Projeto de portfólio adaptado às lacunas.
        portfolio_base = plano["portfolio"]

        competencias_praticar = [
            catalogo[competencia]
            for competencia in portfolio_base["competencias"]
            if competencia in ids_lacunas
        ]

        if competencias_praticar:
            orientacao_portfolio = (
                "Durante o projeto, priorize a prática das "
                "competências identificadas como lacunas."
            )
        else:
            orientacao_portfolio = (
                "Utilize o projeto para consolidar seus "
                "conhecimentos e demonstrar suas habilidades."
            )

        projeto_portfolio = {
            "titulo": portfolio_base["titulo"],
            "descricao": portfolio_base["descricao"],
            "competencias_prioritarias": competencias_praticar,
            "orientacao": orientacao_portfolio
        }

        # 4. Mensagem correspondente ao resultado.
        if lacunas:
            mensagem = (
                f"Foram identificadas {len(lacunas)} lacuna(s) "
                "de competências. O roadmap foi organizado "
                "para priorizar seu desenvolvimento."
            )
        else:
            mensagem = (
                "Você declarou atender aos níveis de referência "
                "Júnior cadastrados para esta carreira. "
                "Continue praticando e desenvolvendo seu portfólio."
            )

        return {
            "carreira_id": carreira_id,
            "carreira": analise["carreira"],
            "cobertura_percentual": analise["cobertura_percentual"],
            "total_lacunas": analise["total_lacunas"],
            "etapas_estudo": etapas_estudo,
            "certificacoes": certificacoes,
            "projeto_portfolio": projeto_portfolio,
            "mensagem": mensagem
        }
