# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Factory for OCFL objects from records."""

from io import BytesIO

import arrow
from ocflcore import OCFLObject, OCFLVersion, StreamDigest


class OCFLObjectBuilder:
    """OCFL Object factory."""

    serializers = {}
    service = None

    def scan(self, identity, query=None):
        """Scan for records."""
        for res in self.service.scan(identity, q=query or ''):
            yield self.build_ocfl_object(res)

    def metadata(self, record):
        """"Build metadata files."""
        for filename, serializer in self.serializers.items():
            content = serializer.serialize_object(record)
            bytes = StreamDigest(BytesIO(content.encode('utf8')))
            yield filename, bytes.stream, bytes.digest

    def files(self, record):
        """"Build data files."""
        return []

    def build_ocfl_object(self, record):
        """Build the OCFL object."""
        # Just one version for now
        timestamp = arrow.get(record['created'])
        v = OCFLVersion(timestamp.datetime)

        # Metadata files
        for filename, stream, digest in self.metadata(record):
            v.files.add(filename, stream, digest)

        # Data files
        for filename, stream, digest in self.files(record):
           v.files.add(filename, stream, digest)

        o = OCFLObject(record['id'])
        o.versions.append(v)
        return o
