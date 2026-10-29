
"""Testes automatizados da análise de lacunas de competências."""

import unittest

from src.analise_gaps import AnalisadorGaps


class TestAnaliseGaps(unittest.TestCase):

    def setUp(self):
        self.analisador = AnalisadorGaps()

        self.conhecimentos_backend = {
            "programacao": 3,
            "apis_rest": 1,
            "sql": 0,
            "git": 2
        }

    def test_lacunas_backend(self):
        """Valida o cenário com duas lacunas em Back-end."""

        resultado = self.analisador.analisar(
            "backend",
            self.conhecimentos_backend
        )

        self.assertEqual(resultado["total_lacunas"], 2)
        self.assertEqual(resultado["cobertura_percentual"], 60.0)

        lacunas = {
            item["id"]: item["gap"]
            for item in resultado["lacunas"]
        }

        self.assertEqual(
            lacunas,
            {"apis_rest": 2, "sql": 2}
        )

    def test_conhecimentos_suficientes(self):
        """Usuário que atende aos requisitos não possui lacunas."""

        conhecimentos = {
            "programacao": 3,
            "apis_rest": 3,
            "sql": 2,
            "git": 2
        }

        resultado = self.analisador.analisar(
            "backend", conhecimentos
        )

        self.assertEqual(resultado["total_lacunas"], 0)
        self.assertEqual(resultado["lacunas"], [])
        self.assertEqual(resultado["cobertura_percentual"], 100.0)

    def test_sem_conhecimentos(self):
        """Conhecimento zero deve identificar todas as lacunas."""

        conhecimentos = {
            competencia: 0
            for competencia in self.conhecimentos_backend
        }

        resultado = self.analisador.analisar(
            "backend", conhecimentos
        )

        self.assertEqual(resultado["total_lacunas"], 4)
        self.assertEqual(resultado["cobertura_percentual"], 0.0)

    def test_conhecimento_acima_do_requisito(self):
        """Proficiência superior não deve gerar pontuação excedente."""

        conhecimentos = {
            "programacao": 5,
            "apis_rest": 3,
            "sql": 2,
            "git": 4
        }

        resultado = self.analisador.analisar(
            "backend", conhecimentos
        )

        self.assertEqual(resultado["total_lacunas"], 0)
        self.assertEqual(resultado["cobertura_percentual"], 100.0)

    def test_respostas_invalidas(self):
        """Rejeita níveis, carreiras e competências inválidas."""

        with self.assertRaises(ValueError):
            self.analisador.analisar(
                "carreira_inexistente",
                self.conhecimentos_backend
            )

        with self.assertRaises(ValueError):
            self.analisador.analisar("backend", None)

        incompletas = self.conhecimentos_backend.copy()
        del incompletas["sql"]

        with self.assertRaises(ValueError):
            self.analisador.analisar("backend", incompletas)

        extras = {
            **self.conhecimentos_backend,
            "competencia_inexistente": 3
        }

        with self.assertRaises(ValueError):
            self.analisador.analisar("backend", extras)

        for nivel in (-1, 6, 2.5, "3", True, None):
            with self.subTest(nivel=nivel):

                conhecimentos = {
                    **self.conhecimentos_backend,
                    "programacao": nivel
                }

                with self.assertRaises(ValueError):
                    self.analisador.analisar(
                        "backend", conhecimentos
                    )

    def test_outra_carreira(self):
        """Verifica a análise de Engenharia de Qualidade."""

        conhecimentos = {
            "testes_manuais": 3,
            "testes_automatizados": 0,
            "processos_qa": 2,
            "git": 2
        }

        resultado = self.analisador.analisar(
            "qa", conhecimentos
        )

        self.assertEqual(resultado["total_lacunas"], 1)
        self.assertAlmostEqual(
            resultado["cobertura_percentual"],
            77.78,
            places=2
        )

        self.assertEqual(
            resultado["lacunas"][0]["id"],
            "testes_automatizados"
        )

        self.assertEqual(
            resultado["lacunas"][0]["gap"],
            2
        )


if __name__ == "__main__":
    unittest.main()
