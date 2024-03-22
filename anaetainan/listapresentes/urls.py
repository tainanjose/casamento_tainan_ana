from django.urls import path

from . import views


urlpatterns = [
    path("", views.PaginaPrincipalListView.as_view(), name="listapresentes.home"),
    path(
        "comprar-presente/<int:pk>/",
        views.IntencaoDePresenteCreateView.as_view(),
        name="listapresentes.intencao.create",
    ),
    path(
        "comprar-presente/confirmacao/<int:pk>/",
        views.IntencaoDePresenteConfirmacaoView.as_view(),
        name="listapresentes.intencao.confirmacao",
    ),
]
