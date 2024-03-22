import pytest
from http import HTTPStatus


@pytest.mark.django_db
def test_deve_retornar_404_not_found_para_url_invalida(client, logged_jon):
    # Dado uma URL invalida
    payload = {"qualque": "coisa"}

    # Quando tentamos acessar
    resp = client.post(
        "/api/core/tasks/invalid", payload, content_type="application/json"
    )

    # Entao 404
    assert resp.status_code == HTTPStatus.NOT_FOUND
