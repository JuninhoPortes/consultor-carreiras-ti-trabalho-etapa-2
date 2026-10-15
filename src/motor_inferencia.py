
"""Motor de inferência do sistema especialista."""

from src.compatibilidade import preparar_experta

preparar_experta()

from experta import KnowledgeEngine, Rule, OR
from src.fatos import RespostaUsuario, EvidenciaCarreira
from src.pontuacao import calcular_pontuacoes
from src.recomendacao import selecionar_carreira

class MotorInferencia(KnowledgeEngine):
    """Gerencia os fatos e executa as regras de inferência."""

    # R01 — Identificação de perfil Back-end
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="A"),
        RespostaUsuario(pergunta="Q02", alternativa="A")
    )
    def regra_r01_backend(self):
        """Identifica interesse em desenvolvimento Back-end."""

        self.declare(
            EvidenciaCarreira(
                carreira="Back-end",
                regra="R01",
                justificativa=(
                    "Interesse em desenvolver APIs e regras de negócio, "
                    "combinado à preferência por implementar algoritmos "
                    "e funcionalidades."
                )
            )
        )
    
    # R02 — Back-end: desenvolvimento e ferramentas
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="A"),
        OR(
            RespostaUsuario(pergunta="Q03", alternativa="A"),
            RespostaUsuario(pergunta="Q03", alternativa="C"),
            RespostaUsuario(pergunta="Q03", alternativa="D")
        )
    )
    def regra_r02_backend(self):
        """Identifica afinidade técnica com Back-end."""

        self.declare(
            EvidenciaCarreira(
                carreira="Back-end",
                regra="R02",
                justificativa=(
                    "Interesse em desenvolver APIs e regras de negócio, "
                    "combinado à familiaridade com Python, Java/C# "
                    "ou bancos de dados."
                )
            )
        )

    # R03 — Identificação de perfil Front-end & UI/UX
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="B"),
        RespostaUsuario(pergunta="Q02", alternativa="B")
    )
    def regra_r03_frontend(self):
        """Identifica interesse em Front-end e UI/UX."""

        self.declare(
            EvidenciaCarreira(
                carreira="Front-end & UI/UX",
                regra="R03",
                justificativa=(
                    "Interesse em desenvolver interfaces web, "
                    "combinado à preferência por criar experiências "
                    "visuais e interativas."
                )
            )
        )

    # R04 — Front-end: desenvolvimento e ferramentas
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="B"),
        RespostaUsuario(pergunta="Q03", alternativa="B")
    )
    def regra_r04_frontend(self):
        """Identifica afinidade técnica com Front-end e UI/UX."""

        self.declare(
            EvidenciaCarreira(
                carreira="Front-end & UI/UX",
                regra="R04",
                justificativa=(
                    "Interesse em desenvolver interfaces web, "
                    "combinado à familiaridade com JavaScript, "
                    "HTML e CSS."
                )
            )
        )
    
    # R05 — Ciência de Dados: modelos preditivos e matemática
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="A"),
        RespostaUsuario(pergunta="Q01", alternativa="C")
    )
    def regra_r05_ciencia_dados(self):
        """Identifica afinidade com Ciência de Dados e ML."""

        self.declare(
            EvidenciaCarreira(
                carreira="Ciência de Dados e ML",
                regra="R05",
                justificativa=(
                    "Interesse em analisar dados e construir modelos "
                    "preditivos, combinado à alta afinidade com "
                    "matemática e estatística."
                )
            )
        )
    
    # R06 — Ciência de Dados: análise e identificação de padrões
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="A"),
        RespostaUsuario(pergunta="Q02", alternativa="C")
    )
    def regra_r06_ciencia_dados(self):
        """Identifica interesse em análise de dados e ML."""

        self.declare(
            EvidenciaCarreira(
                carreira="Ciência de Dados e ML",
                regra="R06",
                justificativa=(
                    "Interesse em desenvolver modelos preditivos, "
                    "combinado à preferência por analisar dados "
                    "e identificar padrões."
                )
            )
        )
    
    # R07 — Engenharia de Dados: processamento e transformação
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="B"),
        RespostaUsuario(pergunta="Q02", alternativa="D")
    )
    def regra_r07_engenharia_dados(self):
        """Identifica interesse em Engenharia de Dados."""

        self.declare(
            EvidenciaCarreira(
                carreira="Engenharia de Dados",
                regra="R07",
                justificativa=(
                    "Interesse em construir processos de coleta, "
                    "transformação e disponibilização de dados, "
                    "combinado à preferência por organizar "
                    "e processar grandes volumes de informações."
                )
            )
        )
    
    # R08 — Engenharia de Dados: pipelines e bancos de dados
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="B"),
        RespostaUsuario(pergunta="Q03", alternativa="D")
    )
    def regra_r08_engenharia_dados(self):
        """Identifica afinidade técnica com Engenharia de Dados."""

        self.declare(
            EvidenciaCarreira(
                carreira="Engenharia de Dados",
                regra="R08",
                justificativa=(
                    "Interesse em construir pipelines de coleta e "
                    "transformação de dados, combinado à "
                    "familiaridade com SQL e bancos de dados."
                )
            )
        )
    
    # R09 — Cibersegurança: investigação e proteção de sistemas
    @Rule(
        RespostaUsuario(pergunta="Q09", alternativa="A"),
        RespostaUsuario(pergunta="Q02", alternativa="F")
    )
    def regra_r09_ciberseguranca(self):
        """Identifica interesse em Cibersegurança."""

        self.declare(
            EvidenciaCarreira(
                carreira="Cibersegurança",
                regra="R09",
                justificativa=(
                    "Interesse em investigar vulnerabilidades e "
                    "proteger sistemas contra ataques, combinado "
                    "à preferência por identificar falhas, "
                    "vulnerabilidades e riscos."
                )
            )
        )
    
    # R10 — Cibersegurança: segurança de redes e sistemas
    @Rule(
        RespostaUsuario(pergunta="Q09", alternativa="A"),
        RespostaUsuario(pergunta="Q03", alternativa="E")
    )
    def regra_r10_ciberseguranca(self):
        """Identifica afinidade técnica com Cibersegurança."""

        self.declare(
            EvidenciaCarreira(
                carreira="Cibersegurança",
                regra="R10",
                justificativa=(
                    "Interesse em investigar vulnerabilidades e "
                    "proteger sistemas contra ataques, combinado "
                    "à familiaridade com Linux e redes."
                )
            )
        )
    
    # R11 — DevOps & SRE: automação e integração contínua
    @Rule(
        RespostaUsuario(pergunta="Q07", alternativa="A"),
        RespostaUsuario(pergunta="Q03", alternativa="F")
    )
    def regra_r11_devops(self):
        """Identifica afinidade técnica com DevOps e SRE."""

        self.declare(
            EvidenciaCarreira(
                carreira="DevOps & SRE",
                regra="R11",
                justificativa=(
                    "Interesse em automatizar implantações, "
                    "monitorar aplicações e melhorar sua "
                    "confiabilidade, combinado à familiaridade "
                    "com Docker e ferramentas de CI/CD."
                )
            )
        )
    
    # R12 — DevOps & SRE: infraestrutura e automação
    @Rule(
        RespostaUsuario(pergunta="Q07", alternativa="A"),
        RespostaUsuario(pergunta="Q02", alternativa="E")
    )
    def regra_r12_devops(self):
        """Identifica interesse em infraestrutura e automação."""

        self.declare(
            EvidenciaCarreira(
                carreira="DevOps & SRE",
                regra="R12",
                justificativa=(
                    "Interesse em automatizar implantações e "
                    "garantir a confiabilidade das aplicações, "
                    "combinado à preferência por configurar "
                    "servidores e automatizar processos."
                )
            )
        )
    
    # R13 — Cloud: arquitetura e plataformas em nuvem
    @Rule(
        RespostaUsuario(pergunta="Q07", alternativa="B"),
        RespostaUsuario(pergunta="Q03", alternativa="G")
    )
    def regra_r13_cloud(self):
        """Identifica afinidade técnica com Computação em Nuvem."""

        self.declare(
            EvidenciaCarreira(
                carreira="Computação em Nuvem",
                regra="R13",
                justificativa=(
                    "Interesse em projetar arquiteturas e ambientes "
                    "em nuvem, combinado à familiaridade com "
                    "plataformas AWS, Azure ou Google Cloud."
                )
            )
        )
    
    # R14 — Cloud: arquitetura e infraestrutura escalável
    @Rule(
        RespostaUsuario(pergunta="Q07", alternativa="B"),
        RespostaUsuario(pergunta="Q05", alternativa="D")
    )
    def regra_r14_cloud(self):
        """Identifica interesse em arquitetura e infraestrutura em nuvem."""

        self.declare(
            EvidenciaCarreira(
                carreira="Computação em Nuvem",
                regra="R14",
                justificativa=(
                    "Interesse em projetar ambientes e arquiteturas "
                    "em nuvem, combinado à preferência por trabalhar "
                    "com servidores, redes e infraestrutura escalável."
                )
            )
        )
    
    # R15 — Mobile: aplicativos e tecnologias móveis
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="C"),
        RespostaUsuario(pergunta="Q03", alternativa="H")
    )
    def regra_r15_mobile(self):
        """Identifica afinidade técnica com Desenvolvimento Mobile."""

        self.declare(
            EvidenciaCarreira(
                carreira="Desenvolvimento Mobile",
                regra="R15",
                justificativa=(
                    "Interesse em desenvolver aplicativos para "
                    "smartphones e tablets, combinado à familiaridade "
                    "com Flutter, React Native ou tecnologias "
                    "de desenvolvimento mobile."
                )
            )
        )
    
    # R16 — Mobile: desenvolvimento e aplicações móveis
    @Rule(
        RespostaUsuario(pergunta="Q08", alternativa="C"),
        RespostaUsuario(pergunta="Q05", alternativa="B")
    )
    def regra_r16_mobile(self):
        """Identifica interesse em desenvolver aplicações móveis."""

        self.declare(
            EvidenciaCarreira(
                carreira="Desenvolvimento Mobile",
                regra="R16",
                justificativa=(
                    "Interesse em desenvolver aplicativos para "
                    "smartphones e tablets, combinado à preferência "
                    "por trabalhar com interfaces e aplicações móveis."
                )
            )
        )
    
    # R17 — QA: automação de testes e qualidade de software
    @Rule(
        RespostaUsuario(pergunta="Q09", alternativa="B"),
        RespostaUsuario(pergunta="Q03", alternativa="I")
    )
    def regra_r17_qa(self):
        """Identifica afinidade técnica com Engenharia de Qualidade."""

        self.declare(
            EvidenciaCarreira(
                carreira="Engenharia de Qualidade (QA)",
                regra="R17",
                justificativa=(
                    "Interesse em identificar defeitos e automatizar "
                    "testes para garantir a qualidade do software, "
                    "combinado à familiaridade com ferramentas "
                    "de testes e automação."
                )
            )
        )
    
    # R18 — QA: qualidade e confiabilidade de software
    @Rule(
        RespostaUsuario(pergunta="Q09", alternativa="B"),
        RespostaUsuario(pergunta="Q04", alternativa="E")
    )
    def regra_r18_qa(self):
        """Identifica interesse em qualidade e testes de software."""

        self.declare(
            EvidenciaCarreira(
                carreira="Engenharia de Qualidade (QA)",
                regra="R18",
                justificativa=(
                    "Interesse em identificar defeitos e automatizar "
                    "testes, combinado à preferência por garantir "
                    "a segurança e a qualidade dos sistemas."
                )
            )
        )
    
    # R19 — Gestão de Produtos: planejamento e prioridades
    @Rule(
        RespostaUsuario(pergunta="Q10", alternativa="A"),
        RespostaUsuario(pergunta="Q02", alternativa="G")
    )
    def regra_r19_gestao_produtos(self):
        """Identifica interesse em Gestão de Produtos."""

        self.declare(
            EvidenciaCarreira(
                carreira="Gestão de Produtos",
                regra="R19",
                justificativa=(
                    "Interesse em definir prioridades e compreender "
                    "as necessidades dos usuários, combinado à "
                    "preferência por planejar funcionalidades "
                    "e orientar decisões de produto."
                )
            )
        )
    
    # R20 — Gestão de Produtos: estratégia e resultados de negócio
    @Rule(
        RespostaUsuario(pergunta="Q10", alternativa="A"),
        RespostaUsuario(pergunta="Q04", alternativa="F")
    )
    def regra_r20_gestao_produtos(self):
        """Identifica afinidade com estratégia e gestão de produtos."""

        self.declare(
            EvidenciaCarreira(
                carreira="Gestão de Produtos",
                regra="R20",
                justificativa=(
                    "Interesse em definir prioridades e orientar "
                    "o desenvolvimento de produtos, combinado "
                    "à preferência por contribuir para decisões "
                    "estratégicas e resultados de negócio."
                )
            )
        )
        
    # R21 — Diferenciação: Ciência de Dados x Engenharia de Dados
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="A"),
        RespostaUsuario(pergunta="Q01", alternativa="C"),
        RespostaUsuario(pergunta="Q03", alternativa="D")
    )
    def regra_r21_diferenciacao_ciencia_dados(self):
        """Diferencia Ciência de Dados de Engenharia de Dados."""

        self.declare(
            EvidenciaCarreira(
                carreira="Ciência de Dados e ML",
                regra="R21",
                justificativa=(
                    "Apesar da familiaridade com SQL e bancos de dados, "
                    "o interesse em modelos preditivos e a alta "
                    "afinidade com matemática e estatística indicam "
                    "maior alinhamento com Ciência de Dados."
                )
            )
        )
    
    # R22 — Diferenciação: Engenharia de Dados x Ciência de Dados
    @Rule(
        RespostaUsuario(pergunta="Q06", alternativa="B"),
        RespostaUsuario(pergunta="Q02", alternativa="D"),
        RespostaUsuario(pergunta="Q03", alternativa="A")
    )
    def regra_r22_diferenciacao_engenharia_dados(self):
        """Diferencia Engenharia de Dados de Ciência de Dados."""

        self.declare(
            EvidenciaCarreira(
                carreira="Engenharia de Dados",
                regra="R22",
                justificativa=(
                    "Apesar da familiaridade com Python, "
                    "o interesse em construir pipelines de dados "
                    "e a preferência por organizar e transformar "
                    "grandes volumes de informações indicam maior "
                    "alinhamento com Engenharia de Dados."
                )
            )
        )
    
    # R23 — Diferenciação: DevOps & SRE x Computação em Nuvem
    @Rule(
        RespostaUsuario(pergunta="Q07", alternativa="A"),
        RespostaUsuario(pergunta="Q03", alternativa="G"),
        RespostaUsuario(pergunta="Q02", alternativa="E")
    )
    def regra_r23_diferenciacao_devops(self):
        """Diferencia DevOps & SRE de Computação em Nuvem."""

        self.declare(
            EvidenciaCarreira(
                carreira="DevOps & SRE",
                regra="R23",
                justificativa=(
                    "Apesar da familiaridade com plataformas de nuvem, "
                    "o interesse em automatizar implantações, monitorar "
                    "aplicações e garantir sua confiabilidade, "
                    "combinado à preferência por servidores e "
                    "automação, indica maior alinhamento com "
                    "DevOps & SRE."
                )
            )
        )
    
    # R24 — Diferenciação: Computação em Nuvem x DevOps & SRE
    @Rule(
        RespostaUsuario(pergunta="Q07", alternativa="B"),
        RespostaUsuario(pergunta="Q03", alternativa="F"),
        RespostaUsuario(pergunta="Q04", alternativa="D")
    )
    def regra_r24_diferenciacao_cloud(self):
        """Diferencia Computação em Nuvem de DevOps & SRE."""

        self.declare(
            EvidenciaCarreira(
                carreira="Computação em Nuvem",
                regra="R24",
                justificativa=(
                    "Apesar da familiaridade com Docker e ferramentas "
                    "de CI/CD, o interesse em projetar arquiteturas "
                    "em nuvem e trabalhar com infraestrutura "
                    "estável e escalável indica maior alinhamento "
                    "com Computação em Nuvem."
                )
            )
        )
    
    # R25 — Diferenciação: Engenharia de Qualidade x Cibersegurança
    @Rule(
        RespostaUsuario(pergunta="Q09", alternativa="B"),
        RespostaUsuario(pergunta="Q02", alternativa="F"),
        RespostaUsuario(pergunta="Q03", alternativa="I")
    )
    def regra_r25_diferenciacao_qa(self):
        """Diferencia Engenharia de Qualidade de Cibersegurança."""

        self.declare(
            EvidenciaCarreira(
                carreira="Engenharia de Qualidade (QA)",
                regra="R25",
                justificativa=(
                    "Apesar do interesse em investigar falhas e riscos, "
                    "a preferência por automatizar testes e a "
                    "familiaridade com ferramentas de qualidade "
                    "indicam maior alinhamento com Engenharia "
                    "de Qualidade e Testes."
                )
            )
        )


    
    def analisar(self, respostas: dict[str, str]) -> dict[str, int]:
        """Executa as regras e retorna as pontuações elegíveis."""

        self.reset()

        # Registra as respostas do usuário.
        for pergunta, alternativa in respostas.items():
            self.declare(
                RespostaUsuario(
                    pergunta=pergunta,
                    alternativa=alternativa
                )
            )

        # Executa as regras de inferência.
        self.run()

        # Calcula as pontuações das carreiras.
        pontuacoes = calcular_pontuacoes(respostas)

        # Identifica as regras que permitem uma recomendação.
        regras_identificacao = {
            f"R{i:02d}" for i in range(1, 21)
        }

        # Identifica as carreiras com regras disparadas.
        carreiras_elegiveis = {
            fato["carreira"]
            for fato in self.facts.values()
            if isinstance(fato, EvidenciaCarreira)
            and fato["regra"] in regras_identificacao
        }

        # Retorna somente as pontuações das carreiras elegíveis.
        return {
            carreira: pontos
            for carreira, pontos in pontuacoes.items()
            if carreira in carreiras_elegiveis
        }

    
    def gerar_resultado(self, respostas: dict[str, str]) -> dict:
        """Gera a recomendação profissional com justificativas."""

        # Executa as regras e obtém as pontuações elegíveis.
        pontuacoes = self.analisar(respostas)

        # Seleciona a carreira considerando os desempates.
        carreira = selecionar_carreira(pontuacoes, respostas)

        # Verifica se foi possível definir uma carreira.
        if carreira is None:
            return {
                "carreira": None,
                "pontuacao": None,
                "justificativas": [],
                "mensagem": (
                    "Informações insuficientes ou empate não resolvido. "
                    "São necessárias respostas adicionais."
                )
            }

        # Recupera as justificativas das regras disparadas.
        justificativas = [
            {
                "regra": fato["regra"],
                "motivo": fato["justificativa"]
            }
            for fato in self.facts.values()
            if isinstance(fato, EvidenciaCarreira)
            and fato["carreira"] == carreira
        ]

        # Organiza as justificativas pelo identificador da regra.
        justificativas.sort(key=lambda item: item["regra"])

        return {
            "carreira": carreira,
            "pontuacao": pontuacoes[carreira],
            "justificativas": justificativas,
            "mensagem": "Recomendação realizada com sucesso."
        }


