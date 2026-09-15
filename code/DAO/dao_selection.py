# -*- coding: utf-8 -*-

"""
Classe Dao[Selection]
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional, override
from modeles.selection import Selection
from dao.dao import Dao
from dao.dao_literary_prize import LiteraryPrizeDao
from dao.dao_book import BookDao
from modeles.lIteraryprize import LiteraryPrize


@dataclass
class SelectionDao(Dao[Selection]):
    @staticmethod
    def selection_from_db(record: tuple[date, int], prize: LiteraryPrize) -> Selection:
        """Construit une selection du modèle d'après son entité en BD"""
        return Selection(record[0], prize, record[1])

    @override(Dao)
    async def read(self, id_entity: int) -> Optional[Selection]:
        """Renvoit la sélection correspondante à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        async with self.connection() as session:
            record = await session.scalar("""SELECT prize_id FROM LITERARY_PRIZE WHERE selection_id = :c""",
                                          {"c": id_entity})
            if record is None:
                return record
            prize = LiteraryPrizeDao.read(self.connection, id_entity=record)
            select = self.selection_from_db(await session.execute("""SELECT date_selection, selection_number FROM 
            SELECTION WHERE selection_id = :c""", {"c": id_entity}), prize)

            for book in await session.scalars("""SELECT book_id FROM VOTE WHERE selection_id = :c""",
                                                 {"c": id_entity}):
                books = BookDao.read(self.connection, id_entity=book)

                select.add_dict_character(books, await session.scalar("""SELECT 
                number_vote FROM VOTE WHERE book_id = :b AND selection_id = :c""", {"b": book, "c": id_entity}))

            return book

    @override(Dao)
    async def read_all(self) -> list[Selection]:
        """Renvoit l'ensemble des sélections de la BD."""
        book_list: list[Selection] = []
        async with self.connection() as session:
            for select in await session.scalars("""SELECT selection_id FROM SELECTION"""):
                book_list.append(self.read(select))
        return book_list
