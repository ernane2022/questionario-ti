from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("formulario/<str:perfil>/", views.formulario, name="formulario"),
    path("obrigado/", views.obrigado, name="obrigado"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("exportar/", views.exportar, name="exportar"),
]