# -*- coding: utf-8 -*-

"""
Classe Dao[LiteraryPrize]
"""

from dataclasses import dataclass
from typing import Optional, override
from modeles.lIteraryprize import LiteraryPrize
from dao.dao import Dao
from dao.dao_jurymember import JuryMemberDao


@dataclass
class LiteraryPrizeDao(Dao[LiteraryPrize]):


