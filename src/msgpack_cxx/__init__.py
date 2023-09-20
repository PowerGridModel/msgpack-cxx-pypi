# SPDX-FileCopyrightText: 2022 Contributors to the Power Grid Model project <dynamic.grid.calculation@alliander.com>
#
# SPDX-License-Identifier: MPL-2.0

from pathlib import Path
from importlib_resources import files


def get_include() -> Path:
    return files("msgpack_cxx.include")
