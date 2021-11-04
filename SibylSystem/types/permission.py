from dataclasses import dataclass
from typing import Optional
from enum import Enum

@dataclass
class PermissionResponse:
    success: Optional[bool] = None
    result: Optional[str] = None
    error: Optional[str] = None
    
    
class Permissions(Enum):
    USER = 0
    ENFORCER = 1
    INSPECTOR = 2