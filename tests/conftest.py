import pytest

from src.api.app import QiwaApi
from src.api.http_client import HTTPClient


@pytest.fixture(autouse=True)
def api():
    return HTTPClient()


@pytest.fixture(scope="class")
def delete_service_categories():
    yield
    api = QiwaApi.login_as_admin()
    response = api.e_service.api.get_admin_tags()
    tags = response.json()["data"]
    for tag in tags:
        if tag["attributes"]["code"] not in ("businesses", "employees", "visas"):
            api.e_service.api.delete_tag(tag["id"])
    api.e_service.api.get_admin_tags()
