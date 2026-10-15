
"""Testes de validação com personas profissionais."""

import unittest

from src.motor_inferencia import MotorInferencia


class TestPersonas(unittest.TestCase):
    """Valida recomendações com questionários completos."""

    def test_persona_analitica(self):
        """Valida o perfil de Ciência de Dados e ML."""

        respostas = {
            "Q01": "C",
            "Q02": "C",
            "Q03": "A",
            "Q04": "C",
            "Q05": "C",
            "Q06": "A",
            "Q07": "C",
            "Q08": "D",
            "Q09": "C",
            "Q10": "D"
        }

        resultado = MotorInferencia().gerar_resultado(respostas)

        self.assertEqual(
            resultado["carreira"], "Ciência de Dados e ML"
        )
        self.assertEqual(resultado["pontuacao"], 8)

        regras = {
            item["regra"]
            for item in resultado["justificativas"]
        }

        self.assertTrue({"R05", "R06"}.issubset(regras))

    def test_persona_seguranca(self):
        """Valida o perfil de Cibersegurança."""

        respostas = {
            "Q01": "B",
            "Q02": "F",
            "Q03": "E",
            "Q04": "E",
            "Q05": "E",
            "Q06": "C",
            "Q07": "C",
            "Q08": "D",
            "Q09": "A",
            "Q10": "D"
        }

        resultado = MotorInferencia().gerar_resultado(respostas)

        self.assertEqual(
            resultado["carreira"], "Cibersegurança"
        )
        self.assertEqual(resultado["pontuacao"], 7)

        regras = {
            item["regra"]
            for item in resultado["justificativas"]
        }

        self.assertTrue({"R09", "R10"}.issubset(regras))


    def test_persona_visual(self):
        """Valida o perfil de Front-end & UI/UX."""

        respostas = {
            "Q01": "A",
            "Q02": "B",
            "Q03": "B",
            "Q04": "B",
            "Q05": "B",
            "Q06": "C",
            "Q07": "C",
            "Q08": "B",
            "Q09": "C",
            "Q10": "D"
        }

        resultado = MotorInferencia().gerar_resultado(respostas)

        self.assertEqual(
            resultado["carreira"], "Front-end & UI/UX"
        )
        self.assertEqual(resultado["pontuacao"], 7)

        regras = {
            item["regra"]
            for item in resultado["justificativas"]
        }

        self.assertTrue({"R03", "R04"}.issubset(regras))

    def test_persona_negocios(self):
        """Valida o perfil de Gestão de Produtos."""

        respostas = {
            "Q01": "B",
            "Q02": "G",
            "Q03": "J",
            "Q04": "F",
            "Q05": "F",
            "Q06": "C",
            "Q07": "C",
            "Q08": "D",
            "Q09": "C",
            "Q10": "A"
        }

        resultado = MotorInferencia().gerar_resultado(respostas)

        self.assertEqual(
            resultado["carreira"], "Gestão de Produtos"
        )
        self.assertEqual(resultado["pontuacao"], 6)

        regras = {
            item["regra"]
            for item in resultado["justificativas"]
        }

        self.assertTrue({"R19", "R20"}.issubset(regras))


if __name__ == "__main__":
    unittest.main()
