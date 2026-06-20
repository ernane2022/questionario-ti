from django.contrib import admin
from .models import RespostaProfissional, RespostaEstudante, RespostaPublico


@admin.register(RespostaProfissional)
class RespostaProfissionalAdmin(admin.ModelAdmin):
    list_display = ["id", "area_atuacao", "tempo_atuacao", "regime_trabalho", "estado", "cidade", "criado_em"]
    list_filter  = ["area_atuacao", "tempo_atuacao", "regime_trabalho", "faixa_etaria", "estado"]
    search_fields = ["cidade", "stack_principal", "maior_dificuldade"]
    readonly_fields = ["criado_em"]
    date_hierarchy = "criado_em"


@admin.register(RespostaEstudante)
class RespostaEstudanteAdmin(admin.ModelAdmin):
    list_display = ["id", "curso", "instituicao", "semestre", "turno", "estado", "criado_em"]
    list_filter  = ["semestre", "turno", "motivo_escolha", "possui_estagio", "estado"]
    search_fields = ["curso", "instituicao", "cidade"]
    readonly_fields = ["criado_em"]
    date_hierarchy = "criado_em"


@admin.register(RespostaPublico)
class RespostaPublicoAdmin(admin.ModelAdmin):
    list_display = ["id", "frequencia_uso_tecnologia", "confianca_sistemas", "associa_ti_a", "estado", "criado_em"]
    list_filter  = ["frequencia_uso_tecnologia", "confianca_sistemas", "impacto_ia", "estado"]
    search_fields = ["cidade", "percepcao_profissao"]
    readonly_fields = ["criado_em"]
    date_hierarchy = "criado_em"