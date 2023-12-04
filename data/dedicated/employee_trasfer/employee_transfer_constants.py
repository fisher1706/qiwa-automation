from data.constants import Language
from data.dedicated.enums import ServicesAndTools
from data.dedicated.models.transfer_type import TransferType

type_4 = TransferType(
    code="4",
    name_ar=ServicesAndTools.TRANSFER_LABORER_FROM_ANOTHER_ESTABLISHMENT.value[Language.AR],
    name_en=ServicesAndTools.TRANSFER_LABORER_FROM_ANOTHER_ESTABLISHMENT.value[Language.EN],
)
type_9 = TransferType(
    code="9",
    name_ar=ServicesAndTools.DEPENDENT_TRANSFER.value[Language.AR],
    name_en=ServicesAndTools.DEPENDENT_TRANSFER.value[Language.EN],
)
type_12 = TransferType(
    code="12",
    name_ar=ServicesAndTools.HOME_WORKERS_TRANSFER.value[Language.AR],
    name_en=ServicesAndTools.HOME_WORKERS_TRANSFER.value[Language.EN],
)

REJECT_REASON = "I don’t want to be transferred"
