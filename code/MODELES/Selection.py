# -*- coding: utf-8 -*-

"""
Classe Selection
"""

from dataclasses import dataclass, field
from typing import override
from abc import ABC
from datetime import date
from LIteraryPrize import LiteraryPrize
from Book import Book


@dataclass
class Selection(ABC):
    """Selection des livres par les prix littéraires ainsi que le nombre de vote pour chaque livre"""
    date_selection: date
    name_prize: LiteraryPrize
    selection: int
    dic_book_vote: dict[Book, int] = field(default_factory=dict)

