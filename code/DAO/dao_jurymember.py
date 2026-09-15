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
        """Construit un membre du jury du modèle d'après son entité en BD"""
        return JuryMember(record[0], record[1], record[2], record[3])

    @override(Dao)
    async def read(self, id_entity: int) -> Optional[JuryMember]:
        """Renvoit le membre du jury correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        async with self.connection() as session:
            record = (await session.execute("""SELECT perso_name, person_lastname, biography, chairman FROM person 
            OIN JURY_MEMBER ON person.person_id = JURY_MEMBER.person_id WHERE member_id = :c""", {"c": id_entity})
                      ).fetchone()
            return self.jury_from_db(record) if record is not None else None

    @override(Dao)
    async def read_all(self) -> list[JuryMember]:
        """Renvoit l'ensemble des membres des jurys de la BD."""
        author_list: list[JuryMember] = []
        async with self.connection() as session:
            for record in (await session.execute("""SELECT perso_name, person_lastname, biography, chairman FROM person 
            JOIN JURY_MEMBER ON person.person_id = JURY_MEMBER.person_id """)).fetchall():
                author_list.append(self.jury_from_db(record))
        return author_list
