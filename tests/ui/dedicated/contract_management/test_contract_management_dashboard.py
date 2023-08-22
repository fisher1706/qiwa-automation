import allure
import pytest

from data.constants import ContractManagement, Language
from data.dedicated.contract_management import employer
from src.ui.actions.contract_management import ContractManagementActions
from src.ui.pages.languages_page import Languages


@allure.feature('Contract Management Dashboard')
@pytest.mark.daily
@pytest.mark.ui
@pytest.mark.cm
@pytest.mark.stage
@pytest.mark.usefixtures("go_to_auth_page")
class TestContractManagement:  # pylint: disable=unused-argument

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.contract_management_actions = ContractManagementActions()
        self.language = Languages()

    @allure.title('Verify the contract authentication score and buttons in the Contract Management page')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1217', '9273,9274,9289')
    def test_user_can_see_the_contract_authentication_score(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.verify_description(ContractManagement.DESCRIPTION, Language.EN)
        self.contract_management_actions.verify_score(
            ContractManagement.CONTRACT_AUTHENTICATION_SCORE_FOR_SAUDI_EMPLOYEES, Language.EN)
        self.contract_management_actions.verify_score(
            ContractManagement.CONTRACT_AUTHENTICATION_SCORE_FOR_EXPATS_EMPLOYEES, Language.EN)
        self.contract_management_actions.verify_score(
            ContractManagement.TOTAL_CONTRACT_AUTHENTICATION, Language.EN)
        self.language.click_on_lang_button(Language.AR)

        self.contract_management_actions.verify_title(ContractManagement.TITLE, Language.AR)
        self.contract_management_actions.verify_description(ContractManagement.DESCRIPTION, Language.AR)
        self.contract_management_actions.verify_score(
            ContractManagement.CONTRACT_AUTHENTICATION_SCORE_FOR_SAUDI_EMPLOYEES, Language.AR)
        self.contract_management_actions.verify_score(
            ContractManagement.CONTRACT_AUTHENTICATION_SCORE_FOR_EXPATS_EMPLOYEES, Language.AR)
        self.contract_management_actions.verify_score(
            ContractManagement.TOTAL_CONTRACT_AUTHENTICATION, Language.AR)
        self.contract_management_actions.verify_btn_contract_templates_is_clickable()
        self.contract_management_actions.verify_btn_create_bulk_contracts_is_clickable()
        self.contract_management_actions.verify_btn_create_contract_is_clickable()
