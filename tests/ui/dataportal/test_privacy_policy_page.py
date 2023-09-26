import allure
import pytest

from data.data_portal.constants import TRANSLATION_XLSX, Localization, PrivacyPolicy
from data.data_portal.dataset import PrivacyPolicyData
from src.ui.dataportal import data_portal
from utils.allure import TestmoProject, project
from utils.xlsx_parser import get_value_from_xlsx_model

case_id = project(TestmoProject.LMI)


@allure.title('Check EN translation')
@case_id(5899)
@pytest.mark.parametrize('locator, row', PrivacyPolicyData.privacy_elements,
                         ids=PrivacyPolicyData.privacy_element_ids)
def test_en_translation_in_xlsx_model(locator, row):
    data_portal.open_privacy_policy()
    data_portal.privacy_policy\
        .check_translation_with_xlsx_model(locator, get_value_from_xlsx_model(TRANSLATION_XLSX,
                                                                              PrivacyPolicy.SHEET, row, column=2))


@allure.title('Check AR translation')
@case_id(5900)
@pytest.mark.parametrize('locator, row', PrivacyPolicyData.privacy_elements,
                         ids=PrivacyPolicyData.privacy_element_ids)
def test_ar_translation_in_xlsx_model(locator, row):
    data_portal.open_privacy_policy()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.privacy_policy\
        .check_translation_with_xlsx_model(locator, get_value_from_xlsx_model(TRANSLATION_XLSX,
                                                                              PrivacyPolicy.SHEET, row, column=3))
