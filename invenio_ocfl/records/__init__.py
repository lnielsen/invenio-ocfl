# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""OCFL data layer."""

from .repository import OCFLRepository
from .storage import FileSystemStorage

__all__ = (
    'OCFLRepository',
    'FileSystemStorage',
)
