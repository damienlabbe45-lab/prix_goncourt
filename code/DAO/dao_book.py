# -*- coding: utf-8 -*-

"""
Classe Dao[Book]
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional, override
from modeles.book import Book
from dao.dao import Dao
from dao.dao_author import AuthorDao
from modeles.author import Author
from dao.dao_character import CharacterDao


@dataclass
class BookDao(Dao[Book]):
    @staticmethod
    def book_from_db(record: tuple[str, str, int, float, str, str, date], author: Author) -> Book:
        """Construit un livre du modèle d'après son entité en BD"""
        return Book(record[0], record[1], record[2], record[3], record[4], record[5], record[6], author)

    @override
    async def read(self, id_entity: int) -> Optional[Book]:
        """Renvoit le livre correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        async with self.connection() as session:
            record = await session.scalar("""SELECT author_id FROM BOOK where book_id = :c""", {"c": id_entity})
            if record is None:
                return record
            author = AuthorDao.read(self.connection, id_entity=record)
            book = self.book_from_db(await session.execute("""SELECT title, editor, number_page, price, ISBN
            , summarize, release_book FROM BOOK WHERE book_id = :c""", {"c": id_entity}), author)
            for charact in await session.scalars("""SELECT character_id FROM CREATING where book_id = :c""",
                                                 {"c": id_entity}):
                book.add_list_character(CharacterDao.read(self.connection, charact))

            return book

    @override
    async def read_all(self) -> list[Book]:
        """Renvoit l'ensemble des livres de la BD."""
        book_list: list[Book] = []
        async with self.connection() as session:
            for author_id in await session.scalars("""SELECT author_id FROM BOOK where book_id"""):
                author = AuthorDao.read(self.connection, id_entity=author_id)
                book = self.book_from_db(await session.execute("""SELECT title, editor, number_page, price, ISBN
                            , summarize, release_book FROM BOOK WHERE author_id = :c """, {"c": author_id}), author)
                for charact in await session.scalars("""SELECT character_id FROM CREATING where book_id = (
                SELECT book_id FROM BOOK WHERE author_id = :c )""", {"c": author_id}):
                    book.add_list_character(CharacterDao.read(self.connection, charact))
                book_list.append(book)
        return book_list
