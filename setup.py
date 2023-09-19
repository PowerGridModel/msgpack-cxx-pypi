# SPDX-FileCopyrightText: 2022 Contributors to the Power Grid Model project <dynamic.grid.calculation@alliander.com>
#
# SPDX-License-Identifier: MPL-2.0

import os
import platform
import shutil
from itertools import chain
from pathlib import Path
from typing import List

# noinspection PyPackageRequirements
from setuptools import setup
from setuptools.command.build_ext import build_ext
from wheel.bdist_wheel import bdist_wheel


class bdist_wheel_abi_none(bdist_wheel):
    def finalize_options(self):
        bdist_wheel.finalize_options(self)
        self.root_is_pure = False

    def get_tag(self):
        python, abi, plat = bdist_wheel.get_tag(self)
        return "py3", "none", plat


def generate_build_ext(pkg_dir: Path, pkg_name: str):
    """
    Generate extension dict for setup.py
    the return value ext_dict, can be called in setup(**ext_dict)
    Args:
        pkg_dir:
        pkg_name:
    Returns:

    """

    # return dict of exts
    return {"cmdclass": {"bdist_wheel": bdist_wheel_abi_none}}


def get_msgpack(pkg_dir: Path):
    if not pkg_dir.is_dir():
        raise NotImplementedError()


def prepare_pkg(setup_file: Path) -> dict:
    """

    Args:
        setup_file:
    Returns:

    """
    print(f"Build wheel from {setup_file}")
    pkg_dir = setup_file.parent / "msgpack-cxx"
    # package description
    pkg_pip_name = "msgpack-cxx"
    pkg_name = pkg_pip_name.replace("-", "_")
    return generate_build_ext(pkg_dir=pkg_dir, pkg_name=pkg_name)


setup(
    **prepare_pkg(setup_file=Path(__file__).resolve()),
)
