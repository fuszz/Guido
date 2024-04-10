import blad
import tonacja
from enumerations import enum_kody_midi, enum_nazwy_dzwiekow


# Napisane docstringi

class Dzwiek:

    def __eq__(self, other):
        return type(self) is type(
            other) and self._nazwa_dzwieku == other._nazwa_dzwieku and self._oktawa_dzwieku == other._oktawa_dzwieku

    def __init__(self, nowa_oktawa_dzwieku: int, nowa_nazwa_dzwieku: str):
        """
        Tworzy nową instancję klasy Dzwiek. Zwraca BladTworzeniaDzwieku w dwóch przypadkach:
            1. Gdy podano niepoprawną wartość oktawy (spoza zakresu od 0 do 8 wł.)
            2. Gdy podano niepoprawną nazwę dźwięku (spoza enuma)
        :param nowa_oktawa_dzwieku: int z zakresy od 0 do 8 (patrz: dokumentacja)
        :param nowa_nazwa_dzwieku:  str o wartości równej jednej z
        """

        if nowa_oktawa_dzwieku not in range(0, 9) or not isinstance(nowa_oktawa_dzwieku, int):
            raise blad.BladTworzeniaDzwieku("Niepoprawna oktawa")

        try:
            self._nazwa_dzwieku = enum_nazwy_dzwiekow.NazwyDzwiekow(nowa_nazwa_dzwieku)
        except ValueError:
            raise blad.BladTworzeniaDzwieku("Niepoprawna nazwa")
        self._oktawa_dzwieku = nowa_oktawa_dzwieku

    def podaj_oktawe(self) -> int:
        """
        Zwraca numer oktawy, w której zawiera się dźwięk.
        :return: int
        """
        return self._oktawa_dzwieku

    def podaj_nazwe_dzwieku(self) -> enum_nazwy_dzwiekow.NazwyDzwiekow:
        """
        Zwraca nazwę dźwięku jako enum_nazwy_dzwiekow.NazwaDzwieku
        :return: enum_nazwy_dzwiekow.NazwyDzwiekow
        """
        return self._nazwa_dzwieku

    def podaj_swoj_stopien(self, badana_tonacja: tonacja.Tonacja) -> int:
        """
        Podaje stopień dźwięku w pewnej tonacji.
        W przypadku nieporawnego dżwięku (względem danej tonacji) podnosi enum_blad.BladDzwiekPozaTonacja
        :param badana_tonacja: tonacja.Tonacja - tonacja, w której bada się stopień dźwięku
        :return: int
        """
        dzwieki_badanej_tonacji = badana_tonacja.podaj_liste_nazw_dzwiekow()
        if self._nazwa_dzwieku.value not in dzwieki_badanej_tonacji:
            raise blad.BladDzwiekPozaTonacja("Dzwiek nie jest stopniem tej tonacji")
        else:
            return dzwieki_badanej_tonacji.index(self._nazwa_dzwieku.value)

    def podaj_swoj_kod_wzgledny(self, badana_tonacja: tonacja.Tonacja) -> int:
        """
        Podaje kod względny dźwięku w tonacji, czyli <nr oktawy>*7+<stopień dźwięku w tonacji>
        :param badana_tonacja: tonacja.Tonacja - tonacja, w której bada się stopień dźwięku
        :return: int - kod 'względny'
        """
        return self._oktawa_dzwieku * 7 + self.podaj_swoj_stopien(badana_tonacja)

    def podaj_swoj_kod_midi(self) -> int:
        """
        Zwraca kod dźwięku w postaci MIDI.
        Nigdy nie powinno zwrócić błędu, bo każdy poprawny dźwięk ma taki kod.
        [<numer oktawy> * 12 + <dzwiek, gdzie c = 0, a h = 11>] + 12
        :return: int
        """
        kod: int = 12 + 12 * self._oktawa_dzwieku
        for kod_bezwzgledny in enum_kody_midi.KodyMidi:
            if kod_bezwzgledny.name.lower() == self._nazwa_dzwieku.value[0]:
                kod += kod_bezwzgledny.value
                for znak in self._nazwa_dzwieku.value[1:]:
                    if znak == '#':
                        kod += 1
                    elif znak == 'b':
                        kod -= 1
                return kod
