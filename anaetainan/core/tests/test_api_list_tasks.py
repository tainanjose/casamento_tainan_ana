import pytest
from unittest.mock import ANY

from anaetainan.core.models import Task


def test_nao_deve_permitir_listar_task_sem_login(client):
    # Dado um usuário anônimo

    # Quando tentamos listar itens
    resp = client.get("/api/core/tasks/list")

    # Entao recebemos um sem autorizacao
    assert resp.status_code == 401


@pytest.mark.django_db
def test_deve_retornar_lista_vazia(client, logged_jon):
    # Quando tentamos listar itens
    resp = client.get("/api/core/tasks/list")
    data = resp.json()

    # Entao recebemos um sem autorizacao
    assert resp.status_code == 200
    assert data.get("tasks") == []


@pytest.mark.django_db
def test_deve_listar_task_com_login(client, logged_jon):
    # Dado um item criado
    Task.objects.create(description="walk the dog")

    # Quando listamos
    resp = client.get("/api/core/tasks/list")
    data = resp.json()

    # Entao
    assert resp.status_code == 200
    assert data == {
        "tasks": [{"description": "walk the dog", "done": False, "id": ANY}]
    }
