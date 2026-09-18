from dao.dao_selection import SelectionDao
from dao.dao_book import BookDao
from dao.dao_jurymember import JuryMemberDao
from dao.dao_literary_prize import LiteraryPrizeDao
from dao.dao_author import AuthorDao
from dao.dao_character import CharacterDao


class VisitorInterface:
    async def read_selections(self) -> None:
        for selection in await SelectionDao().read_all():
            print(f"{selection} \n")

    async def read_books(self) -> None:
        for book in await BookDao().read_all():
            print(f"{book} \n")

    async def read_jury_members(self) -> None:
        for jury_member in await JuryMemberDao().read_all():
            print(f"{jury_member} \n")

    async def read_literary_prize(self) -> None:
        for literary_prize in await LiteraryPrizeDao().read_all():
            print(f"{literary_prize} \n")

    async def read_authors(self) -> None:
        for author in await AuthorDao().read_all():
            print(f"{author} \n")

    async def read_characters(self) -> None:
        for character in await CharacterDao().read_all():
            print(f"{character} \n")


