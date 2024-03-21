import pytest

from anaetainan.core.models import Task
from anaetainan.core.service import tasks_svc


@pytest.mark.django_db
def test_deve_retornar_lista_vazia():
    itens_list = tasks_svc.list_tasks()
    assert itens_list == []


@pytest.mark.django_db
def test_deve_listar_com_10_iten():
    # Dado 10 itens criados
    itens = [Task(description=f"Tasks nro ${number}") for number in range(1, 11)]
    Task.objects.bulk_create(itens)

    itens_list = tasks_svc.list_tasks()

    assert len(itens_list) == 10
