
"""Interface web do Consultor Inteligente de Carreiras em TI."""

import streamlit as st

from src.motor_inferencia import MotorInferencia
from pathlib import Path
from src.complementares import (
    ATIVIDADES_COMPLEMENTARES,
    obter_candidatas,
)


st.set_page_config(
    page_title="Consultor Inteligente de Carreiras",
    page_icon=None,
    layout="centered"
)


# Questionário definido durante a engenharia de conhecimento.
PERGUNTAS = {
    "Q01": (
        "Qual é seu nível de afinidade com matemática e estatística?",
        {"A": "Baixo", "B": "Médio", "C": "Alto"}
    ),
    "Q02": (
        "Qual atividade você gostaria de realizar no dia a dia?",
        {
            "A": "Desenvolver algoritmos e funcionalidades",
            "B": "Criar interfaces e experiências visuais",
            "C": "Analisar dados e identificar padrões",
            "D": "Organizar e transformar grandes volumes de dados",
            "E": "Configurar servidores e automatizar processos",
            "F": "Investigar falhas, vulnerabilidades e riscos",
            "G": "Planejar funcionalidades e prioridades de produtos"
        }
    ),
    "Q03": (
        "Com qual tecnologia você possui maior familiaridade?",
        {
            "A": "Python",
            "B": "JavaScript, HTML e CSS",
            "C": "Java ou C#",
            "D": "SQL e bancos de dados",
            "E": "Linux e redes",
            "F": "Docker e ferramentas de CI/CD",
            "G": "AWS, Azure ou Google Cloud",
            "H": "Flutter, React Native ou desenvolvimento mobile",
            "I": "Ferramentas de testes e automação",
            "J": "Nenhuma — estou começando"
        }
    ),
    "Q04": (
        "Qual resultado profissional você considera mais interessante?",
        {
            "A": "Desenvolver soluções utilizadas pelas pessoas",
            "B": "Proporcionar experiências visuais intuitivas",
            "C": "Transformar dados em informações úteis",
            "D": "Garantir infraestrutura estável e escalável",
            "E": "Proteger sistemas e garantir sua qualidade",
            "F": "Contribuir para decisões e resultados de negócio"
        }
    ),
    "Q05": (
        "Em qual ambiente você gostaria de trabalhar?",
        {
            "A": "Aplicações web e APIs",
            "B": "Interfaces e aplicações móveis",
            "C": "Plataformas e ambientes de dados",
            "D": "Servidores, redes e infraestrutura em nuvem",
            "E": "Qualidade, segurança e automação",
            "F": "Planejamento e gestão de produtos"
        }
    ),
    "Q06": (
        "Se fosse trabalhar com dados, qual atividade preferiria?",
        {
            "A": "Analisar padrões e criar modelos preditivos",
            "B": "Construir processos de coleta e transformação de dados",
            "C": "Não tenho preferência"
        }
    ),
    "Q07": (
        "Qual atividade de infraestrutura desperta mais interesse?",
        {
            "A": "Automatizar implantações e monitorar aplicações",
            "B": "Projetar ambientes e arquiteturas em nuvem",
            "C": "Não tenho preferência"
        }
    ),
    "Q08": (
        "Qual tipo de desenvolvimento considera mais interessante?",
        {
            "A": "Implementar APIs e regras de negócio",
            "B": "Criar interfaces web intuitivas",
            "C": "Desenvolver aplicativos para smartphones e tablets",
            "D": "Não tenho preferência"
        }
    ),
    "Q09": (
        "Qual atividade você considera mais interessante?",
        {
            "A": "Investigar vulnerabilidades e proteger sistemas",
            "B": "Identificar defeitos e automatizar testes",
            "C": "Não tenho preferência"
        }
    ),
    "Q10": (
        "Qual responsabilidade preferiria assumir em um projeto?",
        {
            "A": "Definir prioridades e orientar o produto",
            "B": "Implementar soluções técnicas",
            "C": "Participar das decisões e da implementação",
            "D": "Ainda não tenho preferência"
        }
    )
}



# Carrega os estilos personalizados.
caminho_css = Path(__file__).parent / "assets" / "estilo.css"

with open(caminho_css, encoding="utf-8") as arquivo:
    st.markdown(
        f"<style>{arquivo.read()}</style>",
        unsafe_allow_html=True
    )



def limpar_feedback():
    """Remove avisos e resultados antigos quando uma resposta muda."""
    st.session_state.pop("aviso_pendencias", None)
    st.session_state.pop("resultado", None)
    st.session_state.pop("Q11", None)
    st.session_state.pop("Q12", None)


def limpar_formulario():
    """Limpa todas as respostas e informações da análise."""
    for codigo in PERGUNTAS:
        st.session_state.pop(codigo, None)

    limpar_feedback()


def limpar_confirmacao():
    """Reinicia a atividade ao trocar a carreira complementar."""
    st.session_state.pop("Q12", None)


# Cabeçalho principal.
st.markdown(
    """
    <div class="hero">
        <div class="hero-tag">SISTEMA ESPECIALISTA EM TI</div>
        <h1>Descubra seu caminho na <span>tecnologia.</span></h1>
        <p>
            Explore suas afinidades, habilidades e interesses
            profissionais. Nosso sistema especialista analisa
            suas respostas para recomendar uma das 10 trilhas
            de carreira em Tecnologia da Informação.
        </p>
        <div class="hero-footer">
            ✦ 10 perguntas &nbsp; • &nbsp;
            10 carreiras &nbsp; • &nbsp;
            Recomendação personalizada
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.info(
    "Responda com base nas suas preferências pessoais. "
    "Não existem respostas certas ou erradas."
)


# Questionário interativo.
with st.container(key="questionario", border=False):

    st.subheader("01 — Seu perfil profissional")
    st.caption(
        "Conte um pouco sobre suas afinidades e conhecimentos."
    )

    for codigo in list(PERGUNTAS.keys())[:5]:
        pergunta, alternativas = PERGUNTAS[codigo]

        st.selectbox(
            f"{codigo} — {pergunta}",
            options=list(alternativas.keys()),
            format_func=lambda opcao, a=alternativas: (
                f"{opcao}) {a[opcao]}"
            ),
            index=None,
            placeholder="Selecione uma alternativa",
            key=codigo,
            on_change=limpar_feedback
        )

    st.divider()

    st.subheader("02 — Suas especialidades")
    st.caption(
        "Identifique as áreas e atividades que mais despertam interesse."
    )

    for codigo in list(PERGUNTAS.keys())[5:]:
        pergunta, alternativas = PERGUNTAS[codigo]

        st.selectbox(
            f"{codigo} — {pergunta}",
            options=list(alternativas.keys()),
            format_func=lambda opcao, a=alternativas: (
                f"{opcao}) {a[opcao]}"
            ),
            index=None,
            placeholder="Selecione uma alternativa",
            key=codigo,
            on_change=limpar_feedback
        )

    st.divider()

    enviar = st.button(
        "Descobrir minha carreira",
        type="primary",
        use_container_width=True,
        key="botao_descobrir"
    )

    # Processamento das respostas.
    if enviar:
        respostas = {
            codigo: st.session_state.get(codigo)
            for codigo in PERGUNTAS
        }

        faltantes = [
            codigo
            for codigo, resposta in respostas.items()
            if resposta is None
        ]

        if faltantes:
            st.session_state.pop("resultado", None)

            st.session_state["aviso_pendencias"] = (
                "Responda todas as perguntas: "
                + ", ".join(faltantes)
            )

        else:
            st.session_state.pop("aviso_pendencias", None)

            motor = MotorInferencia()

            st.session_state["resultado"] = (
                 motor.gerar_resultado(respostas)
            )

    # Solicita a rolagem automática após gerar o resultado.
    st.session_state["rolar_para_resultado"] = True

    # Exibe o aviso somente enquanto não houver correção.
    if st.session_state.get("aviso_pendencias"):
        st.warning(st.session_state["aviso_pendencias"])



# Apresentação da recomendação.
if "resultado" in st.session_state:

    resultado = st.session_state["resultado"]

    # Ponto de destino da rolagem automática.
    st.markdown(
        '<div id="resultado-carreira"></div>',
        unsafe_allow_html=True
    )

    st.divider()


    st.markdown(
        '<div class="resultado-titulo">'
        'ANÁLISE PROFISSIONAL'
        '</div>',
        unsafe_allow_html=True
    )

    st.header("Sua recomendação")

    
    if resultado["carreira"] is None:

        st.markdown(
            f'<div class="aviso-complementar">'
            f'{resultado["mensagem"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        respostas_atuais = {
            codigo: st.session_state.get(codigo)
            for codigo in PERGUNTAS
        }

        candidatas = obter_candidatas(respostas_atuais)

        if candidatas:
            with st.container(
                key="perguntas_complementares",
                border=False
            ):
                st.subheader("Vamos conhecer melhor seu perfil")
                st.caption(
                    "Identificamos afinidades que merecem uma análise "
                    "mais específica. Responda às duas perguntas abaixo."
                )

                st.selectbox(
                    "Q11 — Qual destas áreas mais desperta seu interesse?",
                    options=candidatas,
                    index=None,
                    placeholder="Selecione uma área",
                    key="Q11",
                    on_change=limpar_confirmacao
                )

                carreira_escolhida = st.session_state.get("Q11")

                if carreira_escolhida:
                    atividades = ATIVIDADES_COMPLEMENTARES[
                        carreira_escolhida
                    ]

                    st.selectbox(
                        "Q12 — Qual atividade você preferiria realizar?",
                        options=["A", "B"],
                        format_func=lambda opcao: (
                            atividades[0]
                            if opcao == "A"
                            else atividades[1]
                        ),
                        index=None,
                        placeholder="Selecione uma atividade",
                        key="Q12"
                    )

                if st.button(
                    "Confirmar minha afinidade",
                    type="primary",
                    use_container_width=True,
                    key="botao_complementar"
                ):
                    escolha = st.session_state.get("Q11")
                    atividade = st.session_state.get("Q12")

                    if not escolha or not atividade:
                        st.warning(
                            "Responda às duas perguntas complementares."
                        )
                    else:
                        respostas_completas = {
                            **respostas_atuais,
                            "Q11": escolha,
                            "Q12": atividade
                        }

                        motor = MotorInferencia()

                        st.session_state["resultado"] = (
                            motor.gerar_resultado(respostas_completas)
                        )

                        st.session_state[
                            "rolar_para_resultado"
                        ] = True

                        st.rerun()

        else:
            st.info(
                "Ainda não identificamos evidências suficientes "
                "para selecionar áreas de investigação. "
                "Revise suas preferências no questionário inicial."
            )


    else:
        st.markdown(
    """
    <div class="sucesso-banner">
        Perfil analisado com sucesso!
    </div>
    """,
    unsafe_allow_html=True
)

        st.subheader(f"♛ {resultado['carreira']}")

        st.metric(
            "Pontuação de compatibilidade",
            resultado["pontuacao"]
        )

        st.caption(
            "A pontuação indica evidências de afinidade "
            "e não representa uma probabilidade de sucesso."
        )

        st.markdown("### Por que essa carreira?")

        for item in resultado["justificativas"]:
            with st.expander(
                f"Regra {item['regra']}",
                expanded=False
            ):
                st.write(item["motivo"])

    st.button(
    "Refazer questionário",
    on_click=limpar_formulario,
    use_container_width=True,
    key="botao_refazer"
)


    # Rola suavemente até o resultado após a análise.
    if st.session_state.pop("rolar_para_resultado", False):
        st.html(
            """
            <script>
                (function () {
                    let tentativas = 0;

                    function rolarParaResultado() {
                        const alvo = document.getElementById(
                            "resultado-carreira"
                        );

                        if (alvo) {
                            alvo.scrollIntoView({
                                behavior: "smooth",
                                block: "start"
                            });
                        } else if (tentativas++ < 20) {
                            setTimeout(rolarParaResultado, 100);
                        }
                    }

                    setTimeout(rolarParaResultado, 200);
                })();
            </script>
            """,
            unsafe_allow_javascript=True
        )


st.divider()

st.markdown(
    """
    <p style="
        text-align: center;
        color: #b9d4e5;
        font-size: 0.85rem;
        margin-top: 1rem;
    ">
        Consultor Inteligente de Carreiras em TI
        • Sistema Especialista baseado em Regras
        • Python + Experta + Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
