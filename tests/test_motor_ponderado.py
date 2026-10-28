
"""Testes automatizados do motor de compatibilidade ponderada."""

import unittest

from src.motor_ponderado import MotorPonderado


class TestMotorPonderado(unittest.TestCase):

    def setUp(self):
        self.motor = MotorPonderado()

        # Perfil neutro: afinidade moderada em todas as dimensões.
        self.respostas = {
            dimensao: 3
            for dimensao in self.motor.base["dimensoes"]
        }

    def obter_carreira(self, resultado, identificador):
        return next(
            carreira
            for carreira in resultado["ranking"]
            if carreira["id"] == identificador
        )

    def test_compatibilidade_neutra(self):
        """Todas as afinidades moderadas devem produzir 50%."""

        resultado = self.motor.analisar(self.respostas)

        for carreira in resultado["ranking"]:
            self.assertEqual(
                carreira["pontuacao_base"], 50.0
            )
            self.assertEqual(
                carreira["compatibilidade_percentual"], 50.0
            )
            self.assertEqual(
                carreira["regras_acionadas"], []
            )

    def test_bonus_backend(self):
        """Verifica o bônus da regra RP01."""

        self.respostas["backend"] = 5
        self.respostas["logica"] = 5

        resultado = self.motor.analisar(self.respostas)
        backend = self.obter_carreira(resultado, "backend")

        regras = [
            regra["regra"]
            for regra in backend["regras_acionadas"]
        ]

        self.assertIn("RP01", regras)
        self.assertEqual(backend["ajuste_total"], 4)

        self.assertAlmostEqual(
            backend["compatibilidade_percentual"],
            backend["pontuacao_base"] + 4,
            places=2
        )

    def test_penalidade_backend(self):
        """Verifica a penalidade da regra RP02."""

        self.respostas["backend"] = 2
        self.respostas["interfaces"] = 4

        resultado = self.motor.analisar(self.respostas)
        backend = self.obter_carreira(resultado, "backend")

        regras = [
            regra["regra"]
            for regra in backend["regras_acionadas"]
        ]

        self.assertIn("RP02", regras)
        self.assertEqual(backend["ajuste_total"], -5)

    def test_ranking_e_top3(self):
        """Verifica quantidade e ordenação das recomendações."""

        self.respostas["backend"] = 5
        self.respostas["logica"] = 5

        resultado = self.motor.analisar(self.respostas)

        self.assertEqual(len(resultado["ranking"]), 10)
        self.assertEqual(len(resultado["top_3"]), 3)

        self.assertEqual(
            resultado["top_3"],
            resultado["ranking"][:3]
        )

        pontuacoes = [
            carreira["compatibilidade_percentual"]
            for carreira in resultado["ranking"]
        ]

        self.assertEqual(
            pontuacoes,
            sorted(pontuacoes, reverse=True)
        )

        self.assertEqual(
            resultado["top_3"][0]["id"],
            "backend"
        )

        self.assertAlmostEqual(
            resultado["top_3"][0]["compatibilidade_percentual"],
            81.78,
            places=2
        )

    def test_desempate_deterministico(self):
        """Empates devem seguir os critérios definidos pelo motor."""

        resultado = self.motor.analisar(self.respostas)

        identificadores = [
            carreira["id"]
            for carreira in resultado["ranking"]
        ]

        self.assertEqual(
            identificadores,
            sorted(identificadores)
        )

    def test_limites_percentuais(self):
        """Nenhuma compatibilidade pode ultrapassar 0% ou 100%."""

        for afinidade in (1, 5):
            with self.subTest(afinidade=afinidade):

                respostas = {
                    dimensao: afinidade
                    for dimensao in self.motor.base["dimensoes"]
                }

                resultado = self.motor.analisar(respostas)

                for carreira in resultado["ranking"]:
                    percentual = carreira[
                        "compatibilidade_percentual"
                    ]

                    self.assertGreaterEqual(percentual, 0)
                    self.assertLessEqual(percentual, 100)

    def test_respostas_invalidas(self):
        """Rejeita respostas fora da escala ou incompletas."""

        casos = [
            {"logica": 0},
            {"logica": 6},
            {"logica": "5"},
            {"logica": True},
            {"logica": None},
        ]

        for alteracao in casos:
            with self.subTest(alteracao=alteracao):

                respostas = {
                    **self.respostas,
                    **alteracao
                }

                with self.assertRaises(ValueError):
                    self.motor.analisar(respostas)

        respostas_incompletas = self.respostas.copy()
        del respostas_incompletas["logica"]

        with self.assertRaises(ValueError):
            self.motor.analisar(respostas_incompletas)

        respostas_extras = {
            **self.respostas,
            "dimensao_inexistente": 5
        }

        with self.assertRaises(ValueError):
            self.motor.analisar(respostas_extras)

    def test_analises_independentes(self):
        """Uma análise não deve interferir nas seguintes."""

        respostas_backend = {
            **self.respostas,
            "backend": 5,
            "logica": 5
        }

        primeira = self.motor.analisar(respostas_backend)
        segunda = self.motor.analisar(self.respostas)

        self.assertEqual(
            primeira["top_3"][0]["id"],
            "backend"
        )

        self.assertEqual(
            len(segunda["ranking"]),
            10
        )

        for carreira in segunda["ranking"]:
            self.assertEqual(
                carreira["compatibilidade_percentual"],
                50.0
            )
            self.assertEqual(
                carreira["regras_acionadas"],
                []
            )


if __name__ == "__main__":
    unittest.main()
