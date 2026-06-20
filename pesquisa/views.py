from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.http import HttpResponse
from collections import Counter

from .models import RespostaProfissional, RespostaEstudante, RespostaPublico
from .forms import RespostaProfissionalForm, RespostaEstudanteForm, RespostaPublicoForm
from .export import exportar_excel_multi


def index(request):
    total = (
        RespostaProfissional.objects.count()
        + RespostaEstudante.objects.count()
        + RespostaPublico.objects.count()
    )
    return render(request, "pesquisa/index.html", {"total": total})


def formulario(request, perfil):
    forms_map = {
        "profissional": (RespostaProfissionalForm, "Profissional de TI", "💼"),
        "estudante": (RespostaEstudanteForm, "Estudante de TI / Área afim", "🎓"),
        "publico": (RespostaPublicoForm, "Público Geral", "🌐"),
    }
    if perfil not in forms_map:
        return redirect("index")

    FormClass, titulo, icone = forms_map[perfil]

    if request.method == "POST":
        form = FormClass(request.POST)
        if form.is_valid():
            form.save()
            return redirect("obrigado")
    else:
        form = FormClass()

    return render(request, "pesquisa/formulario.html", {
        "form": form,
        "titulo": titulo,
        "icone": icone,
        "perfil": perfil,
    })


def obrigado(request):
    return render(request, "pesquisa/obrigado.html")


@staff_member_required
def dashboard(request):
    prof = RespostaProfissional.objects.all()
    est  = RespostaEstudante.objects.all()
    pub  = RespostaPublico.objects.all()

    total = prof.count() + est.count() + pub.count()

    perfis = [
        {"perfil": "Profissional", "total": prof.count()},
        {"perfil": "Estudante",    "total": est.count()},
        {"perfil": "Público Geral","total": pub.count()},
    ]

    def dist(qs, field):
        return list(qs.values(field).annotate(total=Count(field)).order_by("-total"))

    def conta_comp(qs, campo):
        todas = []
        for r in qs.exclude(**{campo: ""}):
            todas.extend(getattr(r, campo).split(","))
        return [{"nome": k, "total": v} for k, v in Counter(todas).most_common(8)]

    ctx = {
        "total": total,
        "perfis": perfis,
        "areas": dist(prof, "area_atuacao"),
        "tempos": dist(prof, "tempo_atuacao"),
        "regimes": dist(prof, "regime_trabalho"),
        "comp_tec_prof": conta_comp(prof, "competencias_tecnicas"),
        "comp_comp_prof": conta_comp(prof, "competencias_comportamentais"),
        "semestres": dist(est, "semestre"),
        "motivos": dist(est, "motivo_escolha"),
        "comp_tec_est": conta_comp(est, "competencias_tecnicas"),
        "freq_uso": dist(pub, "frequencia_uso_tecnologia"),
        "confianca": dist(pub, "confianca_sistemas"),
        "associa": dist(pub, "associa_ti_a"),
        "mercado_prof": dist(prof, "percebe_mercado"),
        "mercado_est":  dist(est,  "percebe_mercado"),
        "mercado_pub":  dist(pub,  "percebe_mercado"),
        "prof_recentes": prof[:5],
        "est_recentes":  est[:5],
        "pub_recentes":  pub[:5],
    }
    return render(request, "pesquisa/dashboard.html", ctx)


@staff_member_required
def exportar(request):
    wb = exportar_excel_multi(
        RespostaProfissional.objects.all(),
        RespostaEstudante.objects.all(),
        RespostaPublico.objects.all(),
    )
    resp = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    resp["Content-Disposition"] = 'attachment; filename="pesquisa_computacao.xlsx"'
    wb.save(resp)
    return resp