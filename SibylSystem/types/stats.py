from dataclasses import dataclass
from typing import Optional, Dict

from SibylSystem.types.error import Error


@dataclass
class StatsResult:
    error: Optional[Error] = None
    success: Optional[bool] = None
    result: Optional[Dict[str, int]] = None