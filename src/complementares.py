
"""Perguntas complementares para perfis profissionais ambíguos."""

from src.pontuacao import (
    SINAIS_PRINCIPAIS,
    calcular_pontuacoes,
)

ATIVIDADES_COMPLEMENTARES = {
    "Back-end": (
        "Desenvolver APIs e regras de negócio",
        "Projetar serviços e integração com bancos de dados",
    ),
    "Front-end & UI/UX": (
        "Construir interfaces web interativas",
        "Melhorar a usabilidade e experiência do usuário",
    ),
    "Ciência de Dados e ML": (
        "Construir modelos preditivos",
        "Realizar análises estatísticas e identificar padrões",
    ),
    "Engenharia de Dados": (
        "Construir pipelines de dados",
        "Organizar e transformar dados em grande escala",
    ),
    "Cibersegurança": (
        "Investigar vulnerabilidades e possíveis ataques",
        "Proteger sistemas, redes e informações",
    ),
    "DevOps & SRE": (
        "Automatizar implantações e integrações",
        "Monitorar sistemas e melhorar sua confiabilidade",
    ),
    "Computação em Nuvem": (
        "Projetar arquiteturas em nuvem",
        "Planejar infraestrutura escalável em AWS, Azure ou GCP",
    ),
    "Desenvolvimento Mobile": (
        "Criar aplicativos para Android e iOS",
        "Desenvolver experiências para dispositivos móveis",
    ),
    "Engenharia de Qualidade (QA)": (
        "Criar testes automatizados",
        "Investigar defeitos e validar funcionalidades",
    ),
    "Gestão de Produtos": (
        "Definir prioridades e estratégias de produto",
        "Compreender usuários e planejar funcionalidades",
    ),
}


def obter_candidatas(respostas: dict[str, str]) -> list[str]:
    """Identifica carreiras com evidências para investigação adicional."""

    pontuacoes = calcular_pontuacoes(respostas)

    principais = {
        carreira
        for (pergunta, alternativa), carreira
        in SINAIS_PRINCIPAIS.items()
        if respostas.get(pergunta) == alternativa
    }

    if principais:
        candidatas = principais
    else:
        # Sem sinais principais, exige pelo menos dois
        # sinais complementares para oferecer uma carreira.
        candidatas = {
            carreira
            for carreira, pontos in pontuacoes.items()
            if pontos >= 2
        }

    return sorted(
        candidatas,
        key=lambda carreira: (-pontuacoes[carreira], carreira)
    )
