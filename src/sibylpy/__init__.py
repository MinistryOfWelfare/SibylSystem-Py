# SibylPy

# Copyright (C) 2021 Sayan Biswas, AnonyIndian

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import httpx, typing

from .types import TokenValidation, Ban, BanResult, Token, PermissionResponse
from .exceptions import GeneralException, InvalidTokenException, InvalidPermissionRangeException
__version__ = '0.0.2'

class SibylClient:
    def __init__(self, host: str, token: str, client: typing.Optional[httpx.Client] = None, show_license: bool = True) -> None:
        if show_license:
            l = '''
    SibylPy Copyright (C) 2021 Sayan Biswas, AnonyIndian
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.
            '''
            print(l)
        if not host.endswith("/"):
            host += "/"
        if not host.startswith("http"):
            host = "http://" + host
        self.host = host
        self.token = token
        self.client = client
        if not self.client:
            self.client = httpx.Client()
        if not self.check_token(self.token):
            raise InvalidTokenException()
    
    def check_token(self, token: str):
        r = self.client.get(f"{self.host}checkToken?token={token}")
        x = TokenValidation(**r.json())
        if not x.success:
            raise InvalidTokenException()
        return x.result

    def create_token(self, user_id: int, permission: int = 0):
        if permission > 2:
            raise InvalidPermissionRangeException("Permission can be 0, 1, 2, not {}".format(permission))
        r = self.client.get(f"{self.host}createToken?token={self.token}&user-id={user_id}&permission={permission}")
        if r.status_code != 200:
            raise GeneralException("Failed to create token")
        return Token(**r.json()["result"])

    def revoke_token(self, user_id: int):
        return self._token_method(
            'revokeToken?token=', user_id, "Failed to revoke token"
        )

    def change_permission(self, user_id: int, permission: int):
        r = self.client.get(f"{self.host}changePerm?token={self.token}&user-id={user_id}&permission={permission}")
        if r.status_code != 200:
            raise GeneralException("Failed to change permission")
        return PermissionResponse(**r.json())
    
    def get_token(self, user_id: int):
        return self._token_method(
            'getToken?token=', user_id, "Failed to get token"
        )

    def _token_method(self, arg0, user_id, arg2):
        r = self.client.get(f'{self.host}{arg0}{self.token}&user-id={user_id}')
        if r.status_code != 200:
            raise GeneralException(arg2)
        return Token(**r.json()['result'])
        
    def add_ban(self, user_id: int, reason: str, message: str=None, source: str=None):
        r = self.client.get(f"{self.host}addBan?token={self.token}&user-id={user_id}&reason={reason}&message={message}&source={source}")
        if r.status_code != 200:
            raise GeneralException("Failed to add ban")
        return BanResult(**r.json()["result"])
    
    def delete_ban(self, user_id: int):
        r = self.client.get(f"{self.host}removeBan?token={self.token}&user-id={user_id}")
        if r.status_code != 200:
            raise GeneralException("Failed to delete ban")
        return True
    
    def get_info(self, user_id: int):
        r = self.client.get(f"{self.host}getInfo?token={self.token}&user-id={user_id}")
        if r.status_code != 200:
            raise GeneralException("Failed to get info")
        return Ban(**r.json()["result"])

    def report_user(self, user_id: int, reason: str, message: str=None):
        r = self.client.get(f"{self.host}reportUser?token={self.token}&user-id={user_id}&reason={reason}&message={message}")
        if r.status_code != 200:
            raise GeneralException("Failed to delete ban")
        return True


    
