import dzwiek
import tonacja
import enum_wartosci_nut
import enum_funkcje
import enum_przewroty
import enum_zdwojony_skladnik
import enum_funkcje


class Akord:
    def __init__(self, nowy_sopran: dzwiek.Dzwiek, nowy_alt: dzwiek.Dzwiek, nowy_tenor: dzwiek.Dzwiek,
                 nowy_bas: dzwiek.Dzwiek, dlugosc: float):
        self._dlugosc:  enum_wartosci_nut.WartosciNut = enum_wartosci_nut.WartosciNut(dlugosc)
        self._alt: dzwiek.Dzwiek = nowy_alt
        self._sopran: dzwiek.Dzwiek = nowy_sopran
        self._tenor: dzwiek.Dzwiek = nowy_tenor
        self._bas: dzwiek.Dzwiek = nowy_bas

    def podaj_dlugosc(self) -> enum_wartosci_nut.WartosciNut:
        return self._dlugosc

    def podaj_sopran(self) -> dzwiek.Dzwiek:
        return self._sopran

    def podaj_alt(self) -> dzwiek.Dzwiek:
        return self._alt

    def podaj_tenor(self) -> dzwiek.Dzwiek:
        return self._tenor

    def podaj_bas(self) -> dzwiek.Dzwiek:
        return self._bas

    def ustal_funkcje(self, dana_tonacja: tonacja.Tonacja) -> enum_funkcje.Funkcja:
        try:
            stopien_sopranu: int = self._sopran.podaj_swoj_stopien(dana_tonacja)
            stopien_altu: int = self._alt.podaj_swoj_stopien(dana_tonacja)
            stopien_tenoru: int = self._tenor.podaj_swoj_stopien(dana_tonacja)
            stopien_basu: int = self._bas.podaj_swoj_stopien(dana_tonacja)
        except ValueError:
            return enum_funkcje.Funkcja.BLAD

        lista_stopni = [stopien_sopranu, stopien_altu, stopien_tenoru, stopien_basu]

        lista_stopni = sorted(set(lista_stopni))

        if lista_stopni == [0, 2, 4]:
            if dana_tonacja.czy_dur():
                return enum_funkcje.Funkcja('T')
            else:
                return enum_funkcje.Funkcja('mT')

        elif lista_stopni == [0, 3, 5]:
            if dana_tonacja.czy_dur():
                return enum_funkcje.Funkcja('S')
            else:
                return enum_funkcje.Funkcja('mS')

        elif lista_stopni == [1, 4, 6]:
            return enum_funkcje.Funkcja('D')

        elif lista_stopni == [1, 3, 4, 6]:
            return enum_funkcje.Funkcja('D7')

        else:
            return enum_funkcje.Funkcja('Błąd')

    def ustal_przewrot(self, dana_tonacja: tonacja.Tonacja) -> enum_przewroty.Przewrot:
        try:
            stopien_basu: int = self._bas.podaj_swoj_stopien(dana_tonacja)
        except ValueError:
            return enum_przewroty.Przewrot.NIE_ZDEFINIOWANO
        funkcja: enum_funkcje.Funkcja = self.ustal_funkcje(dana_tonacja)

        if funkcja == enum_funkcje.Funkcja.TONIKA or funkcja == enum_funkcje.Funkcja.MOLL_TONIKA:
            if stopien_basu == 0:
                return enum_przewroty.Przewrot.POSTAC_ZASADNICZA
            elif stopien_basu == 2:
                return enum_przewroty.Przewrot.PIERWSZY
            elif stopien_basu == 4:
                return enum_przewroty.Przewrot.DRUGI

        elif funkcja == enum_funkcje.Funkcja.SUBDOMINANTA or funkcja == enum_funkcje.Funkcja.MOLL_SUBDOMINANTA:
            if stopien_basu == 3:
                return enum_przewroty.Przewrot.POSTAC_ZASADNICZA
            elif stopien_basu == 5:
                return enum_przewroty.Przewrot.PIERWSZY
            elif stopien_basu == 1:
                return enum_przewroty.Przewrot.DRUGI

        elif funkcja == enum_funkcje.Funkcja.DOMINANTA:
            if stopien_basu == 4:
                return enum_przewroty.Przewrot.POSTAC_ZASADNICZA
            elif stopien_basu == 6:
                return enum_przewroty.Przewrot.PIERWSZY
            elif stopien_basu == 1:
                return enum_przewroty.Przewrot.DRUGI

        elif funkcja == enum_funkcje.Funkcja.DOMINANTA_SEPTYMOWA:
            if stopien_basu == 4:
                return enum_przewroty.Przewrot.POSTAC_ZASADNICZA
            elif stopien_basu == 6:
                return enum_przewroty.Przewrot.PIERWSZY
            elif stopien_basu == 1:
                return enum_przewroty.Przewrot.DRUGI
            elif stopien_basu == 3:
                return enum_przewroty.Przewrot.DRUGI

        else:
            return enum_przewroty.Przewrot.NIE_ZDEFINIOWANO

    def ustal_dwojenie(self, dana_tonacja: tonacja.Tonacja) -> enum_zdwojony_skladnik.ZdwojonySkladnik:
        funkcja_akordu = self.ustal_funkcje(dana_tonacja)
        if funkcja_akordu == enum_funkcje.Funkcja.DOMINANTA_SEPTYMOWA:
            return enum_zdwojony_skladnik.ZdwojonySkladnik.BRAK
        try:
            stopien_sopranu: int = self._sopran.podaj_swoj_stopien(dana_tonacja)
            stopien_altu: int = self._alt.podaj_swoj_stopien(dana_tonacja)
            stopien_tenoru: int = self._tenor.podaj_swoj_stopien(dana_tonacja)
            stopien_basu: int = self._bas.podaj_swoj_stopien(dana_tonacja)
        except ValueError:
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