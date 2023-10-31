from datetime import datetime, timedelta

from pydantic import BaseModel
from typing_extensions import Optional

from data.dedicated.models.user import User


class SaudiEstValidation(BaseModel):
    cr_number: Optional[str]
    unified_number_id: Optional[str]


class AppointmentStatus(BaseModel):
    Status: str
    Code: str
    ArabicMsg: str
    EnglishMsg: str


not_in_nitaqat_appointment_rs = AppointmentStatus(Status="ERROR",
                                                  Code="E0000949",
                                                  ArabicMsg="عفوًا، لايمكن حجز موعد لهذه الخدمة لإن المنشأة غير "
                                                            "مدرجة في نطاقات",
                                                  EnglishMsg="Sorry , you can not be able to book appointment "
                                                             "because the establishment does not exists in NITAQAT")

red_nitaqat_appointment_rs = AppointmentStatus(Status="ERROR",
                                               Code="ODM00102",
                                               ArabicMsg="عفواً، نطاق كيان المنشأة يجب أن يكون في الأخضر المنخفض أو "
                                                         "أعلى الرجاء رفع نسبة التوطين في الكيان للاستفادة من الخدمات",
                                               EnglishMsg="Sorry, Nitaqat color of the establishment entity must be "
                                                          "in low green or above , please raise the nationalization "
                                                          "percentage in the entity to benefit from the services.")

lo_sc_user = User(
    personal_number="1045997168",
    labor_office_id="10",
    sequence_number="1383725",
    name="ماجد التميمي",
    office_id="3186"
)

lo_sc_agent = User(
    personal_number="1063277899",
    labor_office_id="",
    sequence_number="",
    name="مجتبى السلمان"
)

lo_sc_nitaqat_not_included = User(
    personal_number="1023411612",
    labor_office_id="1",
    sequence_number="99679",
    office_id="3186",
    name="عبدالعزيز المقيرن"
)


lo_sc_red_nitaqat = User(
    personal_number="1024408138",
    labor_office_id="1",
    sequence_number="63293",
    office_id="3186",
    name="صالح النويصر"
)

lo_sc_low_green_nitaqat = User(
    personal_number="1000683555",
    labor_office_id="1",
    sequence_number="115892",
    office_id="3186",
    name=""
)

lo_sc_med_green_nitaqat = User(
    personal_number="1031203266",
    labor_office_id="1",
    sequence_number="165550",
    office_id="3186",
    name=""
)

lo_sc_high_green_nitaqat = User(
    personal_number="1017221100",
    labor_office_id="1",
    sequence_number="17724",
    office_id="3186",
    name=""
)

lo_sc_platinum_nitaqat = User(
    personal_number="1001622867",
    labor_office_id="1",
    sequence_number="1704257",
    office_id="3186",
    name=""
)

successful_issuing_message = ("Saudization Certificate issued successfully - "
                              "below are the details of the Saudization Certificate.")

today_date = datetime.today().strftime("%d/%m/%Y")
date_after_90_days = (datetime.today() + timedelta(days=90)).strftime("%d/%m/%Y")
