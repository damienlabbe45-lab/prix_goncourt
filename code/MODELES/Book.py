# -*- coding: utf-8 -*-

"""
Classe book
"""

from dataclasses import dataclass
from typing import override
from abc import ABC
from datetime import date
from Author import Author
from Character import Character


@dataclass
class Book(ABC):
    """livre avec son auteur,
    ses persos principaux,
    son résumé,
    son titre,
    son éditeur,
    son ISBN,
    son prix,
    sa date de parution,
    son nombre de page"""

    title: str
    editor: str
    number_page: int
    price: float
    ISBN: str
    summarize: str
    release_book: date
    author_book: Author
    list_main_character: list[Character]
