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


