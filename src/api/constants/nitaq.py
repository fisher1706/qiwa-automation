from enum import Enum


class ColorID(Enum):
    RED = 100
    LOW_GREEN = 300
    GREEN = 310
    HIGH_GREEN = 320
    PLATINUM = 400


class ColorName(Enum):
    RED = "Red"
    LOW_GREEN = "Low Green"
    GREEN = "Medium Green"
    HIGH_GREEN = "High Green"
    PLATINUM = "Platinum"


class ColorCode(Enum):
    RED = "FF0000"
    LOW_GREEN = "CAD400"
    GREEN = "75B027"
    HIGH_GREEN = "2A8443"
    PLATINUM = "EFEFEF"
