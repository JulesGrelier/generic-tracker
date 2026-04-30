from visualizer import Visualizer, datetime
from parser import Parser_CSV, Serie, Measure, Exercice

path = "./data.csv"
today = datetime.today()

df = Visualizer.new(path)

df.n_days_ago(5).view()