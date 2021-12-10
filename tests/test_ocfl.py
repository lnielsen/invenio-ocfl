# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from ocfl import Object as OCFLObject, VersionMetadata


def test_ocflpy(tmpdir):
    o = OCFLObject(identifier='12345-abcde')
