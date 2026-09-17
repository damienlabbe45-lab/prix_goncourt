#!/usr/bin/env python
# -*- coding: utf-8 -*-
from asyncio import run
from test_data.insert_data import insert_data
from test_data.sql_create_table import create_table
from interface.charman_jury_interface import CharmanJuryInterface
from utils.logs import LogErreur

"""
Application des prix littéraires
"""


async def main() -> None:
    """Programme principal."""
    LogErreur().loggingperso()
    await create_table()
    await insert_data()
    await CharmanJuryInterface().selection_charman_initial()

if __name__ == '__main__':
    run(main())
