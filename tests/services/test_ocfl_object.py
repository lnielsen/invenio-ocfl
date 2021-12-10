# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Test of an OCFL Object."""

from datetime import datetime, timezone
from io import BytesIO
from os.path import exists, join

import pytest

from invenio_ocfl.records import FileSystemStorage, OCFLRepository
from invenio_ocfl.services import OCFLObject, OCFLVersion, StorageRoot, \
    StreamDigest, TopLevelLayout


#
# Fixtures
#
@pytest.fixture()
def repository(tmpdir):
    storage = FileSystemStorage(tmpdir.mkdir('root'))
    workspace_storage = FileSystemStorage(tmpdir.mkdir('workspace'))
    root = StorageRoot(TopLevelLayout())
    repository = OCFLRepository(
        root, storage, workspace_storage=workspace_storage)
    repository.initialize()
    return repository


@pytest.fixture()
def minimal_obj(now):
    example_file = StreamDigest(BytesIO(b'minimal example'))
    v = OCFLVersion(now)
    v.files.add('file.txt', example_file.stream, example_file.digest)

    o = OCFLObject('12345-abcde')
    o.versions.append(v)
    return o


@pytest.fixture()
def now():
    return datetime.now(timezone.utc)


#
# Tests
#
def test_ocflobject(now):
    example_file = StreamDigest(BytesIO(b'minimal example'))

    v = OCFLVersion(now)
    v.files.add('file.txt', example_file.stream, example_file.digest)

    o = OCFLObject('12345-abcde')
    o.versions.append(v)

    assert o.id == '12345-abcde'
    assert len(o.versions) == 1
    assert len(o.versions[0].files) == 1
    assert o.head == o.versions[0]


def test_repository_init(tmpdir):
    storage = FileSystemStorage(tmpdir.mkdir('root'))
    workspace_storage = FileSystemStorage(tmpdir.mkdir('workspace'))
    root = StorageRoot(TopLevelLayout())
    repository = OCFLRepository(root, storage, workspace_storage)
    repository.initialize()

    assert exists(join(tmpdir, 'root/0=ocfl_1.1'))
    assert exists(join(tmpdir, 'root/ocfl_layout.json'))
    assert not exists(join(tmpdir, 'root/ocfl_1.1.txt'))


def test_repository_add(tmpdir, repository, minimal_obj):
    repository.add(minimal_obj)
    breakpoint()
    assert exists(join(tmpdir, 'root/0=ocfl_1.1'))
    assert exists(join(tmpdir, 'root/ocfl_layout.json'))

