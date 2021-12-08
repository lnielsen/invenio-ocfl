# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""


def test_version():
    """Test version import."""
    from invenio_ocfl import __version__
    assert __version__


def test_init(app):
    """Test extension initialization."""
    assert 'invenio-ocfl' in app.extensions
