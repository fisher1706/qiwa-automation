import dataclasses


@dataclasses.dataclass
class SubscriptionDefaultPrice:
    DEFAULT_PRICE_VAL_1100: float = 1100
    DEFAULT_PRICE_VAL_2300: float = 2300
    DEFAULT_PRICE_VAL_7000: float = 7000
    DEFAULT_PRICE_VAL_10000: float = 10000
    DEFAULT_PRICE_VAL_12000: float = 12000


@dataclasses.dataclass
class SubscriptionDiscount:
    DISCOUNT_VAL_100: float = 1.00
    DISCOUNT_VAL_25: float = 0.25
    DISCOUNT_VAL_10: float = 0.10
