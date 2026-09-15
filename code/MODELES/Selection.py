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

    @override(ABC)
    def __str__(self) -> str:
        list_results: list[str] = [str(key) + f": {values} votes" for key, values in self.dic_book_vote.items()]
        return f""" la sélection numéro {self.selection} du prix littéraire {self.name_prize} a lieu le 
{self.date_selection}. voici les résultats du vote: {"- \n".join(list_results)}"""


