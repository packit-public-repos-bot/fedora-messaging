# This file is part of fedora_messaging.
# Copyright (C) 2018 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os

import crochet
import pytest

from .utils import get_available_port


@pytest.fixture(autouse=True, scope="session")
def crochet_no_setup():
    crochet.no_setup()


@pytest.fixture
def fixtures_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "fixtures/"))


@pytest.fixture
def available_port():
    try:
        import pytest_twisted
    except ImportError:
        pytest.skip("pytest-twisted is missing, skipping tests", allow_module_level=True)

    return pytest_twisted.blockon(get_available_port())
