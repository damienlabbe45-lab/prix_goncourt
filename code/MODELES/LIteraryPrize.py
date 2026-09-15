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

    @override(ABC)
    def __str__(self) -> str:
        return f"{self.name_prize}" + "- \n".join(map(str, self.list_JuryMember))

    def add_list_jurymember(self, jury: JuryMember) -> None:
        self.list_JuryMember.append(jury)


