import allure
import pytest

from data.constants import Language
from data.dedicated.contract_management.contract_management_constants import (
    CONTRACT_AUTHENTICATION_SCORE_FOR_EXPATS_EMPLOYEES,
    CONTRACT_AUTHENTICATION_SCORE_FOR_SAUDI_EMPLOYEES,
    DESCRIPTION,
    TITLE,
    TOTAL_CONTRACT_AUTHENTICATION,
)
from data.dedicated.contract_management.contract_management_users import employer
from src.ui.actions.old_contract_management import OldContractManagementActions
from src.ui.components.footer import Footer


@allure.feature('Contract Management Dashboard')
@pytest.mark.skip("Deprecated")
class TestContractManagement:  # pylint: disable=unused-argument

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.contract_management_actions = OldContractManagementActions()
        self.footer = Footer()

    @allure.title('Verify the contract authentication score and buttons in the Contract Management page')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1217', '9273,9274,9289')
    def test_user_can_see_the_contract_authentication_score(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.verify_description(DESCRIPTION, Language.EN)
        self.contract_management_actions.verify_score(
            CONTRACT_AUTHENTICATION_SCORE_FOR_SAUDI_EMPLOYEES, Language.EN)
        self.contract_management_actions.verify_score(
            CONTRACT_AUTHENTICATION_SCORE_FOR_EXPATS_EMPLOYEES, Language.EN)
        self.contract_management_actions.verify_score(
            TOTAL_CONTRACT_AUTHENTICATION, Language.EN)
        self.footer.click_on_lang_button(Language.AR)

        self.contract_management_actions.verify_title(TITLE, Language.AR)
        self.contract_management_actions.verify_description(DESCRIPTION, Language.AR)
        self.contract_management_actions.verify_score(
            CONTRACT_AUTHENTICATION_SCORE_FOR_SAUDI_EMPLOYEES, Language.AR)
        self.contract_management_actions.verify_score(
            CONTRACT_AUTHENTICATION_SCORE_FOR_EXPATS_EMPLOYEES, Language.AR)
        self.contract_management_actions.verify_score(
            TOTAL_CONTRACT_AUTHENTICATION, Language.AR)
        self.contract_management_actions.verify_btn_contract_templates_is_clickable()
        self.contract_management_actions.verify_btn_create_bulk_contracts_is_clickable()
        self.contract_management_actions.verify_btn_create_contract_is_clickable()
