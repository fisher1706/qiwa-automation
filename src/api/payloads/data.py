from src.api.payloads.raw.data import Data
from src.api.payloads.raw.root import Root


def change_occupation(attributes):
    return Root(data=Data(type="change-occupation", attributes=attributes))


def group(attributes):
    return Root(data=Data(type="group", attributes=attributes))
