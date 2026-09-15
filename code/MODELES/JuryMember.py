# -*- coding: utf-8 -*-

"""
Classe JuryMember, fille de la classe Person
"""

from dataclasses import dataclass
from person import Person


@dataclass
class JuryMember(Person):
    """membre du jury d'un prix littéraire
    chairman: indique si c'est le président du membre des jurys du prix littéraire
    """
    chairman: bool
