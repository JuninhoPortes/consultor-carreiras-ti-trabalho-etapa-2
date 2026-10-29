
"""Testes do diagnóstico de ambiguidade do motor ponderado."""

import copy
import unittest

from src.motor_ponderado import MotorPonderado
from src.base_conhecimento import validar_base_conhecimento


class TestDiagnosticoPonderado(unittest.TestCase):

    def setUp(self):
        self.motor = MotorPonderado()

        self.respostas = {
            dimensao: 1
            for dimensao in self.motor.base["dimensoes"]
        }

    def test_perfil_predominante(self):
        """Back-end deve apresentar predominância clara."""

        respostas = {
            **self.respostas,
            "backend": 5,
            "logica": 5
        }

        resultado = self.motor.analisar(respostas)

        self.assertEqual(
            resultado["diagnostico"]["classificacao"],
            "predominante"
        )

        self.assertEqual(
            resultado["top_3"][0]["id"],
            "backend"
        )

    def test_perfil_multifacetado(self):
        """Interesses próximos devem indicar perfil multifacetado."""

        respostas = {
            **self.respostas,
            "backend": 5,
            "dados": 5,
            "logica": 5
        }

        resultado = self.motor.analisar(respostas)

        self.assertEqual(
            resultado["diagnostico"]["classificacao"],
            "multifacetado"
        )

        self.assertLessEqual(
            resultado["diagnostico"]["diferenca_top_2"],
            10
        )

    def test_perfil_inconclusivo(self):
        """Afinidades moderadas não devem indicar predominância."""

        respostas = {
            dimensao: 3
            for dimensao in self.motor.base["dimensoes"]
        }

        resultado = self.motor.analisar(respostas)

        self.assertEqual(
            resultado["diagnostico"]["classificacao"],
            "inconclusivo"
        )

        self.assertEqual(
            resultado["top_3"][0]["compatibilidade_percentual"],
            50.0
        )

    def test_afinidades_altas_em_todas_as_areas(self):
        """Afinidade máxima generalizada não indica carreira única."""

        respostas = {
            dimensao: 5
            for dimensao in self.motor.base["dimensoes"]
        }

        resultado = self.motor.analisar(respostas)

        self.assertEqual(
            resultado["diagnostico"]["classificacao"],
            "multifacetado"
        )

    def test_criterio_invalido(self):
        """Rejeita limiares fora da escala percentual."""

        base = copy.deepcopy(self.motor.base)

        base["criterios_diagnostico"][
            "compatibilidade_minima"
        ] = 101

        with self.assertRaises(ValueError):
            validar_base_conhecimento(base)


if __name__ == "__main__":
    unittest.main()
