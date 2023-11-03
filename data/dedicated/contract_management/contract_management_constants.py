from dataclasses import dataclass

from data.constants import Language

VERIFICATION_CODE = {Language.EN: "Verification Code", Language.AR: "رمز التحقق"}
MOBILE_VERIFICATION = {Language.EN: "Mobile verification", Language.AR: "رمز التحقق"}
TITLE = {Language.EN: "Contract Management", Language.AR: "إدارة العقود"}
DESCRIPTION = {
    Language.EN: "A service provided to establishments on Qiwa platform to create and authenticate employee "
    "contracts digitally. After the contract gets created and submitted, it will be sent to the "
    "employee’s account on Qiwa for approval or rejection.",
    Language.AR: "خدمة تتيح للمنشآت إنشاء وتوثيق وإنهاء عقود الموظفين إلكترونيًا، وبعد إنشاء العقد الوظيفي يمكن "
    "للموظف الموافقة على العقد أو رفضه أو طلب تعديله عبر حسابه في قوى أفراد. وفي حال موافقة الطرفين "
    "يعتبر العقد موثق من وزارة الموارد البشرية والتنمية الاجتماعية",
}
CONTRACT_AUTHENTICATION_SCORE_FOR_SAUDI_EMPLOYEES = {
    Language.EN: "Contract Authentication Score for Saudi Employees",
    Language.AR: "مؤشر توثيق العقود للموظفين السعوديين",
}
CONTRACT_AUTHENTICATION_SCORE_FOR_EXPATS_EMPLOYEES = {
    Language.EN: "Contract Authentication Score for Expats Employees",
    Language.AR: "مؤشر توثيق العقود للموظفين المقيمين",
}
TOTAL_CONTRACT_AUTHENTICATION = {
    Language.EN: "Total Contract Authentication",
    Language.AR: "مؤشر توثيق العقود لجميع الموظفين",
}
AUTHENTICATED_CONTRACTS = {Language.EN: "Authenticated Contracts", Language.AR: "عقود موثقة"}
UNAUTHENTICATED_CONTRACTS = {
    Language.EN: "Unauthenticated Contracts",
    Language.AR: "عقود غير موثقة",
}

CONTRACT_TYPE = {Language.EN: "Contract Type", Language.AR: "نوع العقد"}


@dataclass
class SuccessMessages:
    MSG_SUCCESS_CONTRACT_CREATION = {
        Language.EN: "The contract was created! ( please submit an employee transfer request to proceed )",
        Language.AR: "تم إنشاء العقد بنجاح! ( الرجاء اكمال إجراء النقل من خدمة نقل الخدمات )",
    }
    MSG_SUCCESS_CONTRACT_CREATION_SAUDI_NOT_IN_ESTABLISHMENT = {
        Language.EN: "The contract has been sent successfully! Please inform the employee to login to Qiwa platform and"
        " accept the contract.",
        Language.AR: "تم ارسال العقد بنجاح! الرجاء إبلاغ الموظف بالدخول على منصة قوى والموافقة على العقد.",
    }
    MSG_SUCCESS_TEMPLATE_CREATION = {
        Language.EN: "Template was created successfully!",
        Language.AR: "عقود غير موثقة",
    }
    MSG_SUCCESS_TEMPLATE_REMOVING = "The contract template has been deleted successfully"
