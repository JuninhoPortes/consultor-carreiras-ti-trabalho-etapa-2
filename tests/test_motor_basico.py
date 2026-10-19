
"""Teste básico de funcionamento do motor de inferência."""

import unittest

from src.compatibilidade import preparar_experta

preparar_experta()

from experta import Fact, KnowledgeEngine, Rule


class MotorTeste(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.regra_disparada = False

    @Rule(Fact(tipo="teste"))
    def executar_regra(self):
        self.regra_disparada = True


class TestMotorInferencia(unittest.TestCase):

    def test_execucao_regra(self):
        motor = MotorTeste()
        motor.reset()
        motor.declare(Fact(tipo="teste"))
        motor.run()

        self.assertTrue(motor.regra_disparada)


if __name__ == "__main__":
    unittest.main()
