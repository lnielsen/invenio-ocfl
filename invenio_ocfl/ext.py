# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""OCFL module for InvenioRDM."""

from . import config
from .services import OCFLService, OCFLServiceConfig


class InvenioOCFL(object):
    """Invenio-OCFL extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        self.init_services(app)
        app.extensions['invenio-ocfl'] = self

    def init_services(self, app):
        """Initialize service."""
        self.service = OCFLService(config=OCFLServiceConfig(
            records=app.config['OCFL_RECORDS'],
            roots=app.config['OCFL_ROOTS'],
            storages=app.config['OCFL_STORAGES'],
            repositories=app.config['OCFL_REPOSITORIES'],
        ))

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith('OCFL_'):
                app.config.setdefault(k, getattr(config, k))
