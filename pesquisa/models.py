from django.db import models

PERFIL_CHOICES = [
    ("profissional", "Profissional de TI"),
    ("estudante", "Estudante de TI / Área afim"),
    ("publico", "Público Geral"),
]
FAIXA_ETARIA_CHOICES = [
    ("ate18", "Até 18 anos"),
    ("19_24", "19 – 24 anos"),
    ("25_34", "25 – 34 anos"),
    ("35_44", "35 – 44 anos"),
    ("45mais", "45 anos ou mais"),
]
ESCOLARIDADE_CHOICES = [
    ("fundamental", "Ensino Fundamental"),
    ("medio", "Ensino Médio"),
    ("superior_inc", "Superior Incompleto"),
    ("superior_comp", "Superior Completo"),
    ("pos", "Pós-graduação / Mestrado / Doutorado"),
]
GENERO_CHOICES = [
    ("masculino", "Masculino"),
    ("feminino", "Feminino"),
    ("nao_binario", "Não-binário"),
    ("prefiro_nao", "Prefiro não informar"),
]
UF_CHOICES = [
    ("AC", "AC – Acre"), ("AL", "AL – Alagoas"), ("AP", "AP – Amapá"),
    ("AM", "AM – Amazonas"), ("BA", "BA – Bahia"), ("CE", "CE – Ceará"),
    ("DF", "DF – Distrito Federal"), ("ES", "ES – Espírito Santo"),
    ("GO", "GO – Goiás"), ("MA", "MA – Maranhão"), ("MT", "MT – Mato Grosso"),
    ("MS", "MS – Mato Grosso do Sul"), ("MG", "MG – Minas Gerais"),
    ("PA", "PA – Pará"), ("PB", "PB – Paraíba"), ("PR", "PR – Paraná"),
    ("PE", "PE – Pernambuco"), ("PI", "PI – Piauí"), ("RJ", "RJ – Rio de Janeiro"),
    ("RN", "RN – Rio Grande do Norte"), ("RS", "RS – Rio Grande do Sul"),
    ("RO", "RO – Rondônia"), ("RR", "RR – Roraima"), ("SC", "SC – Santa Catarina"),
    ("SP", "SP – São Paulo"), ("SE", "SE – Sergipe"), ("TO", "TO – Tocantins"),
]

MERCADO_CHOICES = [
    ("muito_aquecido", "Muito aquecido"),
    ("aquecido", "Aquecido"),
    ("estavel", "Estável"),
    ("desaquecido", "Desaquecido"),
    ("nao_sei", "Não sei avaliar"),
]


class RespostaProfissional(models.Model):
    AREA_TI_CHOICES = [
        ("desenvolvimento", "Desenvolvimento de Software"),
        ("infra", "Infraestrutura / Redes"),
        ("dados", "Ciência de Dados / BI"),
        ("seguranca", "Segurança da Informação"),
        ("suporte", "Suporte Técnico"),
        ("gestao", "Gestão de TI"),
        ("ia", "Inteligência Artificial"),
        ("mobile", "Desenvolvimento Mobile"),
        ("outro", "Outra"),
    ]
    TEMPO_ATUACAO_CHOICES = [
        ("menos1", "Menos de 1 ano"),
        ("1_3", "1 – 3 anos"),
        ("4_7", "4 – 7 anos"),
        ("8mais", "8 anos ou mais"),
    ]
    REGIME_CHOICES = [
        ("clt", "CLT"),
        ("pj", "PJ / Freelancer"),
        ("servidor", "Servidor Público"),
        ("socio", "Sócio / Empreendedor"),
        ("outro", "Outro"),
    ]

    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES, default="profissional", editable=False)
    faixa_etaria = models.CharField("Faixa etária", max_length=10, choices=FAIXA_ETARIA_CHOICES)
    genero = models.CharField("Gênero", max_length=20, choices=GENERO_CHOICES)
    escolaridade = models.CharField("Escolaridade", max_length=20, choices=ESCOLARIDADE_CHOICES)
    estado = models.CharField("Estado (UF)", max_length=2, choices=UF_CHOICES)
    cidade = models.CharField("Cidade", max_length=100)
    percebe_mercado = models.CharField("Como percebe o mercado de TI atualmente", max_length=20, choices=MERCADO_CHOICES)
    area_atuacao = models.CharField("Área de atuação", max_length=30, choices=AREA_TI_CHOICES)
    tempo_atuacao = models.CharField("Tempo de atuação", max_length=10, choices=TEMPO_ATUACAO_CHOICES)
    regime_trabalho = models.CharField("Regime de trabalho", max_length=20, choices=REGIME_CHOICES)
    trabalha_remoto = models.BooleanField("Trabalha remotamente?", default=False)
    atualizacao_constante = models.BooleanField("Acredita que atualização constante é necessária?", default=True)
    competencias_tecnicas = models.TextField("Competências técnicas mais valorizadas", blank=True)
    competencias_comportamentais = models.TextField("Competências comportamentais mais valorizadas", blank=True)
    stack_principal = models.CharField("Principal stack/tecnologia que usa", max_length=200, blank=True)
    maior_dificuldade = models.TextField("Maior dificuldade ao ingressar na área", blank=True)
    conselho_iniciante = models.TextField("Conselho para quem está iniciando", blank=True)
    percepcao_profissao = models.TextField("Como a sociedade percebe o profissional de TI?", blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Resposta – Profissional"
        verbose_name_plural = "Respostas – Profissionais"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"Profissional – {self.cidade}/{self.estado} ({self.criado_em:%d/%m/%Y})"


class RespostaEstudante(models.Model):
    SEMESTRE_CHOICES = [(str(i), f"{i}º semestre") for i in range(1, 11)]
    TURNO_CHOICES = [
        ("manha", "Manhã"),
        ("tarde", "Tarde"),
        ("noite", "Noite"),
        ("ead", "EAD"),
    ]
    MOTIVO_CHOICES = [
        ("mercado", "Mercado de trabalho aquecido"),
        ("vocacao", "Vocação / paixão pela área"),
        ("salario", "Salário atrativo"),
        ("influencia", "Influência de familiares/amigos"),
        ("outro", "Outro"),
    ]

    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES, default="estudante", editable=False)
    faixa_etaria = models.CharField("Faixa etária", max_length=10, choices=FAIXA_ETARIA_CHOICES)
    genero = models.CharField("Gênero", max_length=20, choices=GENERO_CHOICES)
    escolaridade = models.CharField("Escolaridade", max_length=20, choices=ESCOLARIDADE_CHOICES)
    estado = models.CharField("Estado (UF)", max_length=2, choices=UF_CHOICES)
    cidade = models.CharField("Cidade", max_length=100)
    percebe_mercado = models.CharField("Como percebe o mercado de TI atualmente", max_length=20, choices=MERCADO_CHOICES)
    curso = models.CharField("Curso", max_length=100)
    instituicao = models.CharField("Instituição de ensino", max_length=150)
    semestre = models.CharField("Semestre atual", max_length=5, choices=SEMESTRE_CHOICES)
    turno = models.CharField("Turno", max_length=10, choices=TURNO_CHOICES)
    motivo_escolha = models.CharField("Motivo da escolha do curso", max_length=20, choices=MOTIVO_CHOICES)
    possui_estagio = models.BooleanField("Possui ou já teve estágio na área?", default=False)
    competencias_tecnicas = models.TextField("Competências técnicas que considera mais importantes", blank=True)
    competencias_comportamentais = models.TextField("Competências comportamentais mais importantes", blank=True)
    dificuldade_academica = models.TextField("Principal dificuldade na graduação", blank=True)
    expectativa_carreira = models.TextField("Quais suas expectativas para a carreira?", blank=True)
    conselho_iniciante = models.TextField("Que conselho daria a quem quer entrar na área?", blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Resposta – Estudante"
        verbose_name_plural = "Respostas – Estudantes"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"Estudante – {self.curso} – {self.cidade}/{self.estado} ({self.criado_em:%d/%m/%Y})"


class RespostaPublico(models.Model):
    USO_TI_CHOICES = [
        ("diario", "Diariamente"),
        ("frequente", "Frequentemente"),
        ("ocasional", "Ocasionalmente"),
        ("raramente", "Raramente"),
        ("nunca", "Nunca"),
    ]
    CONFIANCA_CHOICES = [
        ("muita", "Muita confiança"),
        ("moderada", "Confiança moderada"),
        ("pouca", "Pouca confiança"),
        ("nenhuma", "Nenhuma confiança"),
    ]
    ASSOCIA_TI_CHOICES = [
        ("programacao", "Programação"),
        ("conserto", "Conserto de computadores"),
        ("jogos", "Desenvolvimento de jogos"),
        ("redes", "Redes / Internet"),
        ("ia", "Inteligência Artificial"),
        ("nao_sei", "Não sei definir"),
    ]

    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES, default="publico", editable=False)
    faixa_etaria = models.CharField("Faixa etária", max_length=10, choices=FAIXA_ETARIA_CHOICES)
    genero = models.CharField("Gênero", max_length=20, choices=GENERO_CHOICES)
    escolaridade = models.CharField("Escolaridade", max_length=20, choices=ESCOLARIDADE_CHOICES)
    estado = models.CharField("Estado (UF)", max_length=2, choices=UF_CHOICES)
    cidade = models.CharField("Cidade", max_length=100)
    percebe_mercado = models.CharField("Como percebe o mercado de TI atualmente", max_length=20, choices=MERCADO_CHOICES)
    frequencia_uso_tecnologia = models.CharField("Com que frequência usa tecnologia digital?", max_length=15, choices=USO_TI_CHOICES)
    confianca_sistemas = models.CharField("Qual seu nível de confiança em sistemas digitais?", max_length=15, choices=CONFIANCA_CHOICES)
    associa_ti_a = models.CharField("Quando pensa em TI, o que vem à mente?", max_length=20, choices=ASSOCIA_TI_CHOICES)
    conhece_profissional_ti = models.BooleanField("Conhece pessoalmente algum profissional de TI?", default=False)
    impacto_ia = models.BooleanField("Acredita que a IA impactará sua vida nos próximos anos?", default=True)
    percepcao_profissao = models.TextField("Como você enxerga os profissionais de TI?", blank=True)
    uso_tecnologia_cotidiano = models.TextField("Como a tecnologia está presente no seu dia a dia?", blank=True)
    preocupacao_digital = models.TextField("Tem alguma preocupação com o uso de tecnologia?", blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Resposta – Público Geral"
        verbose_name_plural = "Respostas – Público Geral"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"Público – {self.cidade}/{self.estado} ({self.criado_em:%d/%m/%Y})"