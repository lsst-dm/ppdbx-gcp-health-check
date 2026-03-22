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
from typing import Any

import sqlalchemy
from flask import Request

from lsst.dax.ppdb.bigquery import PpdbBigQuery

from lsst.dax.ppdbx.gcp.log_config import setup_logging

setup_logging()


def health_check(request: Request) -> dict[str, Any]:
    """Cloud Function to perform a health check on the PPDB replication
    system."""
    logging.info("Starting PPDB health check.")

    # Setup PPDB BigQuery interface from environment variable configuration
    ppdb = PpdbBigQuery.from_env()

    # Check that the Postgres database is accessible by executing a simple
    # query
    with ppdb._engine.begin() as connection:
        connection.execute(sqlalchemy.text("SELECT 1"))
        logging.info("Successfully executed test query on PPDB Postgres database.")

    # Check that BigQuery is accessible by executing a simple query
    ppdb._query_runner.run_job("health check query", "SELECT 1")

    logging.info("PPDB health check completed successfully.")

    return {"status": "healthy", "message": "Health check completed successfully"}
