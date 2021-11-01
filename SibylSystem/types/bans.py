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

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Ban:
    user_id: Optional[int] = None
    banned: Optional[bool] = None
    reason: Optional[str] = None
    message: Optional[str] = None
    ban_source_url: Optional[str] = None
    banned_by: Optional[int] = None
    crime_coefficient: Optional[int] = None
    date: Optional[str] = None
    ban_flags: Optional[List[str]] = None
    

@dataclass
class BanResult:
    previous_ban: Optional[Ban] = None
    current_ban: Optional[Ban] = None