import httpx, typing
from .types import TokenValidation, CreateToken
from .exceptions import GeneralException, InvalidTokenException, InvalidPermissionRangeException
__version__ = '0.1.0'

class SibylClient:
    def __init__(self, host: str, token: str, client: typing.Optional[httpx.Client] = None) -> None:
        if not host.endswith("/"):
            host += "/"
        self.host = host
        self.token = token
        self.client = client
        if not self.client:
            self.client = httpx.Client()
        r = self.client.get(f"{self.host}checkToken?token={self.token}")
        x = TokenValidation(**r.json())
        if not x.success:
            raise InvalidTokenException()
    
    def create_token(self, user_id: int, permission: int = 0) -> CreateToken:
        if permission > 2:
            raise InvalidPermissionRangeException("Permission can be 0, 1, 2, not {}".format(permission))
        r = self.client.get(f"{self.host}createToken?token={self.token}&user-id={user_id}&permission={permission}")
        if r.status_code != 200:
            raise GeneralException("Failed to create token")
        return CreateToken(**r.json())
    
    def get_token(self, user_id: int):
        r = self.client.get(f"{self.host}getToken?token={self.token}&user-id={user_id}")
        if r.status_code != 200:
            raise GeneralException("Failed to get token")
        return CreateToken(**r.json())
        
        