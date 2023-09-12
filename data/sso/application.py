from pydantic import BaseModel

from utils.hashing_manager import HashingManager
from utils.random_manager import RandomManager


class Application(BaseModel):
    app_name: str = RandomManager().random_eng_string(letters_quantity=5)
    app_description: str = RandomManager().random_eng_string(letters_quantity=10)
    client_id: str = RandomManager().generate_safe_url_string()
    client_secret: str = HashingManager().hash_string_with_salt(client_id)
    url: str = RandomManager().generate_url()
    uri: str = RandomManager().generate_url(path="oauth/callback")
    permissions: str = "permissions"
    scopes: str = "openid profile email phone"
    main: bool = False
    code_challenge_str: str = HashingManager().code_challenge_string()
    code_challenge: str = HashingManager().code_challenge(code_challenge_str)
    code_challenge_method: str = "S256"
