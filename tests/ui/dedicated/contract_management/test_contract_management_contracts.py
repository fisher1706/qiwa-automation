import allure
import pytest

from data.constants import ContractManagement, Language, UserType
from data.dedicated.contract_management import (
    employer,
    laborer_expatriate,
    laborer_expatriate_not_in_the_establishment,
    laborer_saudi,
    laborer_saudi_not_in_the_establishment,
)
from src.ui.actions.contract_management import ContractManagementActions
from src.ui.components.footer import Footer


@allure.feature('Contract Management Contract Creation')
@pytest.mark.usefixtures("go_to_auth_page")
class TestContractManagementContractCreation:  # pylint: disable=unused-argument

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.contract_management_actions = ContractManagementActions()
        self.footer = Footer()

    @allure.title('Create a new contract for Saudi Laborer in the Establishment')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1218', '9319,9276')
    def test_create_a_new_contract_for_saudi_laborer_in_the_establishment(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_create_contract()
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.find_employee(laborer_saudi)
        self.contract_management_actions.fill_contract_info()
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.click_agree_checkbox()
        self.contract_management_actions.click_btn_submit()
        self.contract_management_actions.verify_success_contract_creation(
            ContractManagement.MSG_SUCCESS_CONTRACT_CREATION,
            Language.EN
        )
        self.footer.click_on_lang_button(Language.AR)
        self.contract_management_actions.verify_success_contract_creation(
            ContractManagement.MSG_SUCCESS_CONTRACT_CREATION,
            Language.AR
        )

    @allure.title('Create a new contract for Expatriate laborer in the establishment')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1218&case_id=9275')
    def test_create_a_new_contract_for_expatriate_laborer_in_the_establishment(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_create_contract()
        self.contract_management_actions.select_outside_saudi_arabia()
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.fill_contract_info(laborer=laborer_expatriate, user_type=UserType.EXPAT)
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.click_agree_checkbox()
        self.contract_management_actions.click_btn_submit()
        self.contract_management_actions.verify_success_contract_creation(
            ContractManagement.MSG_SUCCESS_CONTRACT_CREATION_SAUDI_NOT_IN_ESTABLISHMENT,
            Language.EN)

    @allure.title('Create a new contract for an Expatriate Laborer not in the establishment')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1218&case_id=9278')
    def test_create_a_new_contract_for_an_expatriate_laborer_not_in_the_establishment(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_create_contract()
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.fill_contract_info(laborer=laborer_expatriate_not_in_the_establishment,
                                                            user_type=UserType.EXPAT)
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.click_agree_checkbox()
        self.contract_management_actions.click_btn_submit()
        self.contract_management_actions.verify_success_contract_creation(
            ContractManagement.MSG_SUCCESS_CONTRACT_CREATION_SAUDI_NOT_IN_ESTABLISHMENT,
            Language.EN)

    @allure.title('Create a new contract for a Saudi Laborer not in the establishment')
    @allure.testcase('https://qiwa.testmo.net/repositories/4?group_id=1218&case_id=9279')
    def test_create_a_new_contract_for_a_saudi_laborer_not_in_the_establishment(self):
        self.contract_management_actions.navigate_to_cm_service(employer)
        self.contract_management_actions.click_btn_create_contract()
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.find_employee(laborer_saudi_not_in_the_establishment)
        self.contract_management_actions.fill_contract_info(user_type=UserType.USER)
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.click_agree_checkbox()
        self.contract_management_actions.click_btn_submit()
        self.contract_management_actions.verify_success_contract_creation(
            ContractManagement.MSG_SUCCESS_CONTRACT_CREATION_SAUDI_NOT_IN_ESTABLISHMENT,
            Language.EN
        )
        self.footer.click_on_lang_button(Language.AR)
        self.contract_management_actions.verify_success_contract_creation(
            ContractManagement.MSG_SUCCESS_CONTRACT_CREATION_SAUDI_NOT_IN_ESTABLISHMENT,
            Language.AR
        )
