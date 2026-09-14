# -*- coding: utf-8 -*-

from typing import Any
from sqlalchemy import text
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


class CustomAsyncSession(AsyncSession):
    """Session asynchrone personnalisée intégrant le wrapper text() et les méthodes utilitaires."""

    def _text(self, statement: Any) -> Any:
        return text(statement) if isinstance(statement, str) else statement