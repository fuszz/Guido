import enum
import blad

from enumerations import enum_przewroty
from enumerations import enum_skladnik_funkcji
from enumerations import enum_zdwojony_skladnik_funkcji


class Funkcja(enum.Enum):
    """
    Typ wyliczeniowy przechowujący informację o dopuszczalnych w Guido funkcjach harmonicznych: tonice (moll tonice),
    subdominancie (moll subdominancie), dominancie, dominancie septymowej. Jeśli dźwięki nie stanowią żadnej z w/w
    funkcji, mamy błąd.

    UWAGA: Kolejność zapisu enumów jest ważna: akord mollowy musi być zawsze zapisany jako drugi,
    np. najpierw Tonika, potem Moll Tonika
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
        enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_MALA: 2,
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
        enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_MALA: 5,
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
        enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_MALA: 6,
        enum_skladnik_funkcji.SkladnikFunkcji.KWINTA: 1,
        enum_skladnik_funkcji.SkladnikFunkcji.SEPTYMA: 3,
        "tryb": "+"
    }

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value

    @classmethod
    def funkcja_z_listy_stopni(cls, stopnie: list[int], czy_dur: bool) -> 'Funkcja':
        """
        Tworzy instancję klasy Funkcja z 4-elementowej listy dźwięków akordu i informacji o trybie tonacji.
        :param stopnie: list[int]
        :param czy_dur: bool - True, jeśli tonacja durowa, False, kiedy tonacja mollowa.
        :return: Funkcja
        """

        if not ((all(isinstance(stopien, int) and stopien in range(0, 7) for stopien in stopnie)) and isinstance(
                czy_dur, bool)):
            raise blad.BladTworzeniaFunkcji("Niepoprawne parametry")

        mozliwe_funkcje = []
        for element in cls:
            stopnie_funkcji = list(filter(lambda x: isinstance(x, int), getattr(Funkcja, element.name).value.values()))
            if set(sorted(stopnie)) == set(sorted(stopnie_funkcji)):
                mozliwe_funkcje.append(element)
        if len(mozliwe_funkcje) == 1:
            return mozliwe_funkcje[0]
        elif len(mozliwe_funkcje) == 2:
            return mozliwe_funkcje[0] if czy_dur else mozliwe_funkcje[1]
        else:
            raise blad.BladStopienPozaFunkcja("Podane stopnie nie są funkcją")

    def czy_dur(self) -> bool:
        if self.value["tryb"] == "-":
            return False
        else:
            return True

    def stopien_tonacji_w_skladnik_funkcji(self, stopien: int) -> enum_skladnik_funkcji.SkladnikFunkcji:
        """
        Zwraca składnik funkcji (enum, SkladnikFunkcji), który odpowiada podanemu stopniu tonacji.
        Zwraca błąd BladStopienPozaFunkcja, jeśli podany stopień tonacji nie jest składnikiem podanej funkcji.
        Zwraca błąd BladNiepoprawneArgumenty, jeśli stopien nie ma dopuszczalnej wartości
        :param stopien: int, int [0, 6]
        :return: enum_skladnik_funkcji.SkladnikFunkcji
        """
        print(self.name)
        if not (isinstance(stopien, int)):
            raise blad.BladNiepoprawneArgumenty("funkcja.okresl_przewrot(): stopień musi być intem")
        if not (stopien in range(0, 7)):
            raise blad.BladNiepoprawneArgumenty("funkcja.okresl_przewrot(): stopień musi być w [0, 6]")
        for skladnik_funkcji in self.value.keys():
            if self.value[skladnik_funkcji] == stopien:
                return skladnik_funkcji
        raise blad.BladStopienPozaFunkcja(f"{stopien} nie należy do funkcji {self.value["symbol"]}")

    def okresl_przewrot(self, stopien_basu: int) -> enum_przewroty.Przewrot:
        """
        Zwraca przewrót funkcji tonicznej w zależności od stopnia w basie.
        Zwraca błąd BladStopienPozaFunkcja, jeśli podany stopień tonacji nie jest składnikiem podanej funkcji.
        Zwraca błąd BladNiepoprawneArgumenty, jeśli stopien nie ma dopuszczalnej wartości
        :param stopien_basu: int - stopien basu (już w danej tonacji)
        :return: enum_przewroty.Przewrot
        """
        skladnik: enum_skladnik_funkcji.SkladnikFunkcji = self.stopien_tonacji_w_skladnik_funkcji(stopien_basu)
        if skladnik == enum_skladnik_funkcji.SkladnikFunkcji.PRYMA:
            return enum_przewroty.Przewrot.POSTAC_ZASADNICZA
        elif skladnik in (enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_MALA,
                          enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_WIELKA):
            return enum_przewroty.Przewrot.PIERWSZY
        elif skladnik == enum_skladnik_funkcji.SkladnikFunkcji.KWINTA:
            return enum_przewroty.Przewrot.DRUGI
        elif skladnik == enum_skladnik_funkcji.SkladnikFunkcji.SEPTYMA:
            return enum_przewroty.Przewrot.TRZECI

    def dwojenie_jako_skladnik_funkcji(self, stopien: int) -> enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji:
        """
        Zwraca w postaci ZdwojonySkladnikFunkcji info o zdwojonym w akordzie składniku funkcji
        :param stopien: int z [0, 6]- stopień, który występuje w akordzie dwukrotnie. W przypadku D7 nie ma znaczenia.
        :return: enum - ZdwojonySkladnikFunkcji
        """
        if self == Funkcja.DOMINANTA_SEPTYMOWA:
            return enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.BRAK

        skladnik = self.stopien_tonacji_w_skladnik_funkcji(stopien)

        if skladnik == enum_skladnik_funkcji.SkladnikFunkcji.PRYMA:
            return enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.PRYMA
        elif skladnik in (enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_WIELKA,
                          enum_skladnik_funkcji.SkladnikFunkcji.TERCJA_MALA):
            return enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.TERCJA
        elif skladnik == enum_skladnik_funkcji.SkladnikFunkcji.KWINTA:
            return enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.KWINTA
