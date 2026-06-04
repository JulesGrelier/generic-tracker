from pathlib import Path
import pandas as pd
from datetime import date, timedelta
from typing import Self


class GenericTracker():
    def __init__(self, path: Path | str) -> None:
        self.df: pd.DataFrame = pd.read_csv(path, index_col="date", parse_dates=True)


    def print_df(self) -> None:
        print(self.df)


    def return_df(self) -> pd.DataFrame:
        return self.df


    def day_d(self, d: date) -> Self:
        self.df = self.df[ self.df.index == str(d) ]
        return self
    

    def today(self) -> Self:
        self.df = self.df[ self.df.index == str(date.today()) ]
        return self


    def dates_between(self, date_from: date, date_to: date) -> Self:
        self.df = self.df[str(date_from) : str(date_to)]
        return self
    

    def dates_after(self, due_date: date) -> Self:
        self.df = self.df[ str(due_date) : str(due_date.today()) ]
        return self


    def n_days_ago(self, n: int) -> Self:
        target_date = date.today() - timedelta(days = n)
        return self.dates_after(target_date)


    def this_week(self) -> Self:
        today = date.today()
        last_monday = today - timedelta(days=today.isoweekday() - 1)
        return self.dates_after(last_monday)
    

    def this_month(self) -> Self:
        today = date.today()
        first_day_of_the_month = today - timedelta(days=today.day - 1)
        return self.dates_after(first_day_of_the_month)        


    def column(self, column: str) -> Self:
        self.df = pd.DataFrame(self.df[column])
        return self


    def _new_operator_column(self,
        column1: str,
        column2: str,
        title: str,
        join: bool = False,
        operator: str = "/"
    ) -> Self:
        if operator == "/":
            new_column: pd.Series = self.df[column1] / self.df[column2]
        else:
            new_column: pd.Series = self.df[column1] * self.df[column2]

        new_column.name = title

        if join:
            self.df = self.df.join(pd.DataFrame(new_column))
        else:
            self.df = pd.DataFrame(new_column)

        return self