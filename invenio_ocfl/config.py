# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""OCFL module for InvenioRDM."""

from invenio_rdm_records.ocfl import RDMRecordBuilder
from ocflcore import FileSystemStorage, StorageRoot, TopLevelLayout

OCFL_RECORDS = {
    "rdm": RDMRecordBuilder()
}
"""Config for defining records."""


OCFL_ROOTS = {
    "rdm": StorageRoot(TopLevelLayout())
}
"""Configuration of storage roots."""


OCFL_STORAGES = {
    "rdm-root": FileSystemStorage("...."),
    "rdm-workspace": FileSystemStorage("...."),
}
"""Storage definitions."""


OCFL_REPOSITORIES = {
    "rdm": {
        "root": "rdm",
        "storage": "rdm-root",
        "workspace_storage": "rdm-workspace",
    }
}
"""Definition of repositories."""
