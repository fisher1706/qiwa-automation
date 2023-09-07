import allure
import pytest

from data.dataportal.constants import TRANSLATION_XLSX, Localization, PrivacyPolicy
from data.dataportal.dataset import PrivacyPolicyData
from src.ui.qiwa import data_portal
from utils.xlsx_parser import get_value_from_xlsx_model


@allure.title('Check EN translation')
@pytest.mark.parametrize('locator, row', PrivacyPolicyData.privacy_elements,
                         ids=PrivacyPolicyData.privacy_element_ids)
def test_en_translation_in_xlsx_model(locator, row):
    data_portal.open_privacy_policy()
    data_portal.privacy_policy\
        .check_translation_with_xlsx_model(locator, get_value_from_xlsx_model(TRANSLATION_XLSX,
                                                                              PrivacyPolicy.SHEET, row, column=2))


@allure.title('Check AR translation')
@pytest.mark.parametrize('locator, row', PrivacyPolicyData.privacy_elements,
                         ids=PrivacyPolicyData.privacy_element_ids)
def test_ar_translation_in_xlsx_model(locator, row):
    data_portal.open_privacy_policy()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.privacy_policy\
        .check_translation_with_xlsx_model(locator, get_value_from_xlsx_model(TRANSLATION_XLSX,
                                                                              PrivacyPolicy.SHEET, row, column=3))
