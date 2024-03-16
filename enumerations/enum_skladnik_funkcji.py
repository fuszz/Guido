import enum


class SkladnikFunkcji(enum.Enum):
    """ Typ wyliczeniowy, przechowuje informację o składniku akordu"""
    PRYMA = "1"
    TERCJA_WIELKA = "3"
    TERCJA_MAŁA = "3>"
    KWINTA = "5"
    SEPTYMA = "7"

