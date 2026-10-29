
"""Testes automatizados do gerador de roadmaps personalizados."""

import unittest

from src.roadmap import GeradorRoadmap


class TestGeradorRoadmap(unittest.TestCase):

    def setUp(self):
        self.gerador = GeradorRoadmap()
        self.base = self.gerador.base

        self.conhecimentos_backend = {
            "programacao": 3,
            "apis_rest": 1,
            "sql": 0,
            "git": 2
        }

    def test_roadmap_backend_com_lacunas(self):
        """Valida o roadmap do perfil Back-end já analisado."""

        resultado = self.gerador.gerar(
            "backend",
            self.conhecimentos_backend
        )

        self.assertEqual(resultado["carreira_id"], "backend")
        self.assertEqual(resultado["cobertura_percentual"], 60.0)
        self.assertEqual(resultado["total_lacunas"], 2)

        prioridades = [
            etapa["competencia_id"]
            for etapa in resultado["etapas_estudo"]
        ]

        self.assertEqual(
            prioridades,
            ["apis_rest", "sql"]
        )

        self.assertEqual(
            resultado["projeto_portfolio"]["titulo"],
            "API REST de gerenciamento de tarefas"
        )

    def test_priorizacao_das_lacunas(self):
        """Prioriza gaps maiores e os níveis Júnior mais elevados."""

        conhecimentos = {
            competencia: 0
            for competencia in self.conhecimentos_backend
        }

        resultado = self.gerador.gerar(
            "backend",
            conhecimentos
        )

        prioridades = [
            etapa["competencia_id"]
            for etapa in resultado["etapas_estudo"]
        ]

        self.assertEqual(
            prioridades,
            ["apis_rest", "programacao", "git", "sql"]
        )

        self.assertEqual(
            [
                etapa["prioridade"]
                for etapa in resultado["etapas_estudo"]
            ],
            [1, 2, 3, 4]
        )

    def test_certificacoes_por_lacuna(self):
        """Sugere certificações relacionadas às competências pendentes."""

        conhecimentos = {
            "programacao": 3,
            "apis_rest": 3,
            "sql": 2,
            "git": 0
        }

        resultado = self.gerador.gerar(
            "backend",
            conhecimentos
        )

        certificacoes = [
            item["nome"]
            for item in resultado["certificacoes"]
        ]

        self.assertEqual(
            certificacoes,
            ["GitHub Foundations"]
        )

        self.assertEqual(
            resultado["total_lacunas"],
            1
        )

    def test_conteudos_carregados_do_json(self):
        """Confirma que os estudos vêm da base externa."""

        resultado = self.gerador.gerar(
            "backend",
            self.conhecimentos_backend
        )

        estudos = self.base["roadmaps"][
            "estudos_por_competencia"
        ]

        for etapa in resultado["etapas_estudo"]:
            competencia = etapa["competencia_id"]

            self.assertEqual(
                etapa["conteudos"],
                estudos[competencia]
            )

            # O resultado não deve compartilhar a lista original.
            self.assertIsNot(
                etapa["conteudos"],
                estudos[competencia]
            )

    def test_dez_carreiras_com_lacunas(self):
        """Verifica roadmaps para todas as carreiras."""

        for carreira, requisitos in self.base[
            "requisitos_junior"
        ].items():

            with self.subTest(carreira=carreira):
                conhecimentos = {
                    competencia: 0
                    for competencia in requisitos
                }

                resultado = self.gerador.gerar(
                    carreira,
                    conhecimentos
                )

                self.assertEqual(
                    resultado["total_lacunas"],
                    len(requisitos)
                )

                self.assertEqual(
                    len(resultado["etapas_estudo"]),
                    len(requisitos)
                )

                self.assertEqual(
                    resultado["cobertura_percentual"],
                    0.0
                )

                self.assertTrue(
                    resultado["projeto_portfolio"]["titulo"]
                )

    def test_dez_carreiras_sem_lacunas(self):
        """Usuários que atendem aos requisitos não recebem estudos pendentes."""

        for carreira, requisitos in self.base[
            "requisitos_junior"
        ].items():

            with self.subTest(carreira=carreira):
                conhecimentos = requisitos.copy()

                resultado = self.gerador.gerar(
                    carreira,
                    conhecimentos
                )

                self.assertEqual(
                    resultado["total_lacunas"], 0
                )

                self.assertEqual(
                    resultado["cobertura_percentual"],
                    100.0
                )

                self.assertEqual(
                    resultado["etapas_estudo"], []
                )

                self.assertEqual(
                    resultado["certificacoes"], []
                )

                self.assertEqual(
                    resultado["projeto_portfolio"][
                        "competencias_prioritarias"
                    ],
                    []
                )

                # Mesmo sem gaps, existe projeto para portfólio.
                self.assertTrue(
                    resultado["projeto_portfolio"]["titulo"]
                )

    def test_entradas_invalidas(self):
        """Rejeita carreiras e conhecimentos inválidos."""

        with self.assertRaises(ValueError):
            self.gerador.gerar(
                "carreira_inexistente",
                self.conhecimentos_backend
            )

        with self.assertRaises(ValueError):
            self.gerador.gerar("backend", None)

        incompletos = {
            "programacao": 3,
            "apis_rest": 1
        }

        with self.assertRaises(ValueError):
            self.gerador.gerar(
                "backend",
                incompletos
            )

        for nivel in (-1, 6, 2.5, "3", True):
            with self.subTest(nivel=nivel):
                conhecimentos = {
                    **self.conhecimentos_backend,
                    "apis_rest": nivel
                }

                with self.assertRaises(ValueError):
                    self.gerador.gerar(
                        "backend",
                        conhecimentos
                    )

    def test_analises_independentes(self):
        """Uma análise não deve interferir na próxima."""

        primeira = self.gerador.gerar(
            "backend",
            self.conhecimentos_backend
        )

        conhecimentos_completos = {
            "programacao": 3,
            "apis_rest": 3,
            "sql": 2,
            "git": 2
        }

        segunda = self.gerador.gerar(
            "backend",
            conhecimentos_completos
        )

        self.assertEqual(
            primeira["total_lacunas"], 2
        )

        self.assertEqual(
            segunda["total_lacunas"], 0
        )

        self.assertEqual(
            primeira["cobertura_percentual"], 60.0
        )

        self.assertEqual(
            segunda["cobertura_percentual"], 100.0
        )


if __name__ == "__main__":
    unittest.main()
