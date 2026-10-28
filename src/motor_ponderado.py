
"""Motor de compatibilidade ponderada para carreiras em TI."""

import operator

from src.base_conhecimento import carregar_base_conhecimento


OPERADORES = {
    ">=": operator.ge,
    "<=": operator.le,
    ">": operator.gt,
    "<": operator.lt,
    "==": operator.eq,
}


class MotorPonderado:
    """Calcula compatibilidades usando a base externa JSON."""

    def __init__(self):
        self.base = carregar_base_conhecimento()

    def validar_respostas(self, respostas):
        """Exige uma resposta válida para cada dimensão."""

        dimensoes = set(self.base["dimensoes"])

        if not isinstance(respostas, dict):
            raise ValueError("As respostas devem ser um dicionário.")

        if set(respostas) != dimensoes:
            faltantes = sorted(dimensoes - set(respostas))
            extras = sorted(set(respostas) - dimensoes)

            raise ValueError(
                f"Dimensões inválidas. "
                f"Faltantes: {faltantes}. Extras: {extras}."
            )

        for dimensao, valor in respostas.items():
            if type(valor) is not int or not 1 <= valor <= 5:
                raise ValueError(
                    f"A resposta de '{dimensao}' deve estar entre 1 e 5."
                )

    def calcular_base(self, respostas, pesos):
        """Calcula a compatibilidade percentual ponderada."""

        soma_pesos = sum(pesos.values())

        pontuacao = sum(
            peso * (respostas[dimensao] - 1)
            for dimensao, peso in pesos.items()
        )

        return (pontuacao / (4 * soma_pesos)) * 100

    def avaliar_condicoes(self, respostas, condicoes):
        """Verifica se todas as condições da regra são satisfeitas."""

        return all(
            OPERADORES[condicao["operador"]](
                respostas[condicao["dimensao"]],
                condicao["valor"]
            )
            for condicao in condicoes
        )

    
    def diagnosticar_perfil(self, ranking):
        """Classifica o perfil a partir das compatibilidades calculadas."""

        criterios = self.base["criterios_diagnostico"]

        primeira = ranking[0]
        segunda = ranking[1]

        maior = primeira["compatibilidade_percentual"]
        segunda_pontuacao = segunda["compatibilidade_percentual"]

        diferenca = round(maior - segunda_pontuacao, 2)

        limite_minimo = criterios["compatibilidade_minima"]
        margem_multifacetado = criterios[
            "diferenca_maxima_multifacetado"
        ]

        if maior < limite_minimo:
            classificacao = "inconclusivo"
            mensagem = (
                "As afinidades informadas não permitem destacar "
                "uma carreira com segurança. O ranking apresentado "
                "possui caráter exploratório."
            )

        elif diferenca <= margem_multifacetado:
            classificacao = "multifacetado"
            mensagem = (
                "Seu perfil apresenta afinidades próximas entre "
                "diferentes áreas da tecnologia. As carreiras "
                "mais bem posicionadas merecem uma análise conjunta."
            )

        else:
            classificacao = "predominante"
            mensagem = (
                f"Seu perfil apresenta maior compatibilidade "
                f"com {primeira['carreira']}, considerando "
                "as afinidades e regras avaliadas."
            )

        return {
            "classificacao": classificacao,
            "mensagem": mensagem,
            "diferenca_top_2": diferenca
        }


    def analisar(self, respostas):
        """Retorna o ranking completo e as três melhores carreiras."""

        self.validar_respostas(respostas)

        ranking = []

        for carreira in self.base["carreiras"]:
            carreira_id = carreira["id"]

            pontuacao_base = self.calcular_base(
                respostas,
                carreira["pesos"]
            )

            ajuste_total = 0
            regras_acionadas = []

            for regra in self.base["regras_ponderadas"]:
                if regra["carreira"] != carreira_id:
                    continue

                if self.avaliar_condicoes(
                    respostas,
                    regra["condicoes"]
                ):
                    ajuste = regra["ajuste_percentual"]
                    ajuste_total += ajuste

                    regras_acionadas.append({
                        "regra": regra["id"],
                        "tipo": regra["tipo"],
                        "ajuste_percentual": ajuste,
                        "justificativa": regra["justificativa"]
                    })

            compatibilidade = max(
                0,
                min(100, pontuacao_base + ajuste_total)
            )

            ranking.append({
                "id": carreira_id,
                "carreira": carreira["nome"],
                "pontuacao_base": round(pontuacao_base, 2),
                "ajuste_total": ajuste_total,
                "compatibilidade_percentual": round(
                    compatibilidade, 2
                ),
                "regras_acionadas": regras_acionadas
            })

        # Desempate determinístico:
        # 1. Maior compatibilidade final
        # 2. Maior pontuação-base
        # 3. Identificador da carreira
        ranking.sort(
            key=lambda item: (
                -item["compatibilidade_percentual"],
                -item["pontuacao_base"],
                item["id"]
            )
        )

        diagnostico = self.diagnosticar_perfil(ranking)

        return {
            "ranking": ranking,
            "top_3": ranking[:3],
            "diagnostico": diagnostico
        }
