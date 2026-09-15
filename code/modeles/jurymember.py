# -*- coding: utf-8 -*-

"""
Classe JuryMember, fille de la classe Person
"""

from dataclasses import dataclass
from person import Person
from typing import override


@dataclass
class JuryMember(Person):
    """membre du jury d'un prix littéraire
    chairman: indique si c'est le président du membre des jurys du prix littéraire
    """
    chairman: bool

    @override(Person)
    def __str__(self):
        return f" {"président  d' un " if self.chairman else ""} membre du jury {super().__str__()}"