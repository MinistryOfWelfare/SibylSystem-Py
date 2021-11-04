from dataclasses import dataclass
from typing import Optional
from enum import Enum

from SibylSystem.types.error import Error

@dataclass
class PermissionResponse:
    success: Optional[bool] = None
    result: Optional[str] = None
    error: Optional[Error] = None
    
    
class Permissions(Enum):
    USER = 0
    ENFORCER = 1
    INSPECTOR = 2