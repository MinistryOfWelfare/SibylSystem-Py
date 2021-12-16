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

from typing import Optional, Dict

from pydantic import BaseModel

from .error import Error

class SibylStats:
    banned_count: int = 0
    trolling_ban_count: int = 0
    spam_ban_count: int = 0
    evade_ban_count: int = 0
    custom_ban_count: int = 0
    psycho_hazard_ban_count: int = 0
    mal_imp_ban_count: int = 0
    nsfw_ban_count: int = 0
    spam_bot_ban_count: int = 0
    raid_ban_count: int = 0
    mass_add_ban_count: int = 0
    cloudy_count: int = 0
    token_count: int = 0
    inspectors_count: int = 0
    enforces_count: int = 0

class StatsResult(BaseModel):
    error: Optional[Error] = None
    success: Optional[bool] = None
    result: Optional[SibylStats] = None
