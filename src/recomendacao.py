
"""Seleção da carreira recomendada e critérios de desempate."""

from src.pontuacao import SINAIS_PRINCIPAIS, SINAIS_COMPLEMENTARES


def selecionar_carreira(
    pontuacoes: dict[str, int],
    respostas: dict[str, str]
) -> str | None:
    """Seleciona a carreira mais compatível com o perfil."""

    # Verifica se existem carreiras elegíveis.
    if not pontuacoes:
        return None

    # Identifica a maior pontuação.
    maior_pontuacao = max(pontuacoes.values())

    candidatas = [
        carreira
        for carreira, pontos in pontuacoes.items()
        if pontos == maior_pontuacao
    ]

    if len(candidatas) == 1:
        return candidatas[0]

    # Primeiro desempate: quantidade de sinais principais.
    quantidade_principais = {
        carreira: sum(
            1
            for pergunta, alternativa in respostas.items()
            if SINAIS_PRINCIPAIS.get((pergunta, alternativa))
            == carreira
        )
        for carreira in candidatas
    }

    maior_quantidade = max(quantidade_principais.values())

    candidatas = [
        carreira
        for carreira in candidatas
        if quantidade_principais[carreira] == maior_quantidade
    ]

    if len(candidatas) == 1:
        return candidatas[0]

    # Demais desempates: preferências em Q02 e Q03.
    for pergunta in ("Q02", "Q03"):
        alternativa = respostas.get(pergunta)

        favorecidas = SINAIS_COMPLEMENTARES.get(
            (pergunta, alternativa), ()
        )

        correspondentes = [
            carreira
            for carreira in candidatas
            if carreira in favorecidas
        ]

        if len(correspondentes) == 1:
            return correspondentes[0]

        if correspondentes:
            candidatas = correspondentes

    # Empate não resolvido: solicitar mais informações.
    return None
