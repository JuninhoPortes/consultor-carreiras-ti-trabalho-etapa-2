
"""Análise das lacunas de competências para carreiras em TI."""

from src.base_conhecimento import carregar_base_conhecimento


class AnalisadorGaps:
    """Compara conhecimentos atuais com requisitos Júnior."""

    def __init__(self):
        self.base = carregar_base_conhecimento()

        self.carreiras = {
            carreira["id"]: carreira["nome"]
            for carreira in self.base["carreiras"]
        }

    def validar_conhecimentos(self, carreira_id, conhecimentos):
        """Valida a carreira e os níveis informados."""

        requisitos = self.base["requisitos_junior"]

        if carreira_id not in requisitos:
            raise ValueError(
                f"Carreira desconhecida: {carreira_id}"
            )

        if not isinstance(conhecimentos, dict):
            raise ValueError(
                "Os conhecimentos devem ser um dicionário."
            )

        competencias_esperadas = set(requisitos[carreira_id])
        competencias_informadas = set(conhecimentos)

        if competencias_informadas != competencias_esperadas:
            faltantes = sorted(
                competencias_esperadas - competencias_informadas
            )
            extras = sorted(
                competencias_informadas - competencias_esperadas
            )

            raise ValueError(
                f"Competências inválidas. "
                f"Faltantes: {faltantes}. Extras: {extras}."
            )

        for competencia, nivel in conhecimentos.items():
            if type(nivel) is not int or not 0 <= nivel <= 5:
                raise ValueError(
                    f"Nível inválido para '{competencia}'. "
                    "Informe um valor inteiro de 0 a 5."
                )

    def analisar(self, carreira_id, conhecimentos):
        """Identifica gaps e calcula a cobertura dos requisitos."""

        self.validar_conhecimentos(
            carreira_id,
            conhecimentos
        )

        requisitos = self.base["requisitos_junior"][carreira_id]
        catalogo = self.base["competencias"]

        competencias_avaliadas = []
        pontos_obtidos = 0
        pontos_esperados = 0

        for competencia_id, nivel_junior in requisitos.items():
            nivel_atual = conhecimentos[competencia_id]

            gap = max(0, nivel_junior - nivel_atual)

            pontos_obtidos += min(nivel_atual, nivel_junior)
            pontos_esperados += nivel_junior

            competencias_avaliadas.append({
                "id": competencia_id,
                "competencia": catalogo[competencia_id],
                "nivel_atual": nivel_atual,
                "nivel_junior": nivel_junior,
                "gap": gap,
                "atendida": gap == 0
            })

        # Ordena as lacunas por maior diferença de conhecimento.
        lacunas = sorted(
            [
                item
                for item in competencias_avaliadas
                if not item["atendida"]
            ],
            key=lambda item: (
                -item["gap"],
                -item["nivel_junior"],
                item["id"]
            )
        )

        atendidas = [
            item
            for item in competencias_avaliadas
            if item["atendida"]
        ]

        cobertura = (
            (pontos_obtidos / pontos_esperados) * 100
            if pontos_esperados > 0
            else 100.0
        )

        return {
            "carreira_id": carreira_id,
            "carreira": self.carreiras[carreira_id],
            "competencias_avaliadas": competencias_avaliadas,
            "lacunas": lacunas,
            "competencias_atendidas": atendidas,
            "total_lacunas": len(lacunas),
            "cobertura_percentual": round(cobertura, 2)
        }
