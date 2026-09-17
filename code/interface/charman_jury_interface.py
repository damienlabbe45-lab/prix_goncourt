from interface.visitor_interface import VisitorInterface
from dao.dao_selection import SelectionDao
from utils.utils import input_selection
from dao.dao_jurymember import JuryMemberDao
from re import search


class CharmanJuryInterface(VisitorInterface):
    """classe qu'on est censé accéder si on est connecté en tant que l'un des présidents des membres du jury
    comme il y a pas le temps, on supposera qu'on est déja connecté en temps que ça"""
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

    async def vote_book(self, select: int) -> None:
        book_selection = await self.selection_book(select)
        number = len(book_selection)
        counter = len(await JuryMemberDao().read_all())
        list_id_book = []
        params = []
        selection_dao = SelectionDao()
        isbn_id = await selection_dao.mapping_isbn_book_id(select)
        for _ in range(int(number/2)):
            results = await self.selection_book_jury(select, list_id_book)
            result = results[0]
            isbn = search(r"Son numéro isbc est: ([\d-]+)", result).group(1)
            params.append({"b": isbn_id[isbn], "v": input_selection(counter), "s": select})
            list_id_book.append(results[1])

        for i in range(number):
            if i not in list_id_book:
                isbn = search(r"Son numéro isbc est: ([\d-]+)", book_selection[i]).group(1)
                params.append({"b": isbn_id[isbn], "v": 0, "s": select})
        await selection_dao.insert_by_member(params, select)

    async def selection_charman(self, select_initial: int, select: int) -> None:
        await self.vote_book(select)
        if select + 2 == select_initial:
            await self.selection_charman(select_initial, select + 1)

    async def selection_charman_initial(self) -> None:
        selection_id = await SelectionDao().selection_id_prize("Prix littéraire Goncour")
        await self.selection_charman(selection_id, selection_id)
