import enum


class ZdwojonySkladnik(enum.Enum):
    """ Typ wyliczeniowy zwraca informację o tym, który składnik w akordzie jest zdwojony. """
    PRYMA = 0
    TERCJA = 1
    KWINTA = 2
    BRAK = 3
