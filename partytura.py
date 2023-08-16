import tonacja
import akord
import metrum
from typing import List, Union


class Partytura:

    _lista_akordow: List[Union[akord.Akord, str]] = []

    def __init__(self, nowa_tonacja: tonacja.Tonacja, nowe_metrum: str, nowa_liczba_taktow: int):
        if nowa_liczba_taktow > 0:
            self._tonacja: tonacja.Tonacja = nowa_tonacja
            self._metrum: metrum.Metrum = metrum.Metrum(nowe_metrum)
            self._liczba_taktow: int = nowa_liczba_taktow

        else:
            raise ValueError("Niepoprawna liczba taktów")


    def podaj_metrum(self) -> metrum.Metrum:
        return self._metrum

    def podaj_tonacje(self) -> tonacja.Tonacja:
        return self._tonacja

    def podaj_liczbe_taktow(self) -> int:
        return self._liczba_taktow

    def dodaj_akord(self, nowy_akord: akord.Akord) -> None:
        """Funkcja dodaje akord podany w swoim argumencie na koniec listy"""
        self._lista_akordow.append(nowy_akord)

    def zakoncz_takt(self) -> None:
        """Funkcja dopisuje 'T' na koniec obecnej listy akordów.
        Nie sprawdza, czy akord jest kompletny"""
        self._lista_akordow.append('T')

    def czy_poprawna_liczba_taktow(self) -> bool:
        """True, jeśli poprawna liczba znaków końca taktu (T). Wtedy wprowadzanie zakończone."""
        if self._liczba_taktow == self._lista_akordow.count('T'):
            return True
        else:
            return False

    def podaj_liste_akordow(self) -> List[Union[akord.Akord, str]]:
        return self._lista_akordow