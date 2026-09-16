#!/usr/bin/env python
# -*- coding: utf-8 -*-
from asyncio import run
from test_data.insert_data import insert_data

"""
Application des prix littéraires
"""


async def main() -> None:
    """Programme principal."""
    try:
        await insert_data()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    run(main())
