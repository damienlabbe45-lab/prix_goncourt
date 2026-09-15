# -*- coding: utf-8 -*-

"""
Classe Character, fille de la classe Person
"""

from dataclasses import dataclass
from person import Person


@dataclass
class Character(Person):
    """personnage(s) principal(aux) d'un ou de plusieurs livres
    """