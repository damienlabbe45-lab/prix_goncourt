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

    @staticmethod
    def prize_from_db(record: str) -> LiteraryPrize:
        """Construit un prix littéraire du modèle d'après son entité en BD"""
        return LiteraryPrize(record)

    @override(Dao)
    async def read(self, id_entity: int) -> Optional[LiteraryPrize]:
        """Renvoit le prix littéraire correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        async with self.connection() as session:
            record = await session.scalar("""SELECT prize_name FROM LITERARY_PRIZE where prize_id =:c""",
                                          {"c": id_entity})
            if record is None:
                return record
            prize = self.prize_from_db(record)
            for jurys in JuryMemberDao.read(
                    await session.scalars("""SELECT member_id FROM TO_BE_MEMBER_OF where prize_id =:c""",
                                          {"c": id_entity})):
                prize.add_list_jurymember(jurys)
            return prize

