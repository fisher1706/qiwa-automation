from pathlib import Path

import allure
import pytest

from data.delegation import general_data
from src.api.app import QiwaApi
from src.ui.qiwa import qiwa
from utils.helpers import save_pdf_file_from_response


def prepare_data_for_verify_delegation_letter(qiwa_api: QiwaApi, headers: dict):
    delegation_id = qiwa_api.delegation_api.create_delegation(
        headers,
        general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_NO_PARTNERS,
        general_data.TWELVE_MONTHS_DURATION,
    )["id"]
    response = qiwa_api.delegation_api.get_delegation_letter(headers, delegation_id, "en")
    file_path = save_pdf_file_from_response(response, f"Delegation_letter_{delegation_id}")
    delegation_details = qiwa_api.delegation_api.get_delegation_by_id(headers, delegation_id)
    prepared_data = {
        "delegation_status": delegation_details.delegation_status,
        "delegation_id": str(delegation_id),
        "delegate_name": delegation_details.delegate_name,
        "delegate_nid": delegation_details.delegate_nid,
        "expiry_date": delegation_details.expiry_date,
        "file_path": file_path,
    }
    return prepared_data


@allure.step
def open_verify_delegation_letter_page():
    qiwa.open_verify_delegation_letter_page()
    qiwa.delegation_localisation.select_english_localisation_for_public_pages()
    qiwa.delegation_letter_verify_page.should_verify_letter_page_be_displayed()


@pytest.fixture()
def remove_pdf_file():
    yield
    files_folder = Path(__file__).parent.parent.parent.parent.parent.joinpath("data/files")
    for file_path in files_folder.glob("Delegation_letter*.pdf"):
        if file_path.exists():
            file_path.unlink()
