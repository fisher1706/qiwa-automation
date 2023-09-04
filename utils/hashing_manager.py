import bcrypt
import pkce


class HashingManager:
    @staticmethod
    def hash_string_with_salt(string):
        byte_string = string.encode("utf-8")
        salt = bcrypt.gensalt(rounds=12)
        return str(bcrypt.hashpw(byte_string, salt)).strip("b'")

    @staticmethod
    def code_challenge_string() -> str:
        challenge_string = pkce.generate_code_verifier(length=64)
        return challenge_string

    @staticmethod
    def code_challenge(string: str) -> str:
        code_challenge = pkce.get_code_challenge(string)
        return code_challenge
