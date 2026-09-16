from utils.utils import gather_exceptions, execute_insert
from datetime import date


async def insert_data() -> None:
    person_name = ["Yann", "Ace", "Corren", "Byleth", "Daraen", "Corrin", "Sephiroth", "Lucina", "Grima", "Lefantôme",
                   "Jaden"]
    person_last_name = ["Zerfhu", "Ropignon", "Casper", "Sothis", "Veilleur", "Vallah", "Angel", "Yllisse", "Medeus",
                        "Ebball", "Flamel"]
    jury = [10, 3, 4, 5, 6, 7]
    chairman = [True, False, False, False, False, False]
    selection_num = [1, 2, 3]
    selection_date = [date(2026, 9, 2), date(2026, 10, 6), date(2026, 10, 27)]
    prize = "Prix littéraire Goncourt"
    title = ["l'affaire Zerfhu", "Le jeune apprenti de Rubert Griffeacier", "Journal d'un Dovahjul",
             "Comment survivre en pleine nature", "le futur apocalypse", "le retour dans le passé", "les enfers",
             "les veilleurs de Sendarr", "Comment passer d'un tacticien au dieu dragon maléfique",
             "vie chez les Veilleurs de Ylisse en tant que tacticien amnésique", "Vie dans un futur apocalyptique",
             "L'académie de Seiros vu par l'un de ses enseignants", "La vie de la main du destin",
             "roleplay et proggrammation", "magie vs informatique", "un personnage est -il une vraie personne?",
             "Ma vie en tant que ancien roi et rebelle"]
    author = [1, 1, 2, 2, 11, 11, 11, 11, 9, 5, 8, 4, 6, 10, 10, 10, 3]
    editor = "l'oeil et la vie"
    number_page = [400, 120, 350, 100, 560, 245, 23, 34, 103, 56, 167, 980, 123, 78, 23, 80, 1567]
    price = 23.97
    date_release = date(2026, 9, 1)
    isbn = ["978-3-540-8915-6", "978-3-540-8915-9", "978-3-540-8917-6", "978-3-540-8015-6", "978-7-540-8915-6",
            "978-3-540-9915-6", "975-3-540-8915-6", "978-3-540-8910-6", "978-3-540-8905-6", "975-3-540-8910-6",
            "975-3-540-6910-6", "975-3-540-5910-6", "975-3-540-4910-6", "975-3-40-3910-6", "975-3-540-2910-6",
            "975-3-540-1910-6", "975-3-540-9910-6"]
    id_books = list(range(1, 17))
    await gather_exceptions(execute_insert("""INSERT INTO PERSON(person_name, person_lastname) 
                                                VALUES (:pn, :pl)""",
                                                       [{"pn": name, "pl": last_name}
                                                        for name, last_name in zip(person_name, person_last_name)
                                                        ]),

                                    execute_insert("""INSERT INTO SELECTION(selection_number, date_selection)
                                VALUES(:sn, :sd)""", [{"sn": num, "sd": dt}
                                                      for num, dt in zip(selection_num, selection_date)
                                                      ]))

    await gather_exceptions(execute_insert("""INSERT INTO AUTHOR (person_id) VALUES (:p)""",
                                                       [{"p": character} for character in range(1, 12)]),

                                    execute_insert("""INSERT INTO CHARACTER_BOOK (person_id) VALUES (:p)""",
                                                           [{"p": character} for character in range(1, 12)]),

                                    execute_insert("""INSERT INTO JURY_MEMBER (person_id, chairman) 
                                VALUES (:j, :c)""", [{"j": jur, "c": chairma} for jur, chairma in zip(jury, chairman)]),

                                    execute_insert("""INSERT INTO LITERARY_PRIZE(prize_name, selection_id)
                                VALUES(:pri,:sn )""", [{"sn": selection, "pri": prize} for selection in selection_num]))

    await gather_exceptions(execute_insert("""INSERT INTO TO_BE_MEMBER_OF(member_id, prize_id)
                                                VALUES (:j, 1)""", [{"j": jur} for jur in range(1, 7)]),

                                    execute_insert("""INSERT INTO BOOK(
                                title, editor, ISBN, price, number_page, release_book, author_id) 
                                VALUES(:t, :e, :i, :price, :n, :dr, :au)""",
                                                           [{"t": titl, "e": editor, "i": isb, "price": price,
                                                             "n": number_pag, "au": autho, "dr": date_release}
                                                            for titl, isb, number_pag, autho in
                                                            zip(title, isbn, number_page, author)]))

    await gather_exceptions(execute_insert("""INSERT INTO CREATING(book_id, character_id)
            VALUES(:b, :au)""", [{"b": id_book, "au": autho} for id_book, autho in zip(id_books, author)]),

                                   execute_insert("""INSERT INTO VOTE(book_id, selection_id, number_vote)
                                SELECT :b, 1, -23""", [{"b": id_book} for id_book in id_books]))
