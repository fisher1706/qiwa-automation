from enum import Enum
from typing import Literal


class WorkPermitStatus(str, Enum):
    PRINTED = "1"
    EXPIRED = "2"
    PAID = "3"
    PENDING_PAYMENT = "4"
    REJECTED = "5"
    CANCELED = "6"
    CANCELING_PROCESS = "7"


class WorkPermitStatusArabic(str, Enum):
    PRINTED = "تمت الطباعة"
    EXPIRED = "منتهي الصلاحية"
    PAID = "تم السداد"
    PENDING_PAYMENT = "قيد السداد"
    REJECTED = "مرفوض"
    CANCELED = "ملغى"
    CANCELING_PROCESS = "في مرحلة الالغاء"


class WorkPermitStatusLiterals(Enum):
    PRINTED = Literal["تمت الطباعة"], Literal["1"]
    EXPIRED = Literal["منتهي الصلاحية"], Literal["2"]
    PAID = Literal["تم السداد"], Literal["3"]
    PENDING_PAYMENT = Literal["قيد السداد"], Literal["4"]
    REJECTED = Literal["مرفوض"], Literal["5"]
    CANCELED = Literal["ملغى"], Literal["6"]
    CANCELING_PROCESS = Literal["في مرحلة الالغاء"], Literal["7"]
