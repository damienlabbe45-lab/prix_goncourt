# -*- coding: utf-8 -*-

"""
Classe LiteraryPrize
"""

from dataclasses import dataclass
from typing import override
from abc import ABC
from JuryMember import JuryMember


@dataclass
class LiteraryPrize(ABC):
    """nom d'un prix littéraire avec sa liste des membres du jury"""
    name_prize: str
    list_JuryMember: list[JuryMember]


