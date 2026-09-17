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
from modeles.literaryprize import LiteraryPrize


@dataclass
class SelectionDao(Dao[Selection]):
    @staticmethod
    def selection_from_db(record: tuple[date, int], prize: LiteraryPrize) -> Selection:
        """Construit une selection du modèle d'après son entité en BD"""
        return Selection(record[0], prize, record[1])

    @override
    async def read(self, id_entity: int) -> Optional[Selection]:
        """Renvoit la sélection correspondante à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        async with self.connection() as session:
            record = await session.scalar("""SELECT prize_id FROM LITERARY_PRIZE WHERE selection_id = :c""",
                                          {"c": id_entity})
            if record is None:
                return record
            prize = await LiteraryPrizeDao().read(id_entity=record)
            record = await session.execute_fetchone("""SELECT date_selection, selection_number FROM 
            SELECTION WHERE selection_id = :c""", {"c": id_entity})
            select = self.selection_from_db(record, prize)

            for book in await session.scalars("""SELECT book_id FROM VOTE WHERE selection_id = :c""",
                                              {"c": id_entity}):
                books = await BookDao().read(id_entity=book)

                select.add_dict_character(books, await session.scalar("""SELECT 
                number_vote FROM VOTE WHERE book_id = :b AND selection_id = :c""", {"b": book, "c": id_entity}))

            return select

    @override
    async def read_all(self) -> list[Selection]:
        """Renvoit l'ensemble des sélections de la BD."""
        book_list: list[Selection] = []
        async with self.connection() as session:
            for select in await session.scalars("""SELECT selection_id FROM SELECTION"""):
                book_list.append(self.read(select))
        return book_list

    async def insert_by_member(self, params: list[dict[str, str | int]], selection: int) -> None:
        async with self.connection() as session, await session.begin():
            await session.execute("""UPDATE VOTE SET number_vote = :v WHERE book_id = :b AND selection_id = :s""",
                                  params)
            if len(params) > 4:
                await session.execute("""INSERT INTO VOTE (book_id, selection_id, number_vote) 
                SELECT book_id , :s + 1, -23 FROM VOTE WHERE number_vote > 0 AND selection_id = :s""", {"s": selection})

    async def mapping_isbn_book_id(self, selection: int) -> dict[str, int]:
        async with self.connection() as session:
            return await session.mappings("""SELECT ISBN,VOTE.book_id FROM BOOK JOIN VOTE ON VOTE.book_id = BOOK.book_id 
            WHERE selection_id = :s""", {"s": selection})

    async def selection_id_prize(self, prize_name: str) -> int:
        async with self.connection() as session:
            return await session.scalar("""SELECT max(VOTE.selection_id) FROM VOTE JOIN LITERARY_PRIZE ON 
            VOTE.selection_id = LITERARY_PRIZE.selection_id WHERE prize_name = :pn""", {"pn": prize_name})
