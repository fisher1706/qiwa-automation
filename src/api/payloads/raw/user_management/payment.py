from src.api.models.qiwa.base import QiwaBaseModel


class CardDetails(QiwaBaseModel):
    Holder: str = "Jane Jones"
    Number: str = "4111111111111111"
    ExpiryMonth: str = "05"
    ExpiryYear: str = "34"
    CVV: str = "123"


class PaymentRequest(QiwaBaseModel):
    paymentBrand: str = "VISA"
    card: CardDetails = CardDetails()


class BrowserInfo(QiwaBaseModel):
    AcceptHeader: str = "text / html"
    ScreenColorDepth: str = "24"
    JavaEnabled: str = "false"
    Language: str = "en-US"
    ScreenHeight: str = "1080"
    ScreenWidth: str = "1920"
    Timezone: str = "-180"
    ChallengeWindow: str = "4"
    UserAgent: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/114.0.0.0 Safari/537.36"
    )


class Payment(QiwaBaseModel):
    transactionId: int
    type: str = "CARD"
    paymentRequest: PaymentRequest = PaymentRequest()
    browser: BrowserInfo = BrowserInfo()
