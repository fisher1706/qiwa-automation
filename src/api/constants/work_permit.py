from enum import Enum


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
    PAID = "مدفوع"
    PENDING_PAYMENT = "قيد السداد"
    REJECTED = "مرفوض"
    CANCELED = "ملغى"
    CANCELING_PROCESS = "في مرحلة الالغاء"
