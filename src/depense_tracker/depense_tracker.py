from pathlib import Path
from datetime import date, timedelta, datetime
from ..generic_tracker import GenericTracker
from enum import Enum
from typing import Self


class Recurrences(Enum):
    JOUR = ("prix/jour", 1)
    SEMAINE = ("prix/sem.", 7)
    MOIS = ("prix/mois", 30)
    ANNEE = ("prix/an", 365)

def str_to_date(text: str) -> date:
    return datetime.strptime(text, "%Y-%m-%d")

def nb_days_since_today(current_date: date) -> int:
    delta: timedelta = date.today() - current_date
    return delta.days

class DepenseTracker(GenericTracker):
    def __init__(self, path: Path | str) -> None:
        super().__init__(path)