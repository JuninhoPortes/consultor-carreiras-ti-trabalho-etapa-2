
"""Definição dos fatos utilizados pelo sistema especialista."""

from src.compatibilidade import preparar_experta

preparar_experta()

from experta import Fact


class RespostaUsuario(Fact):
    """
    Representa uma resposta fornecida pelo usuário.

    Atributos:
        pergunta: identificador da pergunta (Q01 a Q10).
        alternativa: alternativa selecionada (A, B, C etc.).
    """
    pass


class EvidenciaCarreira(Fact):
    """
    Representa uma evidência identificada pelo motor.

    Atributos:
        carreira: carreira favorecida pela evidência.
        regra: identificador da regra disparada.
        justificativa: motivo da identificação.
    """
    pass
