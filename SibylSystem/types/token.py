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

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TokenValidation(BaseModel):
    success: Optional[bool] = None
    result: Optional[bool] = None
    error: Optional[str] = None


class Token(BaseModel):
    user_id: Optional[int] = None
    hash: Optional[str] = None
    permission: Optional[int] = None
    created_at: Optional[str] = None
    accepted_reports: Optional[int] = None
    denied_reports: Optional[int] = None

    def get_datetime(self) -> datetime:
        return datetime.strptime(self.created_at, "%Y-%m-%d at %H:%M:%S")
