from django.urls import reverse
import pytest


@pytest.fixture
def healthcheck_url():
    return reverse("healthcheck")


def test_healthcheck_url(healthcheck_url):
    assert healthcheck_url == "/healthcheck/"
