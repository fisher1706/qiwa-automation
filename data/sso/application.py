from pydantic import BaseModel

from utils.hashing_manager import HashingManager
from utils.random_manager import RandomManager


class Application(BaseModel):
    app_name = RandomManager().random_eng_string(letters_quantity=5)
    app_description = RandomManager().random_eng_string(letters_quantity=10)
    client_id = RandomManager().generate_safe_url_string()
    client_secret = HashingManager().hash_string_with_salt(client_id)
    url = RandomManager().generate_url()
    uri = RandomManager().generate_url(path="oauth/callback")
    permissions = "permissions"
    scopes = "openid profile email phone"
    main = False
    code_challenge_str = HashingManager().code_challenge_string()
    code_challenge = HashingManager().code_challenge(code_challenge_str)
    code_challenge_method = "S256"
