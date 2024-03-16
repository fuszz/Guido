import dzwiek
import tonacja
from enumerations import enum_funkcje, enum_przewroty, enum_wartosci_nut, enum_zdwojony_skladnik, enum_bledy


class Akord:
    def __init__(self, nowy_sopran: dzwiek.Dzwiek, nowy_alt: dzwiek.Dzwiek, nowy_tenor: dzwiek.Dzwiek,
                 nowy_bas: dzwiek.Dzwiek, wartosc_akordu: enum_wartosci_nut.WartosciNut):
        """
        Tworzy nową instancję klasy Akord. Podnosi enum_bledy.BladTworzeniaAkordu, jeśli podane niepoprawne
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
            raise enum_bledy.BladTworzeniaAkordu("Sprawdź, czy tworzysz akord z poprawnych składników")

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
        except enum_bledy.BladDzwiekPozaTonacja:
            return False
        return True

    def podaj_liste_stopni_dzwiekow(self, badana_tonacja: tonacja.Tonacja) -> list[int]:
        """
        Zwraca listę stopni dźwięków poszczególnych głosów względem danej tonacji w kolejności sopran, alt, tenor, bas.
        Podnosi błąd BladDzwiekPozaTonacja, jeśli któryś z dźwięków nie leży w tonacji.
        Lepiej używać jej dopiero, gdy sprawdzimy, czy dźwięki są z tonacji.
        :param badana_tonacja: tonacja.Tonacja
        :return: list[int]
        """
        if not self.czy_dzwieki_w_tonacji(badana_tonacja):
            raise enum_bledy.BladDzwiekPozaTonacja

        return [
            self._sopran.podaj_swoj_stopien(badana_tonacja),
            self._alt.podaj_swoj_stopien(badana_tonacja),
            self._tenor.podaj_swoj_stopien(badana_tonacja),
            self._bas.podaj_swoj_stopien(badana_tonacja)
        ]

    def ustal_funkcje(self, badana_tonacja: tonacja.Tonacja) -> enum_funkcje.Funkcja:
        """
        Ustala funkcję akordu względem badanej tonacji. Zwraca enum_funkcje.Funkcja.BLAD, jeśli nie wszystkie dźwięki
        akordu są w tonacji lub kiedy akord nie tworzy sensownej funkcji z triady w tonacji.
        :param badana_tonacja: tonacja.Tonacja
        :return: enum_funkcje.Funkcja
        """

        if not self.czy_dzwieki_w_tonacji(badana_tonacja):
            return enum_funkcje.Funkcja.BLAD

        tonacja_durowa: bool = badana_tonacja.czy_dur()
        lista_stopni = sorted(set(self.podaj_liste_stopni_dzwiekow(badana_tonacja)))

        if lista_stopni == [0, 2, 4]:
            return enum_funkcje.Funkcja.TONIKA if tonacja_durowa else enum_funkcje.Funkcja.MOLL_TONIKA

        elif lista_stopni == [0, 3, 5]:
            return enum_funkcje.Funkcja.SUBDOMINANTA if tonacja_durowa else enum_funkcje.Funkcja.MOLL_SUBDOMINANTA

        elif lista_stopni == [1, 4, 6]:
            return enum_funkcje.Funkcja.DOMINANTA

        elif lista_stopni == [1, 3, 4, 6]:
            return enum_funkcje.Funkcja.DOMINANTA_SEPTYMOWA

        else:
            return enum_funkcje.Funkcja.BLAD

    def ustal_przewrot(self, badana_tonacja: tonacja.Tonacja) -> enum_przewroty.Przewrot:

        funkcja: enum_funkcje.Funkcja = self.ustal_funkcje(badana_tonacja)
        if funkcja == enum_funkcje.Funkcja.BLAD:
            return enum_przewroty.Przewrot.NIE_ZDEFINIOWANO

        stopien_basu: int = self._bas.podaj_swoj_stopien(badana_tonacja)

        return funkcja.okresl_przewrot(stopien_basu)

    def ustal_dwojenie(self, badana_tonacja: tonacja.Tonacja) -> enum_zdwojony_skladnik.ZdwojonySkladnik:

        funkcja_akordu = self.ustal_funkcje(badana_tonacja)
        if funkcja_akordu == enum_funkcje.Funkcja.DOMINANTA_SEPTYMOWA:
            return enum_zdwojony_skladnik.ZdwojonySkladnik.BRAK
        try:
            stopien_sopranu: int = self._sopran.podaj_swoj_stopien(badana_tonacja)
            stopien_altu: int = self._alt.podaj_swoj_stopien(badana_tonacja)
            stopien_tenoru: int = self._tenor.podaj_swoj_stopien(badana_tonacja)
            stopien_basu: int = self._bas.podaj_swoj_stopien(badana_tonacja)
        except enum_bledy.BladDzwiekPozaTonacja:
            return enum_zdwojony_skladnik.ZdwojonySkladnik.BRAK

        lista_stopni = [stopien_sopranu, stopien_altu, stopien_tenoru, stopien_basu]
        lista_stopni = sorted(lista_stopni)
        zmienna_pomocnicza = lista_stopni[0]
        zdwojony_stopien_tonacji = None
        for i in lista_stopni[1:]:
            if i == zmienna_pomocnicza:
                zdwojony_stopien_tonacji = i
                break
            else:
                zmienna_pomocnicza = i

        if zdwojony_stopien_tonacji is None:
            return enum_zdwojony_skladnik.ZdwojonySkladnik.BRAK

        if funkcja_akordu == enum_funkcje.Funkcja.TONIKA or funkcja_akordu == enum_funkcje.Funkcja.MOLL_TONIKA:
            if zdwojony_stopien_tonacji == 0:
                return enum_zdwojony_skladnik.ZdwojonySkladnik.PRYMA
            elif zdwojony_stopien_tonacji == 2:
                return enum_zdwojony_skladnik.ZdwojonySkladnik.TERCJA
            elif zdwojony_stopien_tonacji == 4:
                return enum_zdwojony_skladnik.ZdwojonySkladnik.KWINTA

        elif funkcja_akordu == enum_funkcje.Funkcja.SUBDOMINANTA or funkcja_akordu == enum_funkcje.Funkcja.MOLL_SUBDOMINANTA:
            if zdwojony_stopien_tonacji == 3:
                return enum_zdwojony_skladnik.ZdwojonySkladnik.PRYMA
            elif zdwojony_stopien_tonacji == 5:
                return enum_zdwojony_skladnik.ZdwojonySkladnik.TERCJA
            elif zdwojony_stopien_tonacji == 0:
                return enum_zdwojony_skladnik.ZdwojonySkladnik.KWINTA

        elif funkcja_akordu == enum_funkcje.Funkcja.DOMINANTA:
            if zdwojony_stopien_tonacji == 4:
                return enum_zdwojony_skladnik.ZdwojonySkladnik.PRYMA
            elif zdwojony_stopien_tonacji == 6:
                return enum_zdwojony_skladnik.ZdwojonySkladnik.TERCJA
            elif zdwojony_stopien_tonacji == 1:
                return enum_zdwojony_skladnik.ZdwojonySkladnik.KWINTA
        else:
            return enum_zdwojony_skladnik.ZdwojonySkladnik.BRAK

    def wyswietl_akord(self):
        """ FUNKCJA TESTOWA. DO WYWALENIA."""
        print(self._sopran.podaj_swoj_kod_bezwzgledny(), self._alt.podaj_swoj_kod_bezwzgledny(),
              self._tenor.podaj_swoj_kod_bezwzgledny(), self._bas.podaj_swoj_kod_bezwzgledny(), self._dlugosc.value)
