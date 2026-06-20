from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Row, Column
from .models import RespostaProfissional, RespostaEstudante, RespostaPublico

COMP_TEC_CHOICES = [
    ("python", "Python"),
    ("javascript", "JavaScript"),
    ("java", "Java"),
    ("sql", "SQL / Banco de Dados"),
    ("cloud", "Cloud Computing"),
    ("devops", "DevOps / CI-CD"),
    ("seguranca", "Segurança da Informação"),
    ("machine_learning", "Machine Learning / IA"),
    ("redes", "Redes e Infraestrutura"),
    ("mobile", "Desenvolvimento Mobile"),
]
COMP_COMP_CHOICES = [
    ("comunicacao", "Comunicação"),
    ("trabalho_equipe", "Trabalho em equipe"),
    ("resolucao_problemas", "Resolução de problemas"),
    ("aprendizado_continuo", "Aprendizado contínuo"),
    ("organizacao", "Organização e planejamento"),
    ("criatividade", "Criatividade"),
    ("lideranca", "Liderança"),
    ("adaptabilidade", "Adaptabilidade"),
]

BLOCO_PERFIL = [
    Row(Column("faixa_etaria", css_class="col-md-6"), Column("genero", css_class="col-md-6")),
    Row(Column("escolaridade", css_class="col-md-6")),
    Row(Column("estado", css_class="col-md-3"), Column("cidade", css_class="col-md-9")),
]


class RespostaProfissionalForm(forms.ModelForm):
    competencias_tecnicas_check = forms.MultipleChoiceField(
        label="Competências técnicas mais valorizadas",
        choices=COMP_TEC_CHOICES, widget=forms.CheckboxSelectMultiple, required=False,
    )
    competencias_comportamentais_check = forms.MultipleChoiceField(
        label="Competências comportamentais mais valorizadas",
        choices=COMP_COMP_CHOICES, widget=forms.CheckboxSelectMultiple, required=False,
    )

    class Meta:
        model = RespostaProfissional
        exclude = ["perfil", "competencias_tecnicas", "competencias_comportamentais", "criado_em"]
        widgets = {
            "maior_dificuldade": forms.Textarea(attrs={"rows": 3}),
            "conselho_iniciante": forms.Textarea(attrs={"rows": 3}),
            "percepcao_profissao": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            HTML("<h4 class='mt-4 mb-3 text-primary'>📋 Bloco I – Perfil</h4>"),
            *BLOCO_PERFIL,
            HTML("<hr><h4 class='mt-4 mb-3 text-primary'>📊 Bloco II – Percepção do Mercado</h4>"),
            "percebe_mercado",
            HTML("<hr><h4 class='mt-4 mb-3 text-primary'>💼 Bloco III – Atuação Profissional</h4>"),
            Row(Column("area_atuacao", css_class="col-md-6"), Column("tempo_atuacao", css_class="col-md-6")),
            Row(Column("regime_trabalho", css_class="col-md-6")),
            Row(Column("trabalha_remoto", css_class="col-md-6"), Column("atualizacao_constante", css_class="col-md-6")),
            "stack_principal",
            Fieldset("Competências Técnicas", "competencias_tecnicas_check"),
            Fieldset("Competências Comportamentais", "competencias_comportamentais_check"),
            HTML("<hr><h4 class='mt-4 mb-3 text-primary'>💬 Bloco IV – Questões Abertas</h4>"),
            "maior_dificuldade",
            "conselho_iniciante",
            "percepcao_profissao",
            HTML("<hr>"),
            Submit("submit", "Enviar Respostas", css_class="btn btn-success btn-lg w-100 mt-3"),
        )

    def save(self, commit=True):
        inst = super().save(commit=False)
        inst.competencias_tecnicas = ",".join(self.cleaned_data.get("competencias_tecnicas_check", []))
        inst.competencias_comportamentais = ",".join(self.cleaned_data.get("competencias_comportamentais_check", []))
        if commit:
            inst.save()
        return inst


class RespostaEstudanteForm(forms.ModelForm):
    competencias_tecnicas_check = forms.MultipleChoiceField(
        label="Competências técnicas mais importantes",
        choices=COMP_TEC_CHOICES, widget=forms.CheckboxSelectMultiple, required=False,
    )
    competencias_comportamentais_check = forms.MultipleChoiceField(
        label="Competências comportamentais mais importantes",
        choices=COMP_COMP_CHOICES, widget=forms.CheckboxSelectMultiple, required=False,
    )

    class Meta:
        model = RespostaEstudante
        exclude = ["perfil", "competencias_tecnicas", "competencias_comportamentais", "criado_em"]
        widgets = {
            "dificuldade_academica": forms.Textarea(attrs={"rows": 3}),
            "expectativa_carreira": forms.Textarea(attrs={"rows": 3}),
            "conselho_iniciante": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            HTML("<h4 class='mt-4 mb-3 text-primary'>📋 Bloco I – Perfil</h4>"),
            *BLOCO_PERFIL,
            HTML("<hr><h4 class='mt-4 mb-3 text-primary'>📊 Bloco II – Percepção do Mercado</h4>"),
            "percebe_mercado",
            HTML("<hr><h4 class='mt-4 mb-3 text-primary'>🎓 Bloco III – Formação Acadêmica</h4>"),
            Row(Column("curso", css_class="col-md-8"), Column("semestre", css_class="col-md-4")),
            Row(Column("instituicao", css_class="col-md-8"), Column("turno", css_class="col-md-4")),
            Row(Column("motivo_escolha", css_class="col-md-6"), Column("possui_estagio", css_class="col-md-6")),
            Fieldset("Competências Técnicas", "competencias_tecnicas_check"),
            Fieldset("Competências Comportamentais", "competencias_comportamentais_check"),
            HTML("<hr><h4 class='mt-4 mb-3 text-primary'>💬 Bloco IV – Questões Abertas</h4>"),
            "dificuldade_academica",
            "expectativa_carreira",
            "conselho_iniciante",
            HTML("<hr>"),
            Submit("submit", "Enviar Respostas", css_class="btn btn-success btn-lg w-100 mt-3"),
        )

    def save(self, commit=True):
        inst = super().save(commit=False)
        inst.competencias_tecnicas = ",".join(self.cleaned_data.get("competencias_tecnicas_check", []))
        inst.competencias_comportamentais = ",".join(self.cleaned_data.get("competencias_comportamentais_check", []))
        if commit:
            inst.save()
        return inst


class RespostaPublicoForm(forms.ModelForm):
    class Meta:
        model = RespostaPublico
        exclude = ["perfil", "criado_em"]
        widgets = {
            "percepcao_profissao": forms.Textarea(attrs={"rows": 3}),
            "uso_tecnologia_cotidiano": forms.Textarea(attrs={"rows": 3}),
            "preocupacao_digital": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            HTML("<h4 class='mt-4 mb-3 text-primary'>📋 Bloco I – Perfil</h4>"),
            *BLOCO_PERFIL,
            HTML("<hr><h4 class='mt-4 mb-3 text-primary'>📊 Bloco II – Percepção do Mercado</h4>"),
            "percebe_mercado",
            HTML("<hr><h4 class='mt-4 mb-3 text-primary'>💻 Bloco III – Tecnologia no Cotidiano</h4>"),
            Row(Column("frequencia_uso_tecnologia", css_class="col-md-6"), Column("confianca_sistemas", css_class="col-md-6")),
            Row(Column("associa_ti_a", css_class="col-md-6")),
            Row(Column("conhece_profissional_ti", css_class="col-md-6"), Column("impacto_ia", css_class="col-md-6")),
            HTML("<hr><h4 class='mt-4 mb-3 text-primary'>💬 Bloco IV – Questões Abertas</h4>"),
            "percepcao_profissao",
            "uso_tecnologia_cotidiano",
            "preocupacao_digital",
            HTML("<hr>"),
            Submit("submit", "Enviar Respostas", css_class="btn btn-success btn-lg w-100 mt-3"),
        )