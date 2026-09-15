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
