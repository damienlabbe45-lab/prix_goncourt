from interface.visitor_interface import VisitorInterface
from dao.dao_selection import SelectionDao
from utils.utils import input_selection
from dao.dao_jurymember import JuryMemberDao
from re import search


class CharmanJuryInterface(VisitorInterface):
    async def selection_book_jury(self, select: int, id_book: list[int]) -> tuple[str, int]:
        read_selection_dao = await SelectionDao().read(select)
        counter = 0
        books = list(read_selection_dao.dic_book_vote.keys())
        for book in books:
            if book not in id_book:
                print(f"pour voter le livre {book} , taper {counter}")
            counter += 1
        response = input_selection(counter, id_book)
        return books[response], response

