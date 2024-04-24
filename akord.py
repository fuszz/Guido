from dzwiek import Dzwiek
from tonacja import Tonacja
import blad
from enumerations.enum_przewroty import Przewrot
from enumerations.enum_wartosci_nut import WartosciNut
from enumerations.enum_zdwojony_skladnik_funkcji import ZdwojonySkladnikFunkcji
from enumerations.enum_skladnik_funkcji import SkladnikFunkcji
from funkcja import Funkcja


class Akord:

    def __eq__(self, other):
        return (isinstance(self, type(other))
                and self._sopran == other.podaj_sopran()
                and self._alt == other.podaj_alt()
                and self._tenor == other.podaj_tenor()
                and self._bas == other.podaj_bas()
                and self._dlugosc == other.podaj_dlugosc())

    def __init__(self, nowy_sopran: Dzwiek, nowy_alt: Dzwiek, nowy_tenor: Dzwiek,
                 nowy_bas: Dzwiek, wartosc_akordu: WartosciNut):
        """
        Tworzy nową instancję klasy Akord. Podnosi blad.BladTworzeniaAkordu, jeśli podane niepoprawne
        typy argumentów. Nie sprawdza, czy dźwięki przystają do skal głosów.
        :param nowy_sopran: Dzwiek - dźwięk dla sopranu
        :param nowy_alt: Dzwiek - dźwięk dla altu
        :param nowy_tenor: Dzwiek - dźwięk dla tenoru
        :param nowy_bas: Dzwiek - dźwięk dla basu
        :param wartosc_akordu: WartosciNut - długość nut w akordzie.
        """

        if not (isinstance(nowy_bas, Dzwiek) and isinstance(nowy_tenor, Dzwiek)
                and isinstance(nowy_alt, Dzwiek) and isinstance(nowy_sopran, Dzwiek)
                and isinstance(wartosc_akordu, WartosciNut)):
            raise blad.BladTworzeniaAkordu("Sprawdź, czy tworzysz akord z poprawnych składników")

        self._dlugosc: WartosciNut = wartosc_akordu
        self._alt: Dzwiek = nowy_alt
        self._sopran: Dzwiek = nowy_sopran
        self._tenor: Dzwiek = nowy_tenor
        self._bas: Dzwiek = nowy_bas

    def podaj_dlugosc(self) -> WartosciNut:
        """
        Zwraca długość nut w akordzie.
        :return: WartosciNut
        """
        return self._dlugosc

    def podaj_sopran(self) -> Dzwiek:
        """
        Zwraca dźwięk sopranu
        :return: Dzwiek
        """
        return self._sopran

    def podaj_alt(self) -> Dzwiek:
        """
        Zwraca dźwięk altu
        :return: Dzwiek
        """
        return self._alt

    def podaj_tenor(self) -> Dzwiek:
        """
        Zwraca dźwięk tenoru
        :return: Dzwiek
        """
        return self._tenor

    def podaj_bas(self) -> Dzwiek:
        """
        Zwraca dźwięk basu
        :return: Dzwiek
        """
        return self._bas

    def podaj_liste_stopni_dzwiekow_akordu(self, badana_tonacja: Tonacja) -> list[int]:
        """
        Zwraca listę stopni dźwięków poszczególnych głosów względem danej tonacji w kolejności sopran, alt, tenor, bas.
        Nie usuwa duplikatów!
        Podnosi błąd BladDzwiekPozaTonacja, jeśli któryś z dźwięków nie leży w tonacji.
        Lepiej używać jej dopiero, gdy sprawdzimy, czy dźwięki są z tonacji.
        :param badana_tonacja: Tonacja
        :return: list[int]
        """
        lista_wynikowa = []
        for dzwiek in self.podaj_krotke_skladnikow():
            lista_wynikowa.append(dzwiek.podaj_stopien_w_tonacji(badana_tonacja))
        return lista_wynikowa

    def ustal_funkcje(self, badana_tonacja: Tonacja) -> Funkcja:
        """
        Zwraca instancję klasy enumeracyjnej Funkcja, jeśli z podanego akordu można w badanej tonacji utworzyć funkcją.
        W przeciwnym razie podnosi błąd BladStopienPoza

        :param badana_tonacja: Tonacja
        :return: Funkcja
        """
        return Funkcja.funkcja_z_listy_stopni(self.podaj_liste_stopni_dzwiekow_akordu(badana_tonacja),
                                              badana_tonacja.czy_dur())

    def ustal_przewrot(self, badana_tonacja: Tonacja) -> Przewrot:
        """
        Zwraca instancję klasy enumeracyjnej Przewrot, w zależności od basu i funkcji akordu w danej tonacji.
        Jeśli akord nie jest funkcją w badanej tonacji, podnosi błąd BladStopienPozaFunkcja
        :param badana_tonacja: Tonacja - wobec której ustalamy przewrót akordu
        :return: Przewrot
        """
        return self.ustal_funkcje(badana_tonacja).okresl_przewrot(self._bas.podaj_stopien_w_tonacji(badana_tonacja))

    def ustal_pozycje(self, badana_tonacja: Tonacja) -> SkladnikFunkcji:
        """
        Zwraca instancję klasy enumeracyjnej Przewrot, w zależności od basu i funkcji akordu w danej tonacji.
        Jeśli akord nie jest funkcją w badanej tonacji, podnosi błąd BladStopienPozaFunkcja
        :param badana_tonacja: Tonacja - wobec której ustalamy przewrót akordu
        :return: Przewrot
        """
        return self.ustal_funkcje(badana_tonacja).stopien_tonacji_w_skladnik(
            self._sopran.podaj_stopien_w_tonacji(badana_tonacja))

    def podaj_zdwojony_skladnik(self, badana_tonacja: Tonacja) -> (
            ZdwojonySkladnikFunkcji):
        """
            Jeśli akord nie stanowi w badanej tonacji funkcji - podnosi BladStopienPozaFukcja.
            Jeśli akord stanowi funkcję, ale nie ma dwojeń - zwraca '-1'.
            Jeśli akord to funkcja i  jest dwojenie - zwraca stopień dwojonego dźwięku jako int-a z przedziału [0, 6]
            :param badana_tonacja: tonacja, w której rozpatrujemy akord
            """
        funkcja_akordu = self.ustal_funkcje(badana_tonacja)

        if funkcja_akordu == Funkcja.DOMINANTA_SEPTYMOWA:
            return ZdwojonySkladnikFunkcji.BRAK
        for stopien in self.podaj_liste_stopni_dzwiekow_akordu(badana_tonacja):
            if self.podaj_liste_stopni_dzwiekow_akordu(badana_tonacja).count(stopien) == 2:
                return funkcja_akordu.podaj_dwojenie_jako_skladnik(stopien)

    def podaj_krotke_skladnikow(self) -> (Dzwiek, Dzwiek, Dzwiek, Dzwiek):
        """Zwraca dźwięki składowe akordu w postaci czteroelementowej krotki obiektów klasy Dźwięk w kolejności:
        (sopran, alt, tenor, bas)"""
        return self._sopran, self._alt, self._tenor, self._bas

    def podaj_krotke_kodow_midi_skladnikow(self) -> (int, int, int, int):
        """ Zwraca krotkę kodów midi składników akordu w kolejności SATB"""
        return (self._sopran.podaj_kod_midi(),
                self._alt.podaj_kod_midi(),
                self._tenor.podaj_kod_midi(),
                self._bas.podaj_kod_midi())

    def wyswietl_akord(self):
        """ FUNKCJA TESTOWA. DO WYWALENIA."""
        if self == "T":
            print("Koniec taktu")
        else:
            print(self._sopran.podaj_nazwe(), " ", self._sopran.podaj_oktawe(), '\t',
                  self._alt.podaj_nazwe(), " ", self._alt.podaj_oktawe(), '\t',
                  self._tenor.podaj_nazwe(), " ", self._tenor.podaj_oktawe(), '\t',
                  self._bas.podaj_nazwe(), " ", self._bas.podaj_oktawe(), '\t',
                  self._dlugosc.name)
