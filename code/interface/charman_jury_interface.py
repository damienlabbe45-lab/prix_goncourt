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

    async def vote_book(self, select: int):
        number = int(len(await self.selection_book(select)) / 2)
        counter = len(await JuryMemberDao().read_all())
        book = []
        vote = []
        list_id_book = []
        for _ in range(number):
            result = await self.selection_book_jury(select, list_id_book)
            book.append(result[0])
            list_id_book.append(result[1])
            vote.append(input_selection(counter))

        for _ in range(number):
            vote.append(0)

        params = []
        number = 0
        selection_dao = SelectionDao()
        isbn_id = await selection_dao.mapping_isbn_book_id(select)
        while len(params) < len(book):
            books = book[number]
            isbn = search(r"Son numéro isbc est: ([\d-]+)", books).group(1)
            params.append({"b": isbn_id[isbn], "v": vote[number], "s": select})
        await selection_dao.insert_by_member(params, select)
