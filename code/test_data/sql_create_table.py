from pathlib import Path
from utils.utils import execute_insert
from aiofiles import open


async def create_table() -> None:
    file_sql = Path(__file__).resolve().parents[2] / 'bdd' / 'prix_goncourt.sql'
    async with open(file_sql, mode="r", encoding="utf-8") as file:
        file = await file.read()
        statements = [s.strip() for s in file.split(";") if s.strip()]
    for statement in statements:
        await execute_insert(statement)
