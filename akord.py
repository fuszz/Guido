import dzwiek
import tonacja
import wartosci_nut
import funkcje
import przewroty


class Akord:
    def __init__(self, nowy_sopran: dzwiek.Dzwiek, nowy_alt: dzwiek.Dzwiek, nowy_tenor: dzwiek.Dzwiek,
                 nowy_bas: dzwiek.Dzwiek, dlugosc: float):
        self._dlugosc: wartosci_nut.WartosciNut = wartosci_nut.WartosciNut(dlugosc)
        self._alt: dzwiek.Dzwiek = nowy_alt
        self._sopran: dzwiek.Dzwiek = nowy_sopran
        self._tenor: dzwiek.Dzwiek = nowy_tenor
        self._bas: dzwiek.Dzwiek = nowy_bas

    def podaj_dlugosc(self) -> wartosci_nut.WartosciNut:
        return self._dlugosc

    def podaj_sopran(self) -> dzwiek.Dzwiek:
        return self._sopran

    def podaj_alt(self) -> dzwiek.Dzwiek:
        return self._alt

    def podaj_tenor(self) -> dzwiek.Dzwiek:
        return self._tenor

    def podaj_bas(self) -> dzwiek.Dzwiek:
        return self._bas

    def ustal_funkcje(self, dana_tonacja: tonacja.Tonacja) -> funkcje.Funkcja:
        try:
            stopien_sopranu: int = self._sopran.podaj_swoj_stopien(dana_tonacja)
            stopien_altu: int = self._alt.podaj_swoj_stopien(dana_tonacja)
            stopien_tenoru: int = self._tenor.podaj_swoj_stopien(dana_tonacja)
            stopien_basu: int = self._bas.podaj_swoj_stopien(dana_tonacja)
        except ValueError:
            return funkcje.Funkcja.BLAD

        lista_stopni = [stopien_sopranu, stopien_altu, stopien_tenoru, stopien_basu]

        lista_stopni = sorted(set(lista_stopni))

        if lista_stopni == [0, 2, 4]:
            if dana_tonacja.czy_dur():
                return funkcje.Funkcja('T')
            else:
                return funkcje.Funkcja('mT')

        elif lista_stopni == [0, 3, 5]:
            if dana_tonacja.czy_dur():
                return funkcje.Funkcja('S')
            else:
                return funkcje.Funkcja('mS')

        elif lista_stopni == [1, 4, 6]:
            return funkcje.Funkcja('D')

        elif lista_stopni == [1, 3, 4, 6]:
            return funkcje.Funkcja('D7')

        else:
            return funkcje.Funkcja('Błąd')

    def ustal_przewrot(self, dana_tonacja: tonacja.Tonacja) -> przewroty.Przewrot:
        stopien_basu: int = self._bas.podaj_swoj_stopien(dana_tonacja)
        funkcja: funkcje.Funkcja = self.ustal_funkcje(dana_tonacja)

        if funkcja == funkcje.Funkcja.TONIKA or funkcja == funkcje.Funkcja.MOLL_TONIKA:
            if stopien_basu == 0:
                return przewroty.Przewrot.POSTAC_ZASADNICZA
            elif stopien_basu == 2:
                return przewroty.Przewrot.PIERWSZY
            elif stopien_basu == 4:
                return przewroty.Przewrot.DRUGI

        elif funkcja == funkcje.Funkcja.SUBDOMINANTA or funkcja == funkcje.Funkcja.MOLL_SUBDOMINANTA:
            if stopien_basu == 3:
                return przewroty.Przewrot.POSTAC_ZASADNICZA
            elif stopien_basu == 5:
                return przewroty.Przewrot.PIERWSZY
            elif stopien_basu == 1:
                return przewroty.Przewrot.DRUGI

        elif funkcja == funkcje.Funkcja.DOMINANTA:
            if stopien_basu == 4:
                return przewroty.Przewrot.POSTAC_ZASADNICZA
            elif stopien_basu == 6:
                return przewroty.Przewrot.PIERWSZY
            elif stopien_basu == 1:
                return przewroty.Przewrot.DRUGI

        elif funkcja == funkcje.Funkcja.DOMINANTA_SEPTYMOWA:
            if stopien_basu == 4:
                return przewroty.Przewrot.POSTAC_ZASADNICZA
            elif stopien_basu == 6:
                return przewroty.Przewrot.PIERWSZY
            elif stopien_basu == 1:
                return przewroty.Przewrot.DRUGI
            elif stopien_basu == 3:
                return przewroty.Przewrot.DRUGI

        else:
            return przewroty.Przewrot.NIE_ZDEFINIOWANO
