import allure
import pytest

from data.user_management.user_management_datasets import (
    PaymentHeaders,
    SelfSubscriptionType,
)
from data.user_management.user_management_users import owner_account
from src.api.app import QiwaApi
from src.api.models.qiwa.raw.user_management_models import SelfPriceCookie
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.feature("Self subscription flows API")
@pytest.mark.usefixtures("clean_up_session")
class TestSelfSubscriptionAPI:  # pylint: disable=duplicate-code
    @allure.title("E2e self subscription flows")
    @case_id(47003, 46665, 47002, 46667)
    @pytest.mark.parametrize("subscr_type", SelfSubscriptionType.subscription_type)
    def test_self_extend_subscription_flow(self, subscr_type):
        user = owner_account
        qiwa = QiwaApi.login_as_user(user.personal_number)
        self_subsc_cookie = SelfPriceCookie(
            user_id=user.user_id,
            company_sequence_number=user.sequence_number,
            company_labor_office_id=user.labor_office_id,
            user_personal_number=user.personal_number,
        ).dict(by_alias=True)
        self_price = float(
            qiwa.user_management_api.get_self_subscription_price(
                cookie=self_subsc_cookie,
                labor_office_id=user.labor_office_id,
                sequence_number=user.sequence_number,
            )
        )
        transaction_id = int(
            qiwa.user_management_api.post_self_flow(
                cookie=self_subsc_cookie,
                labor_office_id=user.labor_office_id,
                sequence_number=user.sequence_number,
                subscription_price=self_price,
                subscr_type=subscr_type,
            )
        )
        qiwa.payment.post_create_payment(transaction_id=transaction_id)
        qiwa.payment.post_confirm_payment(
            token=PaymentHeaders.authorization, transaction_id=transaction_id
        )
        qiwa.user_management_api.get_thank_you_page(self_subsc_cookie, transaction_id)
