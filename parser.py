from enum import Enum

from datetime import datetime
import pandas as pd



class Exercice(Enum):
    POMPE = "pompe"
    TRACTION_SUPINATION = "traction supination"
    SQUAT = "squat"


class Serie():
    def __init__(self, poids : float, nb_reps : int):
        self.poids = poids
        self.nb_reps = nb_reps


class Measure:

    @staticmethod
    def same_series(date : datetime, serie : Serie, nb_series : int, exercice : Exercice) :
        total_nb_reps = serie.nb_reps * nb_series
        return Measure.as_df(date, serie.poids * total_nb_reps, total_nb_reps, nb_series, exercice)
    

    @staticmethod
    def different_series(date : datetime, series : list[Serie], exercice : Exercice) :
        tonnage = 0
        nb_reps = 0
        nb_series = len(series)

        for serie in series:
            tonnage += serie.poids * serie.nb_reps
            nb_reps += serie.nb_reps

        return Measure.as_df(date, tonnage, nb_reps, nb_series, exercice)
    

    @staticmethod
    def as_df(date : datetime, tonnage : float, nb_reps : int, nb_series : int, exercice : Exercice) -> pd.DataFrame :
        return pd.DataFrame({
            "date" : [date.__str__()],
            "tonnage" : [tonnage],
            "nb_reps" : [nb_reps],
            "nb_series" : [nb_series],
            "exercice" : [exercice.value]
        })





class Parser_CSV:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.df_clone = pd.read_csv(path)
        self.path = path


    def add_measure(self, measure : pd.DataFrame):
        self.df_clone = pd.concat([self.df_clone, measure])
        return self


    def clean_measures_pending(self):
        self.df_clone = self.df


    def view_df_clone(self):
        print(self.df_clone)


    def send(self):
        text = self.df_clone.to_csv(index=False)

        with open(self.path, "w") as f:
            f.write(text)