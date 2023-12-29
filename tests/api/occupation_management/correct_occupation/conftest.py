import random

import pytest

from src.api.models.qiwa.raw.correct_occupation.laborers import LaborerAttributes


@pytest.fixture
def laborer(correct_occupation, change_occupation) -> LaborerAttributes:
    laborers = correct_occupation.get_laborers(per=20)
    cor_requests = correct_occupation.get_requests(per=100)
    cho_users = change_occupation.get_users(per=100)

    cho_eligible_users = [
        user.attributes.personal_number
        for user in list(filter(lambda u: u.attributes.eligibility == "1", cho_users.data))
    ]
    cor_requests_laborers = [laborer.attributes.laborer_id for laborer in cor_requests.data]
    laborers_without_requests = list(
        filter(
            lambda l: l.attributes.laborer_id not in cor_requests_laborers
            and l.attributes.laborer_id in cho_eligible_users,
            laborers.data,
        )
    )
    laborer = random.choice(laborers_without_requests).attributes

    yield laborer

    correct_occupation.delete_request_in_ibm(laborer.laborer_id)
