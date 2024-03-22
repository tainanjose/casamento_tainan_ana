import pytest


@pytest.mark.django_db
def test_deve_retornar_home(client):
    # Quando tentamos adicionar um item
    resp = client.get("/")

    # Entao recebemos um sem autorizacao
    assert resp.status_code == 200
