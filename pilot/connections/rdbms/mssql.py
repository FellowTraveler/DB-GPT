#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Optional, Any

from pilot.connections.rdbms.rdbms_connect import RDBMSDatabase


class MSSQLConnect(RDBMSDatabase):
    """Connect MSSQL Database fetch MetaData
    Args:
    Usage:
    """

    db_type: str = "mssql"
    db_dialect: str = "mssql"
    driver: str = "pyodbc"

    default_db = ["master", "model", "msdb", "tempdb", "modeldb", "resource"]
