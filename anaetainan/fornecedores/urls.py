from django.urls import path

from . import views


urlpatterns = [
    path("", views.FornecedoresListView.as_view(), name="fornecedores.lista"),
]
