# from pathlib import Path
# from visualizer import Visualizer, datetime, Unit, new_visualizer
# from measure import Ex, measure_to_str, freeze_measure, poids_totale
# import matplotlib.pyplot as plt

# path = Path("data.csv")
# today = datetime.today()

# df = new_visualizer(path)

# df.filter_ex(Ex.POMPE).filter_unit(Unit.KG_PAR_REPS).print()

from pathlib import Path
from src.muscu_tracker.muscu_tracker import MuscuTracker
from src.muscu_tracker.consts import Unit, Ex



df = MuscuTracker(Path("data.csv"))
df.filter_unit(Unit.TONNAGE).print_df()