from dataclasses import dataclass
from typing import Optional


@dataclass
class PermissionResponse:
    success: Optional[bool] = None
    result: Optional[str] = None
    error: Optional[str] = None