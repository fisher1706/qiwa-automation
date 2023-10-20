import pytest

from src.api.app import QiwaApi


@pytest.fixture(scope="module")
def api() -> QiwaApi:
    qiwa = QiwaApi.login_as_user("1048285405").select_company(sequence_number=136401)
    qiwa.change_occupation.pass_ott_authorization()
    return qiwa
