from dao.dao_selection import SelectionDao


class VisitorInterface:
    async def selection_book(self, select: int):
        read_selection_dao = await SelectionDao().read(select)
        return list(read_selection_dao.dic_book_vote.keys())
