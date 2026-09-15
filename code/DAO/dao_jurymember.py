# -*- coding: utf-8 -*-

"""
Classe Dao[JuryMember]
"""

from dataclasses import dataclass
from typing import Optional, override
from modeles.jurymember import JuryMember
from dao.dao import Dao


@dataclass
class JuryMemberDao(Dao[JuryMember]):

    @staticmethod
    def jury_from_db(record: tuple[str, str, str, bool]) -> JuryMember:
        """Construit un auteur du modèle d'après son entité en BD"""
        return JuryMember(record[0], record[1], record[2], record[3])

