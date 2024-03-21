import pytest

from anaetainan.core.models import Task
from anaetainan.core.service import tasks_svc
from anaetainan.base.exceptions import BusinessError


@pytest.mark.django_db
def test_deve_inserir_uma_nova_tarefa():
    new_item = tasks_svc.add_task("ABC")

    item = Task.objects.all().first()

    assert item.id == new_item.get("id")
    assert item.description == new_item.get("description")


@pytest.mark.django_db
def test_deve_retornar_um_erro_ao_cadastrar_item_sem_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        new_item = tasks_svc.add_task(None)

    # Então
    assert str(error.value) == "Invalid description"


@pytest.mark.django_db
def test_deve_retornar_um_erro_ao_cadastrar_item_com_espacos_na_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        new_item = tasks_svc.add_task("    ")

    # Então
    assert str(error.value) == "Invalid description"


@pytest.mark.django_db
def test_deve_aceitar_apenas_tipo_string_na_descricao():
    # Quando tentamos adicionar item sem valor
    with pytest.raises(BusinessError) as error:
        new_item = tasks_svc.add_task(1000)

    # Então
    assert str(error.value) == "Invalid description"
