
"""Validação do motor ponderado com diferentes perfis profissionais."""

import unittest

from src.motor_ponderado import MotorPonderado


class TestPerfisPonderados(unittest.TestCase):

    def setUp(self):
        self.motor = MotorPonderado()

        self.respostas_base = {
            dimensao: 1
            for dimensao in self.motor.base["dimensoes"]
        }

    def criar_perfil(self, afinidades):
        """Cria um perfil mantendo afinidade mínima nas demais áreas."""
        return {
            **self.respostas_base,
            **afinidades
        }

    def test_personas_profissionais(self):
        """Valida diferentes perfis e suas regras de identificação."""

        personas = [
            (
                "Back-end",
                {"backend": 5, "logica": 5},
                "backend",
                "RP01"
            ),
            (
                "Ciência de Dados",
                {"dados": 5, "logica": 5},
                "ciencia_dados",
                "RP05"
            ),
            (
                "Cibersegurança",
                {"seguranca": 5, "logica": 5},
                "ciberseguranca",
                "RP09"
            ),
            (
                "Front-end",
                {"interfaces": 5, "qualidade": 4},
                "frontend",
                "RP03"
            ),
            (
                "DevOps",
                {"devops": 5, "nuvem": 5},
                "devops",
                "RP11"
            ),
            (
                "Gestão de Produtos",
                {"produto": 5, "dados": 4},
                "produto",
                "RP19"
            )
        ]

        for nome, afinidades, carreira_esperada, regra_esperada in personas:
            with self.subTest(persona=nome):

                respostas = self.criar_perfil(afinidades)
                resultado = self.motor.analisar(respostas)

                primeira = resultado["top_3"][0]

                self.assertEqual(
                    primeira["id"],
                    carreira_esperada
                )

                regras = {
                    regra["regra"]
                    for regra in primeira["regras_acionadas"]
                }

                self.assertIn(regra_esperada, regras)

    def test_perfil_hibrido_dados_backend(self):
        """Verifica o ranking de um usuário com interesses mistos."""

        respostas = self.criar_perfil({
            "backend": 5,
            "dados": 5,
            "logica": 5
        })

        resultado = self.motor.analisar(respostas)

        top3 = [
            carreira["id"]
            for carreira in resultado["top_3"]
        ]

        self.assertEqual(
            top3,
            ["ciencia_dados", "backend", "engenharia_dados"]
        )

        diferenca = (
            resultado["top_3"][0]["compatibilidade_percentual"]
            - resultado["top_3"][1]["compatibilidade_percentual"]
        )

        # As duas primeiras carreiras apresentam afinidades próximas.
        self.assertLessEqual(diferenca, 10)

    def test_empate_em_perfil_neutro(self):
        """Todas as dimensões moderadas geram compatibilidades iguais."""

        respostas = {
            dimensao: 3
            for dimensao in self.motor.base["dimensoes"]
        }

        resultado = self.motor.analisar(respostas)

        pontuacoes = {
            carreira["compatibilidade_percentual"]
            for carreira in resultado["ranking"]
        }

        self.assertEqual(pontuacoes, {50.0})

        # O ranking continua determinístico.
        ids = [
            carreira["id"]
            for carreira in resultado["ranking"]
        ]

        self.assertEqual(ids, sorted(ids))

    def test_penalidade_em_perfil_conflitante(self):
        """Baixa afinidade com Back-end deve aplicar sua penalidade."""

        respostas = self.criar_perfil({
            "backend": 1,
            "interfaces": 5,
            "logica": 4
        })

        resultado = self.motor.analisar(respostas)

        backend = next(
            carreira
            for carreira in resultado["ranking"]
            if carreira["id"] == "backend"
        )

        regras = {
            regra["regra"]
            for regra in backend["regras_acionadas"]
        }

        self.assertIn("RP02", regras)
        self.assertEqual(backend["ajuste_total"], -5)

        self.assertEqual(
            resultado["top_3"][0]["id"],
            "frontend"
        )


if __name__ == "__main__":
    unittest.main()
