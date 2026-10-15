
"""Testes das perguntas complementares e da regra R26."""

import unittest

from src.motor_inferencia import MotorInferencia
from src.complementares import obter_candidatas


class TestComplementares(unittest.TestCase):

    def setUp(self):
        """Prepara um perfil com interesses em várias áreas."""
        self.respostas = {
            "Q01": "A",
            "Q02": "C",
            "Q03": "C",
            "Q04": "C",
            "Q05": "B",
            "Q06": "B",
            "Q07": "B",
            "Q08": "B",
            "Q09": "B",
            "Q10": "B"
        }

    def test_identificacao_de_candidatas(self):
        """Verifica as carreiras disponíveis para investigação."""

        candidatas = obter_candidatas(self.respostas)

        esperadas = {
            "Engenharia de Dados",
            "Computação em Nuvem",
            "Front-end & UI/UX",
            "Engenharia de Qualidade (QA)"
        }

        self.assertEqual(set(candidatas), esperadas)

    def test_recomendacao_complementar(self):
        """Valida a recomendação após responder Q11 e Q12."""

        respostas = {
            **self.respostas,
            "Q11": "Engenharia de Dados",
            "Q12": "A"
        }

        resultado = MotorInferencia().gerar_resultado(respostas)

        self.assertEqual(
            resultado["carreira"], "Engenharia de Dados"
        )

        self.assertEqual(resultado["pontuacao"], 8)

        regras = {
            item["regra"]
            for item in resultado["justificativas"]
        }

        self.assertIn("R26", regras)

    def test_sem_confirmacao_complementar(self):
        """Não recomenda sem confirmação da atividade."""

        respostas = {
            **self.respostas,
            "Q11": "Engenharia de Dados"
        }

        resultado = MotorInferencia().gerar_resultado(respostas)

        self.assertIsNone(resultado["carreira"])


if __name__ == "__main__":
    unittest.main()
