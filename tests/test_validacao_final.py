
"""Bateria final de validação do sistema especialista."""

import unittest

from src.motor_inferencia import MotorInferencia
from src.fatos import EvidenciaCarreira


class TestValidacaoFinal(unittest.TestCase):

    def test_disparo_das_25_regras(self):
        """Verifica se todas as regras planejadas são acionadas."""

        cenarios = [
            ("R01", {"Q08": "A", "Q02": "A"}),
            ("R02", {"Q08": "A", "Q03": "C"}),
            ("R03", {"Q08": "B", "Q02": "B"}),
            ("R04", {"Q08": "B", "Q03": "B"}),
            ("R05", {"Q06": "A", "Q01": "C"}),
            ("R06", {"Q06": "A", "Q02": "C"}),
            ("R07", {"Q06": "B", "Q02": "D"}),
            ("R08", {"Q06": "B", "Q03": "D"}),
            ("R09", {"Q09": "A", "Q02": "F"}),
            ("R10", {"Q09": "A", "Q03": "E"}),
            ("R11", {"Q07": "A", "Q03": "F"}),
            ("R12", {"Q07": "A", "Q02": "E"}),
            ("R13", {"Q07": "B", "Q03": "G"}),
            ("R14", {"Q07": "B", "Q05": "D"}),
            ("R15", {"Q08": "C", "Q03": "H"}),
            ("R16", {"Q08": "C", "Q05": "B"}),
            ("R17", {"Q09": "B", "Q03": "I"}),
            ("R18", {"Q09": "B", "Q04": "E"}),
            ("R19", {"Q10": "A", "Q02": "G"}),
            ("R20", {"Q10": "A", "Q04": "F"}),
            ("R21", {"Q06": "A", "Q01": "C", "Q03": "D"}),
            ("R22", {"Q06": "B", "Q02": "D", "Q03": "A"}),
            ("R23", {"Q07": "A", "Q03": "G", "Q02": "E"}),
            ("R24", {"Q07": "B", "Q03": "F", "Q04": "D"}),
            ("R25", {"Q09": "B", "Q02": "F", "Q03": "I"})
        ]

        for regra, respostas in cenarios:
            with self.subTest(regra=regra):
                motor = MotorInferencia()
                motor.analisar(respostas)

                disparadas = {
                    fato["regra"]
                    for fato in motor.facts.values()
                    if isinstance(fato, EvidenciaCarreira)
                }

                self.assertIn(regra, disparadas)

    def test_persona_indefinida(self):
        """Não recomenda uma carreira sem evidências suficientes."""

        respostas = {
            "Q01": "B", "Q02": "G",
            "Q03": "J", "Q04": "A",
            "Q05": "A", "Q06": "C",
            "Q07": "C", "Q08": "D",
            "Q09": "C", "Q10": "D"
        }

        resultado = MotorInferencia().gerar_resultado(respostas)

        self.assertIsNone(resultado["carreira"])
        self.assertEqual(resultado["justificativas"], [])

    def test_questionario_vazio(self):
        """Valida o comportamento sem respostas."""

        resultado = MotorInferencia().gerar_resultado({})

        self.assertIsNone(resultado["carreira"])
        self.assertIsNone(resultado["pontuacao"])

    def test_reutilizacao_do_motor(self):
        """Verifica se uma análise não interfere na seguinte."""

        motor = MotorInferencia()

        primeiro = motor.gerar_resultado({
            "Q08": "A", "Q02": "A"
        })

        segundo = motor.gerar_resultado({
            "Q08": "B", "Q02": "B"
        })

        self.assertEqual(primeiro["carreira"], "Back-end")
        self.assertEqual(
            segundo["carreira"], "Front-end & UI/UX"
        )

        regras = {
            item["regra"] for item in segundo["justificativas"]
        }

        self.assertIn("R03", regras)
        self.assertNotIn("R01", regras)

    def test_pontuacao_sem_duplicidade(self):
        """Verifica que múltiplas regras não duplicam pontos."""

        respostas = {
            "Q06": "A",
            "Q01": "C",
            "Q02": "C",
            "Q03": "D"
        }

        resultado = MotorInferencia().gerar_resultado(respostas)

        self.assertEqual(
            resultado["carreira"], "Ciência de Dados e ML"
        )
        self.assertEqual(resultado["pontuacao"], 6)

        regras = {
            item["regra"]
            for item in resultado["justificativas"]
        }

        self.assertTrue(
            {"R05", "R06", "R21"}.issubset(regras)
        )


if __name__ == "__main__":
    unittest.main()
