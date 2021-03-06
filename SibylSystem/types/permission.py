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

from enum import Enum
from typing import Optional

from pydantic import BaseModel

from .error import Error


class PermissionResponse(BaseModel):
    success: Optional[bool] = None
    result: Optional[str] = None
    error: Optional[Error] = None


class Permissions(Enum):
    USER = 0
    ENFORCER = 1
    INSPECTOR = 2
    OWNER = 3
