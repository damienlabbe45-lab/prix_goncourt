# -*- coding: utf-8 -*-

"""
Classe LiteraryPrize
"""

from dataclasses import dataclass, field
from typing import override
from modeles.jurymember import JuryMember


@dataclass
class LiteraryPrize:
    """nom d'un prix littéraire avec sa liste des membres du jury"""
    name_prize: str
    list_jury_member: list[JuryMember] = field(default_factory=list)

    @override
    def __str__(self) -> str:
        return f"{self.name_prize}" + "- \n".join(map(str, self.list_jury_member))

    def add_list_jurymember(self, jury: JuryMember) -> None:
        self.list_jury_member.append(jury)

    def remove_list_jurymember(self, jury: JuryMember) -> None:
        self.list_jury_member.remove(jury)
