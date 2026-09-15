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

    @override(Dao)
    async def read(self, id_entity: int) -> Optional[JuryMember]:
        """Renvoit le personnage correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        async with self.connection() as session:
            record = (await session.execute("""SELECT perso_name, person_lastname, biography FROM person WHERE 
                person_id = (select person_id from AUTHOR where author_id = :c)""",
                                            {"c": id_entity})).fetchone()
            return self.jury_from_db(record) if record is not None else None

