import random


def get_months_list(max_months: int) -> list:
    return [f"{i} month" if i == 1 else f"{i} months" for i in range(1, max_months + 1)]


def get_random_employee(employee_list) -> dict:
    random_index = random.randrange(employee_list["totalElements"])
    return employee_list["content"][random_index]


def formatted_phone_number(phone_number: str) -> str:
    return f"{phone_number[:4]} {phone_number[4:6]} {phone_number[6:9]} {phone_number[9:]}"


def get_partners_data_for_add_delegation(partners: list) -> list:
    partner_data = []
    for partner in partners:
        partner_name = partner["partyName"]
        partner_mobile = partner["partyMobile"]
        formatted_partner_phone = formatted_phone_number(partner_mobile)
        partner_phone_valid = partner["validPhoneNumber"]

        if partner_phone_valid is True:
            partner_phone_valid = "Verified"
        else:
            partner_phone_valid = "All partners must have a verified phone number"

        data = [partner_name, formatted_partner_phone, partner_phone_valid]
        partner_data.append(data)
    return partner_data
