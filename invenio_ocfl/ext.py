# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""OCFL module for InvenioRDM."""

from . import config


class InvenioOCFL(object):
    """Invenio-OCFL extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['invenio-ocfl'] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith('OCFL_'):
                app.config.setdefault(k, getattr(config, k))
