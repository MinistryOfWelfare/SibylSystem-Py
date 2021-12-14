from typing import Optional

from pydantic import BaseModel

from .error import Error


class Result(BaseModel):
    user_id: Optional[int] = None
    division: Optional[int] = None
    assigned_by: Optional[int] = None
    assigned_reason: Optional[str] = None
    assigned_at: Optional[str] = None
    permission: Optional[int] = None


class GeneralInfo(BaseModel):
    error: Optional[Error]
    success: Optional[bool] = None
    result: Optional[Result] = None
