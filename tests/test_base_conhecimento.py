
"""Testes de integridade e carregamento da base externa."""

import copy
import json
import tempfile
import unittest
from pathlib import Path

from src.base_conhecimento import (
    carregar_base_conhecimento,
    validar_base_conhecimento,
)


class TestBaseConhecimento(unittest.TestCase):

    def setUp(self):
        self.base = copy.deepcopy(carregar_base_conhecimento())

    def test_estrutura_completa(self):
        self.assertEqual(len(self.base["carreiras"]), 10)
        self.assertEqual(len(self.base["dimensoes"]), 10)
        self.assertEqual(len(self.base["regras_ponderadas"]), 20)
        self.assertEqual(len(self.base["competencias"]), 34)
        self.assertEqual(
            len(self.base["roadmaps"]["por_carreira"]), 10
        )

    def test_peso_invalido(self):
        self.base["carreiras"][0]["pesos"]["logica"] = 0

        with self.assertRaises(ValueError):
            validar_base_conhecimento(self.base)

    def test_competencia_desconhecida(self):
        self.base["requisitos_junior"]["backend"]["inexistente"] = 3

        with self.assertRaises(ValueError):
            validar_base_conhecimento(self.base)

    def test_roadmap_ausente(self):
        del self.base["roadmaps"]["por_carreira"]["backend"]

        with self.assertRaises(ValueError):
            validar_base_conhecimento(self.base)

    def test_carregamento_dinamico(self):
        """Alterações no JSON externo são lidas pelo carregador."""

        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "base_teste.json"

            self.base["metadados"]["versao"] = "2.0.1"

            caminho.write_text(
                json.dumps(self.base, ensure_ascii=False),
                encoding="utf-8"
            )

            carregada = carregar_base_conhecimento(caminho)

            self.assertEqual(
                carregada["metadados"]["versao"], "2.0.1"
            )

    def test_json_malformado(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "base_invalida.json"
            caminho.write_text('{"incompleto": ', encoding="utf-8")

            with self.assertRaises(ValueError):
                carregar_base_conhecimento(caminho)


if __name__ == "__main__":
    unittest.main()
