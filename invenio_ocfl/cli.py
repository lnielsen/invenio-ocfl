# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Data Futures.
# Copyright (C) 2021 CERN.
#
# Invenio-OCFL is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Command-line tools for OCFL module."""

import click
from flask.cli import with_appcontext
from invenio_access.permissions import system_identity

from invenio_ocfl.proxies import current_ocfl


@click.group()
def cli():
    """OCFL commands."""


@cli.command('export')
@click.argument('builder')
@click.option('-o', '--output')
@click.option('-q', '--query')
@with_appcontext
def export(builder, output=None, query=None):
    """Export records in OCFL."""
    click.secho('Exporting repository as OCFL...')

    current_ocfl.service.export(
        system_identity, builder, storage_path=output, query=query)
