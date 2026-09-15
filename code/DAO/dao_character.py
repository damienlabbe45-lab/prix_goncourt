# -*- coding: utf-8 -*-

"""
Classe Dao[Character]
"""

from dataclasses import dataclass
from typing import Optional
from modeles.character import Character
from dao.dao import Dao


@dataclass
class CharacterDao(Dao[Character]):
    @staticmethod
    def character_from_db(record) -> Character:
        """Construit un cours du modèle d'après son entité en BD"""
        character: Character = Character(record[0], record[1], record[2])

        return character

    async def read(self, id_entity: int) -> Optional[Character]:
        """Renvoit le personnage correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        async with self.connection() as session:
            record = (await session.execute("""SELECT perso_name, person_lastname, biography FROM person WHERE 
                person_id = (select person_id from CHARACTER_BOOK where character_id = :c)""",
                                            {"c": id_entity})).fetchone()
            return self.character_from_db(record) if record is not None else None

    async def read_all(self) -> list[Character]:
        """Renvoit l'ensemble des personnages principaux de la BD."""
        character_list: list[Character] = []
        async with self.connection() as session:
            for record in (await session.execute("""SELECT perso_name, person_lastname, biography FROM person """)
                           ).fetchall():
                character_list.append(self.character_from_db(record))
        return character_list

