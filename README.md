# SibylSystem-Py

>Python3 wrapper for the Sibyl System antispam API for telegram

## Installation

```
pip install sibylsystem
```

# Usage

```py
>>> from SibylSystem import PsychoPass
>>> c = PsychoPass("your token")

    SibylSystem-Py Copyright (C) 2024 Kaizoku
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.

>>> c.get_info(2037525377)
Ban(user_id=2037525377, banned=True, reason='Arcane', message='', ban_source_url='', date='2021-10-30T18:47:00.004137+05:30', banned_by=895373440, crime_coefficient=0)
```

# Docs ?

**Open the source and read the docstrings**
