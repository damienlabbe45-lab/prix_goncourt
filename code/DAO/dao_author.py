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

