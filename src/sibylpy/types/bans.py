from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Ban:
    user_id: Optional[int] = None
    banned: Optional[bool] = None
    reason: Optional[str] = None
    message: Optional[str] = None
    ban_source_url: Optional[str] = None
    date: Optional[datetime] = None
    banned_by: Optional[int] = None
    crime_coefficient: Optional[int] = None
    

@dataclass
class BanResult:
    previous_ban: Optional[Ban] = None
    current_ban: Optional[Ban] = None
    
@dataclass
class AddBan:
    error: None
    success: Optional[bool] = None
    result: Optional[BanResult] = None