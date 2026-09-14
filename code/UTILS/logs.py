from logging import Formatter
from typing import Self


class FormatDate(Formatter):
    """Formateur personnalisé pour utiliser la fonction date() pour l'horodatage."""

    def formatTime(self: Self, record, datefmt=None):
        """
        Retourne la chaîne de date/heure personnalisée.
        """
        from datetime import datetime
        maintenant = datetime.now()
        return maintenant.strftime("%d %B %Y à %H heure %M minutes %S secondes %f microsecondes").replace(
            m := maintenant.strftime("%B"),
            {'January': 'janvier', 'February': 'février', 'March': 'mars', 'April': 'avril', 'May': 'mai',
             'June': 'juin',
             'July': 'juillet', 'August': 'août', 'September': 'septembre', 'October': 'octobre',
             'November': 'novembre', 'December': 'décembre'}[m])

class LogErreur(object):
    """Mixin pour initialiser le système de logging (uniquement les erreurs)."""