import base64
import json
from base64 import b64encode

import allure
import jwt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


class CryptoManager:
    def __init__(self):
        self.encoding_key = "h3t+67wkJLbuEq8IWOkTStHx0CShkvWQ"
        self.constant_iv = "0000000000000000"

    def encrypt(self, password):
        bytes_password = password.encode(encoding="UTF-8")
        encoding_key = self.encoding_key.encode(encoding="UTF-8")
        constant_iv = self.constant_iv.encode(encoding="UTF-8")
        cipher_code = AES.new(encoding_key, AES.MODE_CBC, constant_iv)
        password_cipher = cipher_code.encrypt(pad(bytes_password, AES.block_size))
        return str(b64encode(password_cipher).decode("utf-8")).strip("b'")


@allure.step
def decrypt_saudization_certificate(encrypted_certificate: str) -> dict:
    cipher_key = b"21396810880121396810880121396810"
    cipher_iv = b"PGKEYENCDECIVSPC"
    cipher = AES.new(key=cipher_key, iv=cipher_iv, mode=AES.MODE_CBC)
    decoded = base64.b64decode(encrypted_certificate)
    decrypted = cipher.decrypt(decoded)
    decoded = base64.b64decode(decrypted).decode("utf-8")
    return json.loads(decoded)


def decode_authorization_token(jwt_token: str) -> dict:
    return jwt.decode(jwt_token, algorithms=["HS256"], options={"verify_signature": False})
