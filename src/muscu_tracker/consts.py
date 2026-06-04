from enum import Enum, auto

class Ex(Enum):
    POMPE = "pompe"
    TRACTION_SUPINATION = "traction supination"
    TRACTION_PRONATION = "traction pronation"
    SQUAT = "squat"
    DIPS = "dips"


class Unit(Enum):
    TONNAGE = auto()
    NB_REPS = auto()
    NB_SERIE = auto()
    KG_PAR_REPS = auto()
    TONNAGE_PAR_SERIE = auto()
    NB_REPS_PAR_SERIE = auto()
    REPOS = auto()
    TONNAGE_PAR_REPOS = auto()
    NB_REPS_PAR_REPOS = auto()