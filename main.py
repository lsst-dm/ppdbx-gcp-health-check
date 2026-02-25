# This file is part of ppdb-cloud-functions
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
import os
from typing import Any

import sqlalchemy
from flask import Request

from lsst.dax.ppdb.ppdb_config import PpdbConfig
from lsst.dax.ppdb.ppdb import Ppdb
from lsst.dax.ppdb.bigquery.ppdb_bigquery import PpdbBigQuery, PpdbBigQueryConfig

from lsst.dax.ppdbx.gcp.log_config import setup_logging

setup_logging()


def health_check(request: Request) -> dict[str, Any]:
    """Cloud Function to perform a health check on the PPDB replication
    system."""
    logging.info("Starting PPDB health check.")

    ppdb_config_uri = os.environ.get("PPDB_CONFIG_URI")
    if ppdb_config_uri:
        logging.info("PPDB_CONFIG_URI: %s", ppdb_config_uri)
    else:
        raise RuntimeError("PPDB_CONFIG_URI environment variable is not set.")

    ppdb_config = PpdbConfig.from_uri(ppdb_config_uri)
    logging.info("Loaded PPDB configuration: %s", ppdb_config)

    assert isinstance(ppdb_config, PpdbBigQueryConfig), (
        "ppdb_config is not of type PpdbBigQueryConfig"
    )

    ppdb = Ppdb.from_config(ppdb_config)
    logging.info("Created PPDB instance of type %s", type(ppdb))
    assert isinstance(ppdb, PpdbBigQuery), "PPDB instance is not of type PpdbBigQuery"

    with ppdb._engine.begin() as connection:
        connection.execute(sqlalchemy.text("SELECT 1"))
        logging.info("Successfully executed test query on PPDB Postgres database.")

    logging.info("PPDB health check completed successfully.")

    return {"status": "healthy", "message": "Health check completed successfully"}
