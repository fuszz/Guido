from enum import Enum, auto
import blad


class NazwyInterwalow(Enum):
    PRYMA_CZYSTA = auto(), "1"
    SEKUNDA_MALA = auto(), "2>"
    SEKUNDA_WIELKA = auto(), "2"
    TERCJA_MALA = auto(), "3>"
    TERCJA_WIELKA = auto(), "3"
    KWARTA_ZMNIEJSZONA = auto(), "4>"
    KWARTA_CZYSTA = auto(), "4"
    KWARTA_ZWIEKSZONA = auto(), "4<"
    KWINTA_ZMNIEJSZONA = auto(), "5>"
    KWINTA_CZYSTA = auto(), "5"
    KWINTA_ZWIEKSZONA = auto(), "5<"
    SEKSTA_MALA = auto(), "6>"
    SEKSTA_WIELKA = auto(), "6"
    SEPTYMA_ZMIEJSZONA = auto(), "7>"
    SEPTYMA_MALA = auto(), "7"
    SEPTYMA_WIELKA = auto(), "7<"

    @classmethod
    def interwal_z_symbolu(cls, symbol: str) -> 'NazwyInterwalow':
        for interwal in cls:
            if interwal.value[1] == symbol:
                return interwal
        raise blad.BladBrakTakiegoInterwalu("Niepoprawny symbol")

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value

    def __lt__(self, other):
        return type(self) is type(other) and self.value[0] < other.value[0]

    def __le__(self, other):
        return type(self) is type(other) and self.value[0] <= other.value[0]

    def __gt__(self, other):
        return type(self) is type(other) and self.value[0] > other.value[0]

    def __ge__(self, other):
        return type(self) is type(other) and self.value[0] >= other.value[0]

    def czy_interwal_zwiekszony(self) -> bool:
        """Zwraca True, jeśli dana instancja jest interwałem zwiększonym. W przeciwnym razie zwraca False"""
        if self.value[1] == '<' and self != NazwyInterwalow.SEPTYMA_WIELKA:
            return True
        else:
            return False
