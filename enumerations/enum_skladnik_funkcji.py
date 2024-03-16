import enum


class SkladnikFunkcji(enum.Enum):
    """ Typ wyliczeniowy, przechowuje informację o składniku akordu"""
    PRYMA = "1"
    TERCJA_WIELKA = "3"
    TERCJA_MALA = "3>"
    KWINTA = "5"
    SEPTYMA = "7"

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value

    def __hash__(self):
        return hash(self.name)