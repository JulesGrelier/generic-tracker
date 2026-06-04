from dataclasses import dataclass
from datetime import date
from pathlib import Path

@dataclass
class Depense:
    price: float
    buying_date: date

    def __str__(self) -> str:
        return f"{self.buying_date},{self.price}"

def freeze_depense(depense: Depense, path_file: Path) -> None:
    with open(path_file, mode="a") as f:
        f.write(f"\n{str(depense)}")
        print(f"Nouvelle dépense enregistrée en dur dans le fichier {path_file}")