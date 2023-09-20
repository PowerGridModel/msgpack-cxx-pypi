# SPDX-FileCopyrightText: 2022 Contributors to the Power Grid Model project <dynamic.grid.calculation@alliander.com>
#
# SPDX-License-Identifier: MPL-2.0


from pathlib import Path

from msgpack_cxx import get_include


def test_header():
    include_path: Path = get_include()
    assert (include_path / "msgpack.hpp").exists()
