from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Result:
    user_id: Optional[int] = None
    hash: Optional[str] = None
    permission: Optional[int] = None
    created_at: Optional[datetime] = None
    accepted_reports: Optional[int] = None
    denied_reports: Optional[int] = None