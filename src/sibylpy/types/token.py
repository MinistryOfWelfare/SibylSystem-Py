from dataclasses import dataclass
from typing import Optional
from .result import Result

@dataclass
class TokenValidation:
    success: Optional[bool] = None
    result: Optional[bool] = None
    error: Optional[str] = None


@dataclass
class CreateToken:
    error: Optional[str] = None
    success: Optional[bool] = None
    result: Optional[Result] = None