from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "confirmacao/", views.ConfirmacaoRedirectView.as_view(), name="core.confirmacao"
    ),
    path("confirmacao", views.ConfirmacaoRedirectView.as_view()),
    path("save-the-date/", views.SaveTheDateView.as_view(), name="core.savethedate"),
    path(
        "dicasdehoteis/",
        TemplateView.as_view(template_name="core/dicasdehoteis.html"),
        name="core.dicasdehoteis",
    ),
    path(
        "apps/", TemplateView.as_view(template_name="core/apps.html"), name="core.apps"
    ),
    path(
        "agradecimentopresente/",
        TemplateView.as_view(template_name="core/agradecimento_presente.html"),
        name="core.agradecimentopresente",
    ),
    path(
        "cerimoniareligiosa/",
        TemplateView.as_view(template_name="core/cerimoniareligiosa.html"),
        name="core.cerimoniareligiosa",
    ),
    path(
        "salaodebeleza/",
        TemplateView.as_view(template_name="core/salaodebeleza.html"),
        name="core.salaodebeleza",
    ),
    path(
        "restaurante/",
        TemplateView.as_view(template_name="core/restaurante.html"),
        name="core.restaurante",
    ),
    path(
        "avisoconfirmacao/",
        TemplateView.as_view(template_name="core/avisoconfirmacao.html"),
        name="core.avisoconfirmacao",
    ),
    path("", views.ShowHomeView.as_view(), name="core.showhome"),
    path("quiz/", views.QuizView.as_view(), name="quiz"),  # Nova URL para o quiz
]
