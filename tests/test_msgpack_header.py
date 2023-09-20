from pathlib import Path

from msgpack_cxx import get_include


def test_header():
    include_path: Path = get_include()
    assert (include_path / "msgpack.hpp").exists()
