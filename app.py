
"""Interface avançada do Consultor de Carreiras em TI."""

from pathlib import Path

import streamlit as st
import altair as alt

from src.base_conhecimento import carregar_base_conhecimento
from src.motor_ponderado import MotorPonderado
from src.roadmap import GeradorRoadmap

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Consultor Inteligente de Carreiras em TI",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# IDENTIDADE VISUAL
# ============================================================

CAMINHO_CSS = (
    Path(__file__).resolve().parent
    / "assets"
    / "estilo.css"
)

if CAMINHO_CSS.exists():
    st.markdown(
        f"<style>{CAMINHO_CSS.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# ============================================================
# BASE DE CONHECIMENTO
# ============================================================

base = carregar_base_conhecimento()

# ============================================================
# ARMAZENAMENTO DAS RESPOSTAS
# ============================================================

if "perfil_pessoal" not in st.session_state:
    st.session_state["perfil_pessoal"] = {
        "situacao": None,
        "experiencia": None
    }

if "afinidades" not in st.session_state:
    st.session_state["afinidades"] = {
        dimensao: 3
        for dimensao in base["dimensoes"]
    }

if "objetivos_carreira" not in st.session_state:
    st.session_state["objetivos_carreira"] = {
        "principal": None,
        "foco": None
    }

def salvar_perfil(campo):
    """Preserva as informações pessoais entre as etapas."""

    st.session_state["perfil_pessoal"][campo] = (
        st.session_state[f"_perfil_{campo}"]
    )

def salvar_afinidade(dimensao):
    """Preserva a afinidade e invalida análises anteriores."""

    st.session_state["afinidades"][dimensao] = (
        st.session_state[f"_afinidade_{dimensao}"]
    )

    st.session_state.pop("resultado_ponderado", None)
    st.session_state.pop("carreira_roadmap", None)
    st.session_state["conhecimentos_roadmap"] = {}
    st.session_state.pop("resultado_roadmap", None)

def salvar_objetivo(campo):
    """Preserva os objetivos e atualiza o estado da análise."""

    st.session_state["objetivos_carreira"][campo] = (
        st.session_state[f"_objetivo_{campo}"]
    )

    st.session_state.pop("resultado_ponderado", None)
    st.session_state.pop("carreira_roadmap", None)
    st.session_state["conhecimentos_roadmap"] = {}
    st.session_state.pop("resultado_roadmap", None)

def mudar_carreira_roadmap():
    """Limpa conhecimentos ao escolher outra carreira."""

    st.session_state["conhecimentos_roadmap"] = {}
    st.session_state.pop("resultado_roadmap", None)

def salvar_conhecimento(competencia_id):
    """Preserva os níveis de conhecimento informados."""

    chave = f"_conhecimento_{competencia_id}"

    if "conhecimentos_roadmap" not in st.session_state:
        st.session_state["conhecimentos_roadmap"] = {}

    st.session_state["conhecimentos_roadmap"][competencia_id] = (
        st.session_state[chave]
    )

    # Uma alteração exige gerar novamente o roadmap.
    st.session_state.pop("resultado_roadmap", None)

def analisar_perfil():
    """Executa a análise de compatibilidade profissional."""

    objetivos = st.session_state["objetivos_carreira"]

    if not all(objetivos.values()):
        return

    motor = MotorPonderado()

    respostas = st.session_state["afinidades"].copy()

    resultado = motor.analisar(respostas)

    st.session_state["resultado_ponderado"] = resultado

    # Reinicia a avaliação de competências para a nova análise.
    st.session_state.pop("carreira_roadmap", None)
    st.session_state["conhecimentos_roadmap"] = {}
    st.session_state.pop("resultado_roadmap", None)

    # Solicita rolagem automática até a recomendação.
    st.session_state["rolar_para_resultado"] = True

def gerar_roadmap():
    """Gera o plano apenas quando todas as competências foram respondidas."""

    carreira_id = st.session_state.get("carreira_roadmap")
    resultado = st.session_state.get("resultado_ponderado")
    conhecimentos = st.session_state.get("conhecimentos_roadmap", {})

    if not resultado or carreira_id not in {
        item["id"] for item in resultado["top_3"]
    }:
        return

    requisitos = base["requisitos_junior"][carreira_id]

    if not all(
        conhecimentos.get(competencia_id) is not None
        for competencia_id in requisitos
    ):
        return

    st.session_state["resultado_roadmap"] = GeradorRoadmap().gerar(
        carreira_id,
        {competencia_id: conhecimentos[competencia_id]
         for competencia_id in requisitos}
    )
    st.session_state["rolar_para_roadmap"] = True


# ============================================================
# CONFIGURAÇÃO DAS ETAPAS
# ============================================================

ETAPAS = [
    "Perfil pessoal",
    "Afinidades técnicas",
    "Objetivos de carreira"
]

if "etapa_atual" not in st.session_state:
    st.session_state["etapa_atual"] = 0

def mudar_etapa(deslocamento):
    """Avança ou retorna entre as etapas disponíveis."""

    atual = st.session_state["etapa_atual"]
    nova = atual + deslocamento

    st.session_state["etapa_atual"] = max(
        0,
        min(nova, len(ETAPAS) - 1)
    )

def reiniciar_navegacao():
    """Retorna à primeira etapa."""

    st.session_state["etapa_atual"] = 0

# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    """
    <div style="text-align: center;">
        <h1>👑 Consultor Inteligente de Carreiras</h1>
        <p>
            Descubra suas afinidades profissionais e construa
            seu plano de desenvolvimento em Tecnologia da Informação.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# INDICADOR DE PROGRESSO
# ============================================================

etapa = st.session_state["etapa_atual"]

st.progress(
    (etapa + 1) / len(ETAPAS)
)

st.caption(
    f"Etapa {etapa + 1} de {len(ETAPAS)} — {ETAPAS[etapa]}"
)

st.divider()

# ============================================================
# CONTEÚDO DAS ETAPAS
# ============================================================

if etapa == 0:

    # --------------------------------------------------------
    # ETAPA 1 — PERFIL PESSOAL
    # --------------------------------------------------------

    st.subheader("Seu perfil profissional")

    st.write(
        "Antes de analisar suas afinidades, queremos conhecer "
        "um pouco sobre sua experiência com tecnologia."
    )

    perfil = st.session_state["perfil_pessoal"]

    st.session_state["_perfil_situacao"] = perfil["situacao"]

    st.selectbox(
        "Qual é sua situação profissional atual?",
        options=[
            "Estudante de Tecnologia da Informação",
            "Iniciante na área de tecnologia",
            "Profissional de Tecnologia da Informação",
            "Profissional em transição de carreira"
        ],
        index=None,
        placeholder="Selecione sua situação atual",
        key="_perfil_situacao",
        on_change=salvar_perfil,
        args=("situacao",)
    )

    st.session_state["_perfil_experiencia"] = perfil["experiencia"]

    st.selectbox(
        "Qual é seu nível de experiência com tecnologia?",
        options=[
            "Nenhuma experiência",
            "Menos de 1 ano",
            "Entre 1 e 3 anos",
            "Mais de 3 anos"
        ],
        index=None,
        placeholder="Selecione sua experiência",
        key="_perfil_experiencia",
        on_change=salvar_perfil,
        args=("experiencia",)
    )

    st.caption(
        "Essas informações contextualizam seu perfil, "
        "mas não modificam os pesos do cálculo de compatibilidade."
    )

elif etapa == 1:

    # --------------------------------------------------------
    # ETAPA 2 — AFINIDADES TÉCNICAS
    # --------------------------------------------------------

    st.subheader("Suas afinidades técnicas")

    st.write(
        "Avalie seu nível de interesse por cada área da "
        "Tecnologia da Informação utilizando a escala de 1 a 5."
    )

    st.caption(
        "1 = Nenhuma afinidade | "
        "3 = Afinidade moderada | "
        "5 = Afinidade muito alta"
    )

    for pergunta in base["perguntas_afinidade"]:

        dimensao = pergunta["dimensao"]
        chave = f"_afinidade_{dimensao}"

        # Recupera a resposta armazenada.
        st.session_state[chave] = (
            st.session_state["afinidades"][dimensao]
        )

        st.slider(
            label=pergunta["texto"],
            min_value=1,
            max_value=5,
            step=1,
            key=chave,
            on_change=salvar_afinidade,
            args=(dimensao,)
        )

    st.info(
        "Todas as afinidades começam no nível 3 (moderado). "
        "Ajuste cada valor conforme suas preferências."
    )

elif etapa == 2:

    # --------------------------------------------------------
    # ETAPA 3 — OBJETIVOS DE CARREIRA
    # --------------------------------------------------------

    st.subheader("Seus objetivos de carreira")

    st.write(
        "Estamos quase terminando! Agora queremos compreender "
        "seus objetivos profissionais para contextualizar "
        "as recomendações e seu futuro plano de desenvolvimento."
    )

    objetivos = st.session_state["objetivos_carreira"]

    # --------------------------------------------------------
    # OBJETIVO PRINCIPAL
    # --------------------------------------------------------

    st.session_state["_objetivo_principal"] = (
        objetivos["principal"]
    )

    st.selectbox(
        "Qual é seu principal objetivo profissional?",
        options=[
            "Descobrir uma carreira compatível com meu perfil",
            "Conseguir minha primeira oportunidade em TI",
            "Migrar para outra especialidade de tecnologia",
            "Evoluir profissionalmente na área em que atuo"
        ],
        index=None,
        placeholder="Selecione seu objetivo principal",
        key="_objetivo_principal",
        on_change=salvar_objetivo,
        args=("principal",)
    )

    # --------------------------------------------------------
    # FOCO DE DESENVOLVIMENTO
    # --------------------------------------------------------

    st.session_state["_objetivo_foco"] = (
        objetivos["foco"]
    )

    st.selectbox(
        "O que você deseja priorizar no seu desenvolvimento?",
        options=[
            "Aprender novas tecnologias e competências",
            "Desenvolver projetos para meu portfólio",
            "Preparar-me para certificações profissionais",
            "Combinar estudos, projetos e certificações"
        ],
        index=None,
        placeholder="Selecione sua prioridade",
        key="_objetivo_foco",
        on_change=salvar_objetivo,
        args=("foco",)
    )

    st.caption(
        "Essas informações ajudam a contextualizar sua "
        "orientação profissional. A compatibilidade percentual "
        "continua sendo calculada pelas afinidades e regras "
        "ponderadas da base de conhecimento."
    )

    if all(objetivos.values()):
        st.success(
            "Objetivos registrados! Seu questionário está "
            "preparado para a análise de compatibilidade."
        )

# ============================================================
# NAVEGAÇÃO
# ============================================================

st.divider()

if etapa == 0:

    # Centraliza o botão Continuar na primeira etapa.
    _, coluna_central, _ = st.columns([1, 2, 1])

    with coluna_central:
        st.button(
            "Continuar",
            on_click=mudar_etapa,
            args=(1,),
            use_container_width=True,
            key="wizard_proximo",
            disabled=not all(
                st.session_state["perfil_pessoal"].values()
            )
        )

else:

    # Nas demais etapas, distribui os botões igualmente.
    coluna_voltar, coluna_avancar = st.columns(2)

    with coluna_voltar:
        st.button(
            "Voltar",
            on_click=mudar_etapa,
            args=(-1,),
            use_container_width=True,
            key="wizard_voltar"
        )

    with coluna_avancar:

        if etapa < len(ETAPAS) - 1:
            st.button(
                "Continuar",
                on_click=mudar_etapa,
                args=(1,),
                use_container_width=True,
                key="wizard_proximo"
            )

        else:
            st.button(
                "Analisar meu perfil",
                on_click=analisar_perfil,
                use_container_width=True,
                key="wizard_analisar",
                disabled=not all(
                    st.session_state["objetivos_carreira"].values()
                )
            )

# ============================================================
# RESULTADO DA ANÁLISE PROFISSIONAL
# ============================================================

if etapa == 2 and "resultado_ponderado" in st.session_state:

    resultado = st.session_state["resultado_ponderado"]
    diagnostico = resultado["diagnostico"]

    st.divider()

    # Destino da rolagem automática.
    st.markdown(
        '<div id="resultado-ponderado"></div>',
        unsafe_allow_html=True
    )

    st.subheader("Sua análise profissional")

    classificacoes = {
        "predominante": "Perfil predominante",
        "multifacetado": "Perfil multifacetado",
        "inconclusivo": "Perfil inconclusivo"
    }

    classificacao = diagnostico["classificacao"]

    st.markdown(
        f"**Classificação:** "
        f"{classificacoes[classificacao]}"
    )

    if classificacao == "inconclusivo":
        st.warning(diagnostico["mensagem"])
    else:
        st.info(diagnostico["mensagem"])

    # --------------------------------------------------------
    # TOP 3 DE CARREIRAS
    # --------------------------------------------------------

    st.markdown("### Top 3 — Carreiras mais compatíveis")

    for posicao, carreira in enumerate(
        resultado["top_3"],
        start=1
    ):

        percentual = carreira["compatibilidade_percentual"]

        st.markdown(
            f"**{posicao}º — {carreira['carreira']}**"
        )

        st.metric(
            label="Compatibilidade",
            value=f"{percentual:.2f}%"
        )

        st.progress(percentual / 100)

        st.caption(
            f"Compatibilidade-base: "
            f"{carreira['pontuacao_base']:.2f}% | "
            f"Ajustes das regras: "
            f"{carreira['ajuste_total']:+.2f} p.p."
        )

        regras = carreira["regras_acionadas"]

        if regras:

            with st.expander(
                f"Ver justificativas — {carreira['carreira']}"
            ):

                for regra in regras:

                    tipo = (
                        "Bônus"
                        if regra["tipo"] == "bonus"
                        else "Penalidade"
                    )

                    st.markdown(
                        f"**{regra['regra']} — {tipo} "
                        f"({regra['ajuste_percentual']:+.0f} p.p.)**"
                    )

                    st.write(regra["justificativa"])

        else:
            st.caption(
                "Nenhuma regra adicional foi acionada. "
                "A compatibilidade foi determinada "
                "pelos pesos das afinidades."
            )

        st.divider()

    # --------------------------------------------------------
    # GRÁFICO COMPARATIVO DAS DEZ CARREIRAS
    # --------------------------------------------------------

    st.markdown("### Comparativo geral de carreiras")

    st.write(
        "Visualize sua compatibilidade com todas as dez "
        "trilhas profissionais avaliadas pelo sistema."
    )

    # Nomes resumidos apenas para melhorar a leitura do gráfico.
    nomes_grafico = {
        "backend": "Back-end",
        "frontend": "Front-end & UI/UX",
        "ciencia_dados": "Ciência de Dados/ML",
        "engenharia_dados": "Eng. de Dados",
        "ciberseguranca": "Cibersegurança",
        "devops": "DevOps & SRE",
        "cloud": "Cloud",
        "mobile": "Mobile",
        "qa": "Qualidade (QA)",
        "produto": "Gestão de Produtos"
    }

    dados_grafico = [
        {
            "Carreira": nomes_grafico.get(
                carreira["id"],
                carreira["carreira"]
            ),
            "Compatibilidade (%)": carreira[
                "compatibilidade_percentual"
            ]
        }
        for carreira in resultado["ranking"]
    ]

    grafico = (
        alt.Chart(alt.Data(values=dados_grafico))
        .mark_bar(color="#37E8FF")
        .encode(
            x=alt.X(
                "Compatibilidade (%):Q",
                scale=alt.Scale(domain=[0, 100]),
                title="Compatibilidade (%)"
            ),
            y=alt.Y(
                "Carreira:N",
                sort=[item["Carreira"] for item in dados_grafico],
                title=None,
                axis=alt.Axis(labelLimit=180)
            ),
            tooltip=[
                alt.Tooltip("Carreira:N", title="Carreira"),
                alt.Tooltip(
                    "Compatibilidade (%):Q",
                    title="Compatibilidade (%)",
                    format=".2f"
                )
            ]
        )
        .properties(height=480)
    )

    st.altair_chart(grafico, use_container_width=True)


    st.markdown(
        """
        <p style="
            text-align: center;
            color: #8d9ba9;
            font-size: 0.85rem;
            margin-top: 1rem;
            line-height: 1.5;
        ">
            Os percentuais representam compatibilidade com os
            critérios do sistema, não probabilidades de
            sucesso profissional.
        </p>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # SELEÇÃO DA CARREIRA E AVALIAÇÃO DE COMPETÊNCIAS
    # --------------------------------------------------------

    st.divider()
    st.subheader("Seu desenvolvimento profissional")

    st.write(
        "Selecione uma das três carreiras recomendadas e avalie "
        "seus conhecimentos atuais. Com essas informações, "
        "poderemos identificar suas lacunas de competências "
        "e construir um plano de desenvolvimento personalizado."
    )

    carreiras_disponiveis = {
        carreira["id"]: carreira["carreira"]
        for carreira in resultado["top_3"]
    }

    carreira_escolhida = st.selectbox(
        "Qual carreira você deseja explorar?",
        options=list(carreiras_disponiveis),
        index=None,
        format_func=lambda identificador: (
            carreiras_disponiveis[identificador]
        ),
        placeholder="Selecione uma das carreiras recomendadas",
        key="carreira_roadmap",
        on_change=mudar_carreira_roadmap
    )

    if carreira_escolhida:
        st.markdown("### Avaliação das suas competências")
        st.caption(
            "Informe seu conhecimento atual em cada habilidade. "
            "Utilize a escala de 0 a 5, sendo 0 nenhum conhecimento "
            "e 5 domínio elevado."
        )

        requisitos = base["requisitos_junior"][carreira_escolhida]
        catalogo = base["competencias"]

        if "conhecimentos_roadmap" not in st.session_state:
            st.session_state["conhecimentos_roadmap"] = {}

        conhecimentos = st.session_state["conhecimentos_roadmap"]

        for competencia_id, nivel_junior in requisitos.items():
            chave = f"_conhecimento_{competencia_id}"

            # Restaura a resposta salva; None significa não respondido.
            st.session_state[chave] = conhecimentos.get(competencia_id)

            st.selectbox(
                label=catalogo[competencia_id],
                options=list(range(6)),
                index=None,
                format_func=lambda valor: f"Nível {valor} de 5",
                placeholder="Selecione seu nível atual",
                key=chave,
                on_change=salvar_conhecimento,
                args=(competencia_id,)
            )

            st.caption(f"Nível de referência Júnior: {nivel_junior} de 5")

        respondidas = sum(
            conhecimentos.get(competencia_id) is not None
            for competencia_id in requisitos
        )

        st.markdown(
            f"**Competências avaliadas: {respondidas} "
            f"de {len(requisitos)}**"
        )

        if respondidas == len(requisitos):
            st.success(
                "Todas as competências foram avaliadas! "
                "Seu perfil está preparado para a análise de lacunas."
            )

        st.button(
            "Gerar meu Roadmap",
            key="wizard_gerar_roadmap",
            on_click=gerar_roadmap,
            use_container_width=True,
            disabled=respondidas != len(requisitos)
        )

        # Só mostra o roadmap da carreira atualmente selecionada.
        plano_gerado = st.session_state.get("resultado_roadmap")

        if plano_gerado and plano_gerado["carreira_id"] == carreira_escolhida:
            st.divider()
            st.markdown(
                '<div id="resultado-roadmap"></div>',
                unsafe_allow_html=True
            )
            st.subheader("Seu Roadmap Personalizado")
            st.write(plano_gerado["mensagem"])

            coluna_cobertura, coluna_lacunas = st.columns(2)
            with coluna_cobertura:
                st.metric(
                    "Cobertura dos requisitos Júnior",
                    f"{plano_gerado['cobertura_percentual']:.2f}%"
                )
            with coluna_lacunas:
                st.metric(
                    "Lacunas identificadas",
                    plano_gerado["total_lacunas"]
                )

            st.markdown("### Plano de estudos prioritário")
            if plano_gerado["etapas_estudo"]:
                for item in plano_gerado["etapas_estudo"]:
                    st.markdown(
                        f"**{item['prioridade']}º — "
                        f"{item['competencia']} (Gap {item['gap']})**"
                    )
                    st.caption(
                        f"Seu nível: {item['nivel_atual']}/5 | "
                        f"Referência Júnior: {item['nivel_junior']}/5"
                    )
                    for conteudo in item["conteudos"]:
                        st.markdown(f"- {conteudo}")
            else:
                st.success(
                    "Nenhuma lacuna identificada segundo os níveis "
                    "de referência informados na base de conhecimento."
                )

            st.markdown("### Certificações sugeridas")
            if plano_gerado["certificacoes"]:
                for certificacao in plano_gerado["certificacoes"]:
                    st.markdown(f"**{certificacao['nome']}**")
                    st.caption(
                        "Relacionada às lacunas em: "
                        + ", ".join(certificacao["competencias_relacionadas"])
                    )
                    st.caption(certificacao["orientacao"])
            else:
                st.info(
                    "Não há certificações vinculadas às lacunas "
                    "identificadas. Isso não impede o desenvolvimento "
                    "do seu portfólio."
                )

            st.markdown("### Projeto para o portfólio GitHub")
            projeto = plano_gerado["projeto_portfolio"]
            st.markdown(f"**{projeto['titulo']}**")
            st.write(projeto["descricao"])

            if projeto["competencias_prioritarias"]:
                st.markdown("**Competências a priorizar no projeto:**")
                for competencia in projeto["competencias_prioritarias"]:
                    st.markdown(f"- {competencia}")

            st.caption(projeto["orientacao"])
            st.caption(
                "As referências Júnior são critérios acadêmicos. "
                "As certificações são sugestões opcionais e podem "
                "exigir conhecimentos adicionais."
            )

            if st.session_state.pop("rolar_para_roadmap", False):
                st.html(
                    """
                    <script>
                        setTimeout(() => {
                            const alvo = document.getElementById(
                                "resultado-roadmap"
                            );
                            if (alvo) {
                                alvo.scrollIntoView({
                                    behavior: "smooth",
                                    block: "start"
                                });
                            }
                        }, 250);
                    </script>
                    """,
                    unsafe_allow_javascript=True
                )

    # --------------------------------------------------------
    # ROLAGEM AUTOMÁTICA
    # --------------------------------------------------------

    if st.session_state.pop("rolar_para_resultado", False):

        st.html(
            """
            <script>
                (function () {
                    let tentativas = 0;

                    function rolarParaResultado() {
                        const alvo = document.getElementById(
                            "resultado-ponderado"
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

                    setTimeout(rolarParaResultado, 250);
                })();
            </script>
            """,
            unsafe_allow_javascript=True
        )

# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.markdown(
    """
    <p style="
        text-align: center;
        color: #8d9ba9;
        font-size: 0.85rem;
        margin-top: 0.5rem;
    ">
        Sistema especialista acadêmico para orientação
        de carreiras em Tecnologia da Informação.
    </p>
    """,
    unsafe_allow_html=True
)
