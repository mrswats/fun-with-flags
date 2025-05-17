import json
from http import HTTPStatus

import pytest


@pytest.fixture
def healthcheck_url(url):
    return url("healthcheck")


@pytest.fixture
def get_healthcheck(client, healthcheck_url):
    def _():
        return client.get(healthcheck_url)

    return _


def test_healthcheck_url(healthcheck_url):
    assert healthcheck_url == "/healthcheck/"


def test_healthcheck_response_status_code(get_healthcheck):
    assert get_healthcheck().status_code == HTTPStatus.OK


def test_healthcheck_response_data(get_healthcheck):
    response = get_healthcheck()
    assert json.loads(response.content.decode()) == {"status": "ok"}
