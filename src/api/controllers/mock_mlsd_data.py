import allure

import config
from data.account import Account
from data.constants import UserInfo
from data.mock_mlsd.establishment import Establishment
from src.api.assertions.response_validator import ResponseValidator
from src.api.constants import nitaq
from src.api.constants.subscription import Subscription
from src.api.http_client import HTTPClient
from utils.logger import yaml_logger

logger = yaml_logger.setup_logging(__name__)


class MockMlsdDataController:
    url = config.settings.mock_mlsd_url

    def __init__(self):
        self.api = HTTPClient()
        self.account = None
        self.unified_number_id = None
        self.sequence_number = None
        self.labor_office_id = None

    @allure.step("Prepare new Owner account")
    def prepare_owner_account(
        self,
        user_type=None,
        role="Owner",
        personal_number=None,
        email=None,
        password=None,
        phone_number=None,
        wp_type="valid",
        saudi_count=3,
        expat_count=3,
        branches=None,
        subscription="have-subscription",
    ):
        user_type = user_type if user_type else "saudi"
        if user_type in {"saudi", "expat", "border"} and not personal_number:
            personal_number = self.get_laborers_new(
                user_type=user_type,
                wp_type=wp_type,
                role=role,
                saudi_count=saudi_count,
                expat_count=expat_count,
                branches=branches,
                subscription=subscription,
            )

        password = password if password else UserInfo.PASSWORD
        self.account = Account(
            personal_number=personal_number,
            email=email,
            phone_number=phone_number,
            password=password,
        )

    @allure.step("Prepare establishment")
    def prepare_establishment(
        self,
        red_nitaq=False,
        with_subscription=True,
        cr_number=None,
        branches=None,
        with_laborers=False,
    ):
        """
        Owner account available within a single tests created with specified parameters:
        :param params: red nitaq, green nitaq, no subscription, subscription
        @param with_laborers: if set True
        @param with_subscription: create owner with subscription or without
        @param red_nitaq: when False - nitaq is set to green
        @param cr_number:
        @param branches:
        """
        users = []
        payload = {}
        est_data = {}

        if red_nitaq:
            est_data["nitaq_color_id"] = nitaq.ColorID.RED
            est_data["nitaq_color_name"] = nitaq.ColorName.RED
            est_data["nitaq_color_code"] = nitaq.ColorCode.RED
        if not with_subscription:
            est_data["have_subscription"] = Subscription.SHOULD_ADD
        if cr_number:
            est_data["cr_number"] = cr_number
        if branches:
            est_data["branches"] = branches

        establishment = Establishment.parse_obj(est_data)

        establishment_data = self.post_establishments_new(establishment)
        self.unified_number_id = establishment_data["unified_number_id"]
        self.sequence_number = establishment_data["sequence_number"]
        self.labor_office_id = establishment_data["labor_office_id"]

        if with_laborers:
            response = self.get_establishment_laborers(self.sequence_number)
            for item in response:
                if item["role"] == "Owner":
                    payload["owner"] = item["laborer_id_no"]
                elif item["role"] == "EstablishmentManager":
                    payload["manager"] = item["laborer_id_no"]
                elif item["role"] == "Employee" and str(item["laborer_id_no"]).startswith("2"):
                    payload["employee"] = item["laborer_id_no"]
            users.append(payload)
            account = users[0]["owner"]
        else:
            account = establishment_data["owner_number"]

        self.account = Account(account, UserInfo.DEFAULT_PASSWORD)
        logger.info(
            f"Unified Number ID: {self.unified_number_id}, Sequence Number: {self.sequence_number}, "
            f"Labor Office ID: {self.labor_office_id}"
        )

    def get_laborers_new(
        self,
        user_type,
        role="Owner",
        branches=3,
        wp_type="valid",
        saudi_count=3,
        expat_count=3,
        subscription="have-subscription",
    ):
        """
        :param expat_count: quantity of expats available in new company
        :param saudi_count: quantity of saudis available in new company
        :param branches: branches count for the user
        :param wp_type: valid, invalid, expired
        :param user_type: saudi, expat, border
        :param role: Owner, EstablishmentUser, EstablishmentManager, Employee
        :param subscription: have-subscription, self-pending, invite-pending
        :return: account 'laborer_id' that can be registered to Qiwa
        """
        params = (
            f"?e-count=1"
            f"&wp={wp_type}"
            f"&mobile-auth=true"
            f"&saudi-count={saudi_count}"
            f"&expat-count={expat_count}"
            f"&nitaq-color=any"
            f"&branches={branches}"
            f"&subscription={subscription}"
        )

        response = self.api.get(self.url, endpoint=f"/laborers/new/{user_type}/{role}{params}")
        ResponseValidator(response).check_status_code(name="Get mock Laborer ID", expect_code=200)
        laborer_id_no = response.json()["laborer_id_no"]
        return laborer_id_no

    def post_establishments_new(self, est: Establishment = Establishment()):
        payload = est.dict(exclude_none=True, by_alias=True)
        response = self.api.post(self.url, endpoint="/establishments/new", json=payload)
        ResponseValidator(response).check_status_code(name="Create establishment", expect_code=200)
        json = response.json()
        return json

    def get_establishment_laborers(self, sequence_number, expect_code=200):
        response = self.api.get(self.url, endpoint=f"/establishments/laborers/{sequence_number}")
        ResponseValidator(response).check_status_code(
            name=f"GET /establishments/laborers/{sequence_number}", expect_code=expect_code
        )
        return response.json()
