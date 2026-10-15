
"""Testes das recomendações das 10 carreiras profissionais."""

import unittest

from src.motor_inferencia import MotorInferencia


class TestRecomendacoes(unittest.TestCase):
    """Valida as recomendações do sistema especialista."""

    def test_recomendacoes_das_dez_carreiras(self):
        casos = [
            ("Back-end",
             {"Q08": "A", "Q02": "A"}, "R01"),

            ("Front-end & UI/UX",
             {"Q08": "B", "Q02": "B"}, "R03"),

            ("Ciência de Dados e ML",
             {"Q06": "A", "Q01": "C"}, "R05"),

            ("Engenharia de Dados",
             {"Q06": "B", "Q02": "D"}, "R07"),

            ("Cibersegurança",
             {"Q09": "A", "Q02": "F"}, "R09"),

            ("DevOps & SRE",
             {"Q07": "A", "Q03": "F"}, "R11"),

            ("Computação em Nuvem",
             {"Q07": "B", "Q03": "G"}, "R13"),

            ("Desenvolvimento Mobile",
             {"Q08": "C", "Q03": "H"}, "R15"),

            ("Engenharia de Qualidade (QA)",
             {"Q09": "B", "Q03": "I"}, "R17"),

            ("Gestão de Produtos",
             {"Q10": "A", "Q02": "G"}, "R19")
        ]

        for carreira, respostas, regra in casos:
            with self.subTest(carreira=carreira):
                motor = MotorInferencia()
                resultado = motor.gerar_resultado(respostas)

                self.assertEqual(
                    resultado["carreira"], carreira
                )

                self.assertEqual(
                    resultado["pontuacao"], 4
                )

                regras_disparadas = [
                    item["regra"]
                    for item in resultado["justificativas"]
                ]

                self.assertIn(regra, regras_disparadas)

                self.assertTrue(resultado["justificativas"])



    def test_informacoes_insuficientes(self):
        """Não recomenda uma carreira sem regra de identificação."""

        motor = MotorInferencia()
        resultado = motor.gerar_resultado({"Q08": "A"})

        self.assertIsNone(resultado["carreira"])
        self.assertIsNone(resultado["pontuacao"])
        self.assertEqual(resultado["justificativas"], [])

    def test_desempate_por_atividade_profissional(self):
        """Resolve empate utilizando a preferência em Q02."""

        respostas = {
            "Q01": "C",
            "Q02": "C",
            "Q03": "F",
            "Q05": "D",
            "Q06": "A",
            "Q07": "A"
        }

        motor = MotorInferencia()
        resultado = motor.gerar_resultado(respostas)

        self.assertEqual(
            resultado["carreira"], "Ciência de Dados e ML"
        )
        self.assertEqual(resultado["pontuacao"], 5)

    def test_empate_nao_resolvido(self):
        """Não realiza escolha arbitrária entre carreiras empatadas."""

        respostas = {
            "Q01": "C",
            "Q03": "A",
            "Q04": "A",
            "Q06": "A",
            "Q08": "A"
        }

        motor = MotorInferencia()
        resultado = motor.gerar_resultado(respostas)

        self.assertIsNone(resultado["carreira"])
        self.assertIn("empate", resultado["mensagem"].lower())



if __name__ == "__main__":
    unittest.main()
