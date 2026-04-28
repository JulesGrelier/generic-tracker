from my_df import MyDataFrame, datetime
from parser import Parser_CSV, Serie, Measure, Exercice

path = "./data.csv"
today = datetime.today()

df = MyDataFrame.new(path)

df.n_days_ago(5).view()