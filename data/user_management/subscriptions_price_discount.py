import dataclasses


@dataclasses.dataclass
class SubscriptionDefaultPrice:
    default_price_val_1100: float = 1100
    default_price_val_2300: float = 2300
    default_price_val_7000: float = 7000
    default_price_val_10000: float = 10000
    default_price_val_12000: float = 12000


@dataclasses.dataclass
class SubscriptionDiscount:
    discount_val_100: float = 1.00
    discount_val_25: float = 0.25
    discount_val_10: float = 0.10
