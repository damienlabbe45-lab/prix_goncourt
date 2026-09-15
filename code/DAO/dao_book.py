# -*- coding: utf-8 -*-

"""
Classe Dao[Book]
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional, override
from modeles.book import Book
from dao.dao import Dao
from dao.dao_author import AuthorDao
from modeles.author import Author
from dao.dao_character import CharacterDao


@dataclass
class BookDao(Dao[Book]):
    @staticmethod
    def book_from_db(record: tuple[str, str, int, float, str, str, date], author: Author) -> Book:
        """Construit un livre du modèle d'après son entité en BD"""
        return Book(record[0], record[1], record[2], record[3], record[4], record[5], record[6], author)

