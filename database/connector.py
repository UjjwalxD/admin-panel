import sqlite3 
import logging
from colorama import Fore, Style

class ColoredFormatter(logging.Formatter):
    grey = Fore.LIGHTBLACK_EX + Style.BRIGHT
    green = Fore.LIGHTGREEN_EX + Style.BRIGHT
    yellow = Fore.LIGHTYELLOW_EX + Style.BRIGHT
    red = Fore.LIGHTRED_EX + Style.BRIGHT
    bold_red = Fore.RED + Style.BRIGHT
    reset = Style.RESET_ALL

    FORMATS = {
        logging.DEBUG: grey + "%(asctime)s %(name)s %(levelname)s %(message)s" + reset,
        logging.INFO: green + "%(asctime)s %(name)s %(levelname)s %(message)s" + reset,
        logging.WARNING: yellow + "%(asctime)s %(name)s %(levelname)s %(message)s" + reset,
        logging.ERROR: red + "%(asctime)s %(name)s %(levelname)s %(message)s" + reset,
        logging.CRITICAL: bold_red + "%(asctime)s %(name)s %(levelname)s %(message)s" + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(ColoredFormatter())
logger.addHandler(ch)

class connect:
    @staticmethod
    def database():
        conn = sqlite3.connect('database/database.db')
        logger.debug('Database Connected.')
        return conn
        