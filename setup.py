#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 The MUSSLES developers
#
# This file is part of MUSSLES.
#
# MUSSLES is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MUSSLES is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MUSSLES.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

exec(open("pipeline/version.py").read())  # grab version info


setup(
    name="pipeline",
    version=__version__,
    description="TODO",
    author=__author__,
    author_email=__email__,
    license="GPLv3",
    url="https://github.com/MUSSLES/pipeline",
    classifiers=["Programming Language :: Python :: 3.6"],
    packages=["pipeline"],
    entry_points={"console_scripts": ["pipeline=pipeline:cli_main"]},
    package_data={
        "": ["LICENSE", "readme.rst", "requirements.txt"],
        "pipeline": ["*.py"],
    },
)
