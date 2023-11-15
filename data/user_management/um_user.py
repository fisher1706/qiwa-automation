from data.dedicated.models.user import User


class UmUser(User):
    default_price: float
    default_discount: float
