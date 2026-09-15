# -*- coding: utf-8 -*-

"""
Classe Author, fille de la classe Person
"""

from dataclasses import dataclass
from person import Person


@dataclass
class Author(Person):
    """Auteur d'un livre
    """
