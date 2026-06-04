from pathlib import Path
from typing import Self

from ..generic_tracker import GenericTracker
from src.muscu_tracker.consts import Ex, Unit

class MuscuTracker(GenericTracker):
    def __init__(self, path: Path | str) -> None:
        super().__init__(path)


    def filter_unit(self, u: Unit):
        match u:
            case Unit.TONNAGE:
                return self.column("tonnage")
            case Unit.NB_REPS:
                return self.column("nb_reps")
            case Unit.NB_SERIE:
                return self.column("nb_series")
            case Unit.KG_PAR_REPS:
                return self._new_operator_column("tonnage", "nb_reps", "kg/reps")
            case Unit.TONNAGE_PAR_SERIE:
                return self._new_operator_column("tonnage", "nb_series", "kg/series")
            case Unit.NB_REPS_PAR_SERIE:
                return self._new_operator_column("nb_resp", "nb_reps", "nb_reps/series")
            case Unit.REPOS:
                return self.column("min_repos")
            case Unit.TONNAGE_PAR_REPOS:
                return self._new_operator_column("tonnage", "min_repos", "kg/min_repos")
            case Unit.NB_REPS_PAR_REPOS:
                return self._new_operator_column("nb_reps", "min_repos", "nb_reps/min_repos")
            
    def filter_ex(self, ex: Ex) -> Self:
        self.df = self.df[ self.df["exercice"] == ex.value ]
        return self