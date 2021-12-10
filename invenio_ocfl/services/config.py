# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""OCFL service layer."""

from invenio_records_resources.services import ServiceConfig
from ocflcore import OCFLRepository, StorageRoot


class OCFLServiceConfig(ServiceConfig):
    """OCFL Service Config."""

    def __init__(self, records=None, roots=None, storages=None,
                 repositories=None):
        """Constructor."""
        # Setup roots and storages.
        self.roots = roots or {}
        self.storages = storages or {}
        self.records = records

        # Setup OCFL repositories
        self.repositories = {}
        for name, conf in (repositories or {}).items():
            self.repositories[name] = OCFLRepository(
                self.roots[conf['root']],
                self.storages[conf['storage']],
                workspace_storage=self.storages[conf['workspace_storage']],
            )
