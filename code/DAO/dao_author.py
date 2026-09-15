# -*- coding: utf-8 -*-

"""
Classe Dao[Author]
"""

from dataclasses import dataclass
from typing import Optional, override
from modeles.author import Author
from dao.dao import Dao


@dataclass
class AuthorDao(Dao[Author]):

    @staticmethod
    def author_from_db(record: tuple[str, str, str]) -> Author:
        """Construit un auteur du modèle d'après son entité en BD"""
        return Author(record[0], record[1], record[2])

    @override(Dao)
    async def read(self, id_entity: int) -> Optional[Author]:
        """Renvoit le personnage correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        async with self.connection() as session:
            record = (await session.execute("""SELECT perso_name, person_lastname, biography FROM person WHERE 
                person_id = (select person_id from AUTHOR where author_id = :c)""",
                                            {"c": id_entity})).fetchone()
            return self.author_from_db(record) if record is not None else None

    @override(Dao)
    async def read_all(self) -> list[Author]:
        """Renvoit l'ensemble des personnages principaux de la BD."""
        author_list: list[Author] = []
        async with self.connection() as session:
            for record in (await session.execute("""SELECT perso_name, person_lastname, biography FROM person """)
                           ).fetchall():
                author_list.append(self.author_from_db(record))
        return author_list
