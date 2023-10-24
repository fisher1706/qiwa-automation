from typing import Type

from src.api.models.qiwa.data_attr.saudization_certificate import (
    encrypted_saudization_certificate,
    error,
    not_found,
    saudization_certificate,
)
from src.api.models.qiwa.raw.root import Root

certificate = Root[saudization_certificate, Type[None], Type[None]]
encrypted_certificate = Root[encrypted_saudization_certificate, Type[None], Type[None]]
certificate_not_found = Root[not_found, Type[None], Type[None]]
certificate_error = Root[error, Type[None], Type[None]]
