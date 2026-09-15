# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de Character, Author et JuryMember
"""

from dataclasses import dataclass
from typing import override
from abc import ABC


@dataclass
class Person(ABC):
    """Personne qui peut être un auteur, un membre du jury ou un personnage principal"""
    first_name: str
    last_name: str
    biography: str | None


