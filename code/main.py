#!/usr/bin/env python
# -*- coding: utf-8 -*-
from asyncio import run
from test_data.insert_data import insert_data
from test_data.sql_create_table import create_table

"""
Application des prix littéraires
"""


async def main() -> None:
    """Programme principal."""
    await create_table()
    await insert_data()

if __name__ == '__main__':
    run(main())
