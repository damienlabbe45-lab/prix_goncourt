from logging import Formatter
from typing import Self


class FormatDate(Formatter):
    """Formateur personnalisé pour utiliser la fonction date() pour l'horodatage."""