from logging import Formatter
from typing import Self, override


class FormatDate(Formatter):
    """Formateur personnalisé pour utiliser la fonction date() pour l'horodatage."""

    @override(Formatter)
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
        log_filename = Path(__file__).resolve().parents[2] / 'log_goncourt.log'
        # Utilisation du Formateur
        custom_formetter = FormatDate(
            fmt='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
        root_logger = getLogger()
        # Vérifie si la configuration n'a pas déjà été faite
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
        if not root_logger.handlers:
            from logging import StreamHandler, FileHandler

            class UnbufferedStreamHandler(StreamHandler):
                """Handler console qui force l'affichage immédiat à chaque ligne."""

                @override(StreamHandler)
                def emit(self, record):
                    super().emit(record)
                    self.flush()

            class UnbufferedFileHandler(FileHandler):
                """Handler fichier qui force l'écriture sur le disque à chaque ligne."""

                @override(FileHandler)
                def emit(self, record):
                    super().emit(record)
                    self.flush()

# 1. Gestionnaire pour la console (StreamHandler)
            console_handler = UnbufferedStreamHandler(stdout)
            console_handler.setLevel(WARNING)
            console_handler.setFormatter(custom_formetter)
            # gestionnaire pour le fichier
            file_handler = UnbufferedFileHandler(
                log_filename, encoding='utf-8')
            file_handler.setLevel(WARNING)
            file_handler.setFormatter(custom_formetter)

            root_logger.setLevel(DEBUG)
            root_logger.addHandler(console_handler)
            root_logger.addHandler(file_handler)
