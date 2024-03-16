import enum
from enumerations import enum_przewroty


class Funkcja(enum.Enum):
    """
    Typ wyliczeniowy przechowujący informację o dopuszczalnych w Guido funkcjach harmonicznych: tonice (moll tonice),
    subdominancie (moll subdominancie), dominancie, dominancie septymowej. Jeśli dźwięki nie stanowią żadnej z w/w
    funkcji, mamy błąd.
    """
    TONIKA = 'T'
    MOLL_TONIKA = 'mT'
    SUBDOMINANTA = 'S'
    MOLL_SUBDOMINANTA = 'mS'
    DOMINANTA = 'D'
    DOMINANTA_SEPTYMOWA = 'D7'
    BLAD = 'Błąd'

    def okresl_przewrot(self, stopien_basu: int) -> enum_przewroty.Przewrot:
        """
        Zwraca przewrót funkcji tonicznej w zależności od stopnia w basie.
        :param stopien_basu: int - stopien basu (już w danej tonacji)
        :return: enum_przewroty.Przewrot
        """

        if self in (Funkcja.TONIKA, Funkcja.MOLL_TONIKA):
            if stopien_basu == 0:
                return enum_przewroty.Przewrot.POSTAC_ZASADNICZA
            if stopien_basu == 2:
                return enum_przewroty.Przewrot.PIERWSZY
            if stopien_basu == 4:
                return enum_przewroty.Przewrot.PIERWSZY

        elif self in (Funkcja.SUBDOMINANTA, Funkcja.MOLL_SUBDOMINANTA):
            if stopien_basu == 3:
                return enum_przewroty.Przewrot.POSTAC_ZASADNICZA
            if stopien_basu == 5:
                return enum_przewroty.Przewrot.PIERWSZY
            if stopien_basu == 0:
                return enum_przewroty.Przewrot.PIERWSZY

        elif self in (Funkcja.DOMINANTA, Funkcja.DOMINANTA_SEPTYMOWA):
            if stopien_basu == 4:
                return enum_przewroty.Przewrot.POSTAC_ZASADNICZA
            if stopien_basu == 6:
                return enum_przewroty.Przewrot.PIERWSZY
            if stopien_basu == 1:
                return enum_przewroty.Przewrot.PIERWSZY
            if stopien_basu == 3:
                return enum_przewroty.Przewrot.TRZECI  # <- możliwe tylko w D7!
