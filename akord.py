import dzwiek
import tonacja
import blad
from enumerations import enum_przewroty, enum_wartosci_nut, enum_zdwojony_skladnik_funkcji
import funkcja


class Akord:

    def __eq__(self, other):
        return (type(self) is type(other) and self._sopran == other._sopran
                and self._alt == other._alt
                and self._tenor == other._tenor
                and self._bas == other._bas
                and self._dlugosc == other._dlugosc)

    def __init__(self, nowy_sopran: dzwiek.Dzwiek, nowy_alt: dzwiek.Dzwiek, nowy_tenor: dzwiek.Dzwiek,
                 nowy_bas: dzwiek.Dzwiek, wartosc_akordu: enum_wartosci_nut.WartosciNut):
        """
        Tworzy nową instancję klasy Akord. Podnosi blad.BladTworzeniaAkordu, jeśli podane niepoprawne
        typy argumentów. Nie sprawdza, czy dźwięki przystają do skal głosów.
        :param nowy_sopran: dzwiek.Dzwiek - dźwięk dla sopranu
        :param nowy_alt: dzwiek.Dzwiek - dźwięk dla altu
        :param nowy_tenor: dzwiek.Dzwiek - dźwięk dla tenoru
        :param nowy_bas: dzwiek.Dzwiek - dźwięk dla basu
        :param wartosc_akordu: enum_wartosci_nut.WartosciNut - długość nut w akordzie.
        """

        if not (isinstance(nowy_bas, dzwiek.Dzwiek) and isinstance(nowy_tenor, dzwiek.Dzwiek)
                and isinstance(nowy_alt, dzwiek.Dzwiek) and isinstance(nowy_sopran, dzwiek.Dzwiek)
                and isinstance(wartosc_akordu, enum_wartosci_nut.WartosciNut)):
            raise blad.BladTworzeniaAkordu("Sprawdź, czy tworzysz akord z poprawnych składników")

        self._dlugosc: enum_wartosci_nut.WartosciNut = wartosc_akordu
        self._alt: dzwiek.Dzwiek = nowy_alt
        self._sopran: dzwiek.Dzwiek = nowy_sopran
        self._tenor: dzwiek.Dzwiek = nowy_tenor
        self._bas: dzwiek.Dzwiek = nowy_bas

    def podaj_dlugosc(self) -> enum_wartosci_nut.WartosciNut:
        """
        Zwraca długość nut w akordzie.
        :return: enum_wartosci_nut.WartosciNut
        """
        return self._dlugosc

    def podaj_sopran(self) -> dzwiek.Dzwiek:
        """
        Zwraca dźwięk sopranu
        :return: dzwiek.Dzwiek
        """
        return self._sopran

    def podaj_alt(self) -> dzwiek.Dzwiek:
        """
        Zwraca dźwięk altu
        :return: dzwiek.Dzwiek
        """
        return self._alt

    def podaj_tenor(self) -> dzwiek.Dzwiek:
        """
        Zwraca dźwięk tenoru
        :return: dzwiek.Dzwiek
        """
        return self._tenor

    def podaj_bas(self) -> dzwiek.Dzwiek:
        """
        Zwraca dźwięk basu
        :return: dzwiek.Dzwiek
        """
        return self._bas

    def czy_dzwieki_w_tonacji(self, badana_tonacja: tonacja.Tonacja) -> bool:
        """
        Zwraca True, jeśli wszystkie dźwięki akordu znajdują się w tonacji. W przeciwnym razie zwraca False.
        :param badana_tonacja: tonacja.Tonacja
        :return: bool
        """
        try:
            stopien_sopranu: int = self._sopran.podaj_swoj_stopien(badana_tonacja)
            stopien_altu: int = self._alt.podaj_swoj_stopien(badana_tonacja)
            stopien_tenoru: int = self._tenor.podaj_swoj_stopien(badana_tonacja)
            stopien_basu: int = self._bas.podaj_swoj_stopien(badana_tonacja)
        except blad.BladDzwiekPozaTonacja:
            return False
        return True

    def podaj_liste_stopni_dzwiekow_akordu(self, badana_tonacja: tonacja.Tonacja) -> list[int]:
        """
        Zwraca listę stopni dźwięków poszczególnych głosów względem danej tonacji w kolejności sopran, alt, tenor, bas.
        Nie usuwa duplikatów!
        Podnosi błąd BladDzwiekPozaTonacja, jeśli któryś z dźwięków nie leży w tonacji.
        Lepiej używać jej dopiero, gdy sprawdzimy, czy dźwięki są z tonacji.
        :param badana_tonacja: tonacja.Tonacja
        :return: list[int]
        """
        if not self.czy_dzwieki_w_tonacji(badana_tonacja):
            raise blad.BladDzwiekPozaTonacja

        return [
            self._sopran.podaj_swoj_stopien(badana_tonacja),
            self._alt.podaj_swoj_stopien(badana_tonacja),
            self._tenor.podaj_swoj_stopien(badana_tonacja),
            self._bas.podaj_swoj_stopien(badana_tonacja)
        ]

    def ustal_funkcje(self, badana_tonacja: tonacja.Tonacja) -> funkcja.Funkcja:
        """
        Zwraca instancję klasy enumeracyjnej Funkcja, jeśli z podanego akordu można w badanej tonacji utworzyć funkcją.
        W przeciwnym razie podnosi błąd BladStopienPozaFunkcja.

        :param badana_tonacja: tonacja.Tonacja
        :return: funkcja.Funkcja
        """
        return funkcja.Funkcja.funkcja_z_listy_stopni(self.podaj_liste_stopni_dzwiekow_akordu(badana_tonacja),
                                                      badana_tonacja.czy_dur())

    def ustal_przewrot(self, badana_tonacja: tonacja.Tonacja) -> enum_przewroty.Przewrot:
        """
        Zwraca instancję klasy enumeracyjnej Przewrot, w zależności od basu i funkcji akordu w danej tonacji.
        Jeśli akord nie jest funkcją w badanej tonacji, podnosi błąd BladStopienPozaFunkcja
        :param badana_tonacja: tonacja.Tonacja - wobec której ustalamy przewrót akordu
        :return: enum_przewroty.Przewrot
        """
        return self.ustal_funkcje(badana_tonacja).okresl_przewrot(self._bas.podaj_swoj_stopien(badana_tonacja))

    def ustal_pozycje(self, badana_tonacja: tonacja.Tonacja) -> enum_przewroty.Przewrot:
        """
        Zwraca instancję klasy enumeracyjnej Przewrot, w zależności od basu i funkcji akordu w danej tonacji.
        Jeśli akord nie jest funkcją w badanej tonacji, podnosi błąd BladStopienPozaFunkcja
        :param badana_tonacja: tonacja.Tonacja - wobec której ustalamy przewrót akordu
        :return: enum_przewroty.Przewrot
        """
        return self.ustal_funkcje(badana_tonacja).okresl_przewrot(self._sopran.podaj_swoj_stopien(badana_tonacja))

    def ustal_zdwojony_stopien_tonacji(self, badana_tonacja: tonacja.Tonacja) -> int:
        """
        Jeśli akord nie stanowi w badanej tonacji funkcji - podnosi BladStopienPozaFukcja.
        Jeśli akord stanowi funkcję, ale nie ma dwojeń - zwraca '-1'.
        Jeśli akord stanowi funkcję i  jest dwojenie - zwraca stopień dwojonego dźwięku jako int-a z przedziału [0, 6]

        :param badana_tonacja: tonacja, w której rozpatrujemy akord
        :return: int - stopień zdwojonego dźwięku [0, 6] lub '-1', jeśli nie ma dwojeń
        """
        self.ustal_funkcje(badana_tonacja)
        lista_stopni = self.podaj_liste_stopni_dzwiekow_akordu(badana_tonacja)
        dublowane = [stopien for stopien in lista_stopni if lista_stopni.count(stopien) > 1
                     and stopien not in lista_stopni]
        if len(dublowane) == 0:
            return -1
        elif len(dublowane) == 1:
            return dublowane[0]
        else:
            raise ValueError(
                "COŚ DZIWNEGO W akord.ustal_jaki_stopien_zdwojony() !!!")  # Komunikat testowy - upewnić się, że nigdy nie wystąpi i wywalić.

    def ustal_zdwojony_skladnik_funkcji(self, badana_tonacja: tonacja.Tonacja) -> (
            enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji):
        zdwojony_stopien: int = self.ustal_zdwojony_stopien_tonacji(badana_tonacja)
        return self.ustal_funkcje(badana_tonacja).dwojenie_jako_skladnik_funkcji(zdwojony_stopien)

    def wyswietl_akord(self):
        """ FUNKCJA TESTOWA. DO WYWALENIA."""
        print(self._sopran.podaj_swoj_kod_bezwzgledny(), self._alt.podaj_swoj_kod_bezwzgledny(),
              self._tenor.podaj_swoj_kod_bezwzgledny(), self._bas.podaj_swoj_kod_bezwzgledny(), self._dlugosc.value)
