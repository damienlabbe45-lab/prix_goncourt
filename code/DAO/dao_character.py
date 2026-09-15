# -*- coding: utf-8 -*-

"""
Classe Dao[Character]
"""

from dataclasses import dataclass
from typing import Optional
from modeles.character import Character
from dao.dao import Dao


@dataclass
class CharacterDao(Dao[Character]):
    @staticmethod
    def character_from_db(record) -> Character:
        """Construit un cours du modèle d'après son entité en BD"""
        character: Character = Character(record[0], record[1], record[2])

        return character



