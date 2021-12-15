from typing import Optional

from pydantic import BaseModel

from .error import Error
from ..types import Permissions


class GeneralInfoResult(BaseModel):
    user_id: Optional[int] = None
    division: Optional[int] = None
    assigned_by: Optional[int] = None
    assigned_reason: Optional[str] = None
    assigned_at: Optional[str] = None
    permission: Optional[Permissions] = None

    def is_registered(self) -> bool:
        """
        Returns whether the user is considered as a registered user or not.
        Enforcers, Inspectors and Owners are considered as registered users.
        """
        return self.permission.value > Permissions.USER.value


class GeneralInfo(BaseModel):
    error: Optional[Error]
    success: Optional[bool] = None
    result: Optional[GeneralInfoResult] = None

    def is_registered(self) -> bool:
        """
        Returns whether the user is considered as a registered user or not.
        Enforcers, Inspectors and Owners are considered as registered users.
        """
        return self.result != None and self.result.is_registered()
