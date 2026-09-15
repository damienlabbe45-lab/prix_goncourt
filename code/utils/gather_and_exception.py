from typing import Any
from collections.abc import Awaitable
from asyncio import gather


def manage_exception(exceptions: list[Any]) -> list[Any]:
    """gère toutes les exceptions lors d'éxécutions en parallèle"""
    exceptionss = [r for r in exceptions if isinstance(r, BaseException)]
    if exceptionss:
        if len(exceptionss) > 1:
            raise BaseExceptionGroup(
                "une ou plusieurs exceptions se sont produites", exceptionss)
        raise exceptionss[0]
    return exceptions


async def gather_exceptions(*coros: Awaitable[Any]) -> list[Any]:
    """gere les exceptions de gather de manière générale et éxécute les coroutines en parralèle"""
    return manage_exception(await gather(*coros, return_exceptions=True))
