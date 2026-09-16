# -*- coding: utf-8 -*-

"""
Classe book
"""

from dataclasses import dataclass, field
from typing import override
from datetime import date
from modeles.author import Author
from modeles.character import Character


@dataclass
class Book:
    """livre avec son auteur,
    ses persos principaux,
    son résumé,
    son titre,
    son éditeur,
    son ISBN,
    son prix,
    sa date de parution,
    son nombre de page"""

    title: str
    editor: str
    number_page: int
    price: float
    ISBN: str
    summarize: str
    release_book: date
    author_book: Author
    list_main_character: list[Character] = field(default_factory=list)

    @override
    def __str__(self) -> str:
        return f"""le livre {self.title} édité par l'édition {self.editor} écrit par {self.author_book} paru le 
{self.release_book}. Il a comme numéro ISBN: {self.ISBN} et fait {self.number_page} pages. Ses personnages principaux 
sont {"- \n".join(map(str, self.list_main_character))}. voici son résumé: \n {self.summarize}. son prix est de 
{self.price}"""

    def add_list_character(self, jury: Character) -> None:
        self.list_main_character.append(jury)

    def remove_list_character(self, jury: Character) -> None:
        self.list_main_character.remove(jury)
