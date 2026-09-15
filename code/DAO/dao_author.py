# -*- coding: utf-8 -*-

"""
Classe Dao[Author]
"""

from dataclasses import dataclass
from typing import Optional, override
from modeles.author import Author
from dao.dao import Dao


@dataclass
class AuthorDao(Dao[Author]):

    @staticmethod
    def author_from_db(record: tuple[str, str, str]) -> Author:
        """Construit un auteur du modèle d'après son entité en BD"""
        return Author(record[0], record[1], record[2])
