from enum import Enum

from datetime import datetime
import pandas as pd
from numpy import nan


class Exo(Enum):
    POMPE = "pompe"
    TRACTION_SUPINATION = "traction supination"
    TRACTION_PRONATION = "traction pronation"
    SQUAT = "squat"
    DIPS = "dips"

    


class Serie():
    def __init__(self, poids : float, nb_reps : int):
        self.poids = poids
        self.nb_reps = nb_reps


class Measure:

    @staticmethod
    def same_series(date : datetime, serie : Serie, nb_series : int, exercice : Exo) :
        total_nb_reps = serie.nb_reps * nb_series
        return Measure.as_df(date, serie.poids * total_nb_reps, total_nb_reps, nb_series, exercice)
    

    @staticmethod
    def different_series(date : datetime, series : list[Serie], exercice : Exo) :
        tonnage = 0
        nb_reps = 0
        nb_series = len(series)

        for serie in series:
            tonnage += serie.poids * serie.nb_reps
            nb_reps += serie.nb_reps

        return Measure.as_df(date, tonnage, nb_reps, nb_series, exercice)
    

    @staticmethod
    def as_df(date : datetime, tonnage : float, nb_reps : int, nb_series : int, exercice : Exo) -> pd.DataFrame :
        return pd.DataFrame({
            "date" : [date.__str__()],
            "tonnage" : [tonnage],
            "nb_reps" : [nb_reps],
            "nb_series" : [nb_series],
            "exercice" : [exercice.value]
        })


class MyMeasure():
    def as_df(self,
                exo : Exo,
                kg : float | tuple[float],
                nb_reps : float | tuple[float],
                nb_sets : float = 1,
                rest : float | tuple[float] = None,
                date : datetime = datetime.today()):
        pass


    @staticmethod
    def new(
            exo : Exo,
            kg : float | tuple[float],
            nb_reps : float | tuple[float],
            nb_sets : int = nan,
            rest : float | tuple[float] = nan,
            date : datetime = datetime.today()
            ) -> pd.DataFrame:
            
            for i in [kg, nb_reps, rest] :
                 if type(i) == tuple :
                        nb_sets = len(i)

            array = pd.DataFrame(index=range(nb_sets), columns=range(3))

            array.iloc[:,0]=kg
            array.iloc[:,1]=nb_reps
            array.iloc[:,2]=rest

            return pd.DataFrame({
                "date" : [date.__str__()],
                "tonnage" : [(array.iloc[:,0] * array.iloc[:,1]).sum()],
                "nb_reps" : [array.iloc[:,1].sum()],
                "nb_series" : [nb_sets],
                "exercice" : [exo.value]
            })


MyMeasure(Exo.TRACTION_SUPINATION, 74, (4,3,2), rest=(3,4,3))

MyMeasure(kg=74, nb_reps=(4, 3, 2), rest=(3, 4, 3), exo=Exo.TRACTION_SUPINATION)











class Parser_CSV:
    def __init__(self, path):
        self.df_clone = pd.read_csv(path)
        self.path = path


    def add_measure(self, measure : pd.DataFrame):
        self.df_clone = pd.concat([self.df_clone, measure])
        return self


    def clean_measures_pending(self):
        self.df_clone = pd.read_csv(self.path)


    def view_df_clone(self):
        print(self.df_clone)


    def send(self):
        text = self.df_clone.to_csv(index=False)

        with open(self.path, "w") as f:
            f.write(text)