# SibylSystem-py

# Copyright (C) 2021 Sayan Biswas, AnonyIndian

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import Optional

from pydantic import BaseModel

from .error import Error


class ReportResponse(BaseModel):
    success: Optional[bool] = None
    result: Optional[str] = None
    error: Optional[Error] = None

class MultiScanInfo:
    user_id: int = None
    reason: Optional[str] = ''
    message: Optional[str] = ''
    target_type: Optional[int] = 0

    def __init__(self, 
            user_id: int, 
            reason: str = '', 
            message: str = '', 
            target_type: int = 0,
        ):
        self.user_id = user_id
        self.reason = reason
        self.message = message
        self.target_type = target_type

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "reason": self.reason,
            "message": self.message,
            "target_type": self.target_type,
        }