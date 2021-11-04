from dataclasses import dataclass
from typing import Optional


@dataclass
class Error:
    code: Optional[int] = None
    message: Optional[str] = None
    origin: Optional[str] = None
    date: Optional[str] = None