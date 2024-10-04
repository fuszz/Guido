import enum


class ZdwojonySkladnikFunkcji(enum.Enum):
    PRYMA = 0
    TERCJA = 3
    KWINTA = 5
    BRAK = -1  # przy D7 bez opuszczeń składników

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value
    