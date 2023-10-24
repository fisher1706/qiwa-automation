from typing import Any, Literal, Type

from src.api.models.qiwa.raw.data import Data
from src.api.models.qiwa.raw.saudi_certificate import (
    EncryptedSaudizationCertificate,
    Error,
    SaudizationCertificate,
)

saudization_certificate = Data[
    str,
    Literal["saudization-certificate"],
    SaudizationCertificate,
    Type[None],
]
encrypted_saudization_certificate = Data[
    str,
    Literal["encrypted-saudization-certificate"],
    EncryptedSaudizationCertificate,
    Type[None],
]
error = Data[str, Literal["error"], Error, Type[None]]
not_found = Data[Literal["-1"], Literal["not_found"], list[Any], Type[None]]
