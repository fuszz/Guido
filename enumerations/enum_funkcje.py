import enum
from enumerations import enum_przewroty
from enumerations import enum_skladnik_funkcji
from enumerations import enum_bledy


class Funkcja(enum.Enum):
    """
    Typ wyliczeniowy przechowujący informację o dopuszczalnych w Guido funkcjach harmonicznych: tonice (moll tonice),
    subdominancie (moll subdominancie), dominancie, dominancie septymowej. Jeśli dźwięki nie stanowią żadnej z w/w
    funkcji, mamy błąd.
    """
    TONIKA = {
        "symbol": "T",
        enum_skladnik_funkcji.SkladnikFunkcji.PRYMA: 0,
        enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_WIELKA: 2,
        enum_skladnik_funkcji.SkladnikFunkcji.KWINTA: 4,
        "tryb": "+"
    }
    MOLL_TONIKA = {
        "symbol": "mT",
        enum_skladnik_funkcji.SkladnikFunkcji.PRYMA: 0,
        enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_MAŁA: 2,
        enum_skladnik_funkcji.SkladnikFunkcji.KWINTA: 4,
        "tryb": "-"
    }
    SUBDOMINANTA = {
        "symbol": "S",
        enum_skladnik_funkcji.SkladnikFunkcji.PRYMA: 3,
        enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_WIELKA: 5,
        enum_skladnik_funkcji.SkladnikFunkcji.KWINTA: 0,
        "tryb": "+"
    }
    MOLL_SUBDOMINANTA = {
        "symbol": "mS",
        enum_skladnik_funkcji.SkladnikFunkcji.PRYMA: 3,
        enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_MAŁA: 5,
        enum_skladnik_funkcji.SkladnikFunkcji.KWINTA: 0,
        "tryb": "-"
    }
    DOMINANTA = {
        "symbol": "D",
        enum_skladnik_funkcji.SkladnikFunkcji.PRYMA: 4,
        enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_WIELKA: 6,
        enum_skladnik_funkcji.SkladnikFunkcji.KWINTA: 1,
        "tryb": "+"
    }
    DOMINANTA_SEPTYMOWA = {
        "symbol": "D7",
        enum_skladnik_funkcji.SkladnikFunkcji.PRYMA: 4,
        enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_MAŁA: 6,
        enum_skladnik_funkcji.SkladnikFunkcji.KWINTA: 1,
        enum_skladnik_funkcji.SkladnikFunkcji.SEPTYMA: 3,
        "tryb": "+"
    }

    @classmethod
    def funkcja_z_listy_stopni(cls, stopnie: list[int]) -> 'Funkcja':
        """
        Tworzy instancję klasy Funkcja z 4-elementowej listy dźwięków akordu.
        :param stopnie: list[int]
        :return: Funkcja
        """
        for element in cls.__members__:
            stopnie_funkcji = list(filter(lambda x: isinstance(x, int), getattr(Funkcja, element).value.values()))
            if set(sorted(stopnie)) == set(sorted(stopnie_funkcji)):
                return cls.__init__(element)
        raise enum_bledy.BladStopienPozaFunkcja(f"{stopnie} nie tworzą żadnej funkcji spośród {cls.__members__.keys()}")

    def czy_dur(self) -> bool:
        if self["tryb"] == "-":
            return False
        else:
            return True

    def okresl_przewrot(self, stopien_basu: int) -> enum_przewroty.Przewrot:
        """
        Zwraca przewrót funkcji tonicznej w zależności od stopnia w basie.
        :param stopien_basu: int - stopien basu (już w danej tonacji)
        :return: enum_przewroty.Przewrot
        """
        skladnik: enum_skladnik_funkcji.SkladnikFunkcji = self.stopien_tonacji_w_skladnik_funkcji(stopien_basu)
        if skladnik == enum_skladnik_funkcji.SkladnikFunkcji.PRYMA:
            return enum_przewroty.Przewrot.POSTAC_ZASADNICZA
        elif skladnik in (enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_MAŁA,
                          enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_WIELKA):
            return enum_przewroty.Przewrot.PIERWSZY
        elif skladnik == enum_skladnik_funkcji.SkladnikFunkcji.KWINTA:
            return enum_przewroty.Przewrot.DRUGI
        elif skladnik == enum_skladnik_funkcji.SkladnikFunkcji.SEPTYMA:
            return enum_przewroty.Przewrot.TRZECI

    def stopien_tonacji_w_skladnik_funkcji(self, stopien: int) -> enum_skladnik_funkcji.SkladnikFunkcji:
        for skladnik_funkcji, stopien_tonacji in self.value:
            if stopien_tonacji == stopien:
                return skladnik_funkcji
        raise enum_bledy.BladStopienPozaFunkcja(f"{stopien} nie należy do funkcji {self.value["symbol"]}")
