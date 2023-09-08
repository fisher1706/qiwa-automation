import allure

from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@allure.title("Appointments: Book with visit type Establishment")
@case_id(22132)
def test_book_establishment_appointment():
    qiwa.login_as_user(login="1006586984")

