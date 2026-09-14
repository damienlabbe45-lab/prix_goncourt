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

    def loggingperso(self: Self):
        """Configure le logging pour afficher uniquement les erreurs dans la console et un fichier."""
        from logging import getLogger, DEBUG, WARNING
        import sys
        from sys import stdout
        from pathlib import Path
        stdout.reconfigure(line_buffering=True)  # type: ignore[union-attr]
        sys.stderr.reconfigure(line_buffering=True)  # type: ignore[union-attr]
        LOG_FILENAME = Path(__file__).resolve().parents[1] / 'log_bot.log'
        # Utilisation du Formateur
        CUSTOM_FORMETTER = FormatDate(
            fmt='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
        root_logger = getLogger()
        # Vérifie si la configuration n'a pas déjà été faite
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
        if not root_logger.handlers:
            from logging import StreamHandler, FileHandler