"""Testes de robustez e casos-limite da Fase 5.

Execute a partir da raiz do projeto:
    python -m unittest discover -s tests -v
"""

import unittest

from src.motor_ponderado import MotorPonderado
from src.roadmap import GeradorRoadmap


class TestRobustezFase5(unittest.TestCase):
    def setUp(self):
        self.motor = MotorPonderado()
        self.gerador = GeradorRoadmap()

    @staticmethod
    def ranking_simulado(primeira, segunda):
        """Cria duas candidatas para exercitar os limites do diagnostico."""
        return [
            {
                "carreira": "Desenvolvimento Back-end",
                "compatibilidade_percentual": primeira,
            },
            {
                "carreira": "Engenharia de Dados",
                "compatibilidade_percentual": segunda,
            },
        ]

    def test_limite_inclusivo_de_dez_pontos(self):
        """Dez pontos de diferenca ainda indicam perfil multifacetado."""
        resultado = self.motor.diagnosticar_perfil(
            self.ranking_simulado(55.0, 45.0)
        )
        self.assertEqual(resultado["classificacao"], "multifacetado")
        self.assertEqual(resultado["diferenca_top_2"], 10.0)

    def test_diferenca_acima_de_dez_pontos(self):
        """Uma diferenca de 10,01 indica perfil predominante."""
        resultado = self.motor.diagnosticar_perfil(
            self.ranking_simulado(55.0, 44.99)
        )
        self.assertEqual(resultado["classificacao"], "predominante")
        self.assertEqual(resultado["diferenca_top_2"], 10.01)

    def test_abaixo_do_minimo_mesmo_em_empate(self):
        """Abaixo de 55% o perfil e inconclusivo, inclusive em empate."""
        resultado = self.motor.diagnosticar_perfil(
            self.ranking_simulado(54.99, 54.99)
        )
        self.assertEqual(resultado["classificacao"], "inconclusivo")
        self.assertEqual(resultado["diferenca_top_2"], 0.0)

    def test_todas_afinidades_no_minimo(self):
        """Perfil minimo nao gera compatibilidade artificial."""
        respostas = {dimensao: 1 for dimensao in self.motor.base["dimensoes"]}
        resultado = self.motor.analisar(respostas)
        self.assertEqual(len(resultado["ranking"]), 10)
        self.assertEqual(resultado["diagnostico"]["classificacao"], "inconclusivo")
        self.assertTrue(
            all(item["compatibilidade_percentual"] == 0.0
                for item in resultado["ranking"])
        )

    def test_todas_afinidades_no_maximo(self):
        """Bonus nao pode elevar percentuais acima de 100%."""
        respostas = {dimensao: 5 for dimensao in self.motor.base["dimensoes"]}
        resultado = self.motor.analisar(respostas)
        self.assertEqual(len(resultado["ranking"]), 10)
        self.assertEqual(resultado["diagnostico"]["classificacao"], "multifacetado")
        self.assertTrue(
            all(item["compatibilidade_percentual"] == 100.0
                for item in resultado["ranking"])
        )

    def test_fluxo_completo_do_perfil_backend(self):
        """A recomendacao se conecta aos gaps e ao roadmap esperado."""
        respostas = {dimensao: 1 for dimensao in self.motor.base["dimensoes"]}
        respostas.update({"logica": 5, "backend": 5})
        resultado = self.motor.analisar(respostas)
        primeira = resultado["top_3"][0]

        self.assertEqual(primeira["id"], "backend")
        self.assertEqual(primeira["compatibilidade_percentual"], 59.56)
        self.assertIn(
            "RP01", [regra["regra"] for regra in primeira["regras_acionadas"]]
        )

        conhecimentos = {
            "programacao": 3,
            "apis_rest": 1,
            "sql": 0,
            "git": 2,
        }
        roadmap = self.gerador.gerar(primeira["id"], conhecimentos)
        self.assertEqual(roadmap["cobertura_percentual"], 60.0)
        self.assertEqual(roadmap["total_lacunas"], 2)
        self.assertEqual(
            [etapa["competencia_id"] for etapa in roadmap["etapas_estudo"]],
            ["apis_rest", "sql"],
        )
        self.assertTrue(roadmap["projeto_portfolio"]["titulo"])

    def test_roadmap_sem_lacunas_mesmo_acima_do_junior(self):
        """Conhecimentos superiores ao Junior nao geram gaps negativos."""
        conhecimentos = {
            competencia: 5
            for competencia in self.gerador.base["requisitos_junior"]["backend"]
        }
        resultado = self.gerador.gerar("backend", conhecimentos)
        self.assertEqual(resultado["cobertura_percentual"], 100.0)
        self.assertEqual(resultado["total_lacunas"], 0)
        self.assertEqual(resultado["etapas_estudo"], [])
        self.assertTrue(resultado["projeto_portfolio"]["titulo"])


if __name__ == "__main__":
    unittest.main()
