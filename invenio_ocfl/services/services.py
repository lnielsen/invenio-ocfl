# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""OCFL service layer."""

from invenio_records_resources.services import Service

from ocflcore import OCFLRepository, FileSystemStorage
from os.path import join

class OCFLService(Service):
    """OCFL Service."""

    def export(self, identity, builder_name, storage_path=None, query=None):
        """Export a full repository"""
        # self.require_permission(identity, 'export')

        builder = self.config.records[builder_name]

        if storage_path is not None:
            root = self.config.roots[builder_name]
            storage = FileSystemStorage(join(storage_path, 'root'))
            workspace = FileSystemStorage(join(storage_path, 'workspace'))
            repository = OCFLRepository(
                root, storage, workspace_storage=workspace)
        else:
            repository = self.config.repositories[builder_name]

        repository.initialize()

        for ocfl_obj in builder.scan(identity, query=query):
            repository.add(ocfl_obj)

        return True
