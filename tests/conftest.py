import pytest

from django.urls import reverse


@pytest.fixture
def url():
    def _(url_name: str) -> str:
        return reverse(url_name)
