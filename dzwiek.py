import tonacja
from enumerations import enum_bezwzgledne_kody_dzwiekow, enum_nazwy_dzwiekow, enum_bledy


class Dzwiek:

    def __init__(self, nowa_oktawa_dzwieku: int, nowa_nazwa_dzwieku: str):
        """ Konstruktor klasy Dzwiek zwraca BladTworzeniaDzwieku w dwóch przypadkach:
            1. Gdy podano niepoprawną wartość oktawy (spoza zakresy od 0 do 8 wł.)
            2. Gdy podano niepoprawną nazwę dźwięku (spoza enuma)
        """
        if nowa_oktawa_dzwieku not in range(9):
            raise enum_bledy.BladTworzeniaDzwieku("Podana niepoprawna wartość oktawy")
        else:
            self._oktawa_dzwieku = nowa_oktawa_dzwieku

        try:
            self._nazwa_dzwieku = enum_nazwy_dzwiekow.NazwyDzwiekow(nowa_nazwa_dzwieku)
        except ValueError:
            raise enum_bledy.BladTworzeniaDzwieku("Podana niepoprawna nazwa dźwięku")

    def podaj_oktawe(self) -> int:
        """Zwraca względną oktawę, gdzie znajduje się dźwięk."""
        return self._oktawa_dzwieku

    def podaj_nazwe_dzwieku(self) -> str:
        """Zwraca nazwę dźwięku."""
        return self._nazwa_dzwieku.value

    def podaj_swoj_stopien(self, badana_tonacja: tonacja.Tonacja) -> int:
        """
        W przypadku nieporawnego dżwięku (względem danej tonacji)
        wyrzuca enum_blad BladDzwiekPozaTonacja
        """
        dzwieki_badanej_tonacji = badana_tonacja.podaj_liste_nazw_dzwiekow()
        if self._nazwa_dzwieku.value not in dzwieki_badanej_tonacji:
            raise enum_bledy.BladDzwiekPozaTonacja("")
        else:
            return dzwieki_badanej_tonacji.index(self._nazwa_dzwieku.value)

    def podaj_swoj_kod_wzgledny(self, odpytywana_tonacja: tonacja.Tonacja) -> int:
        return self._oktawa_dzwieku * 7 + self.podaj_swoj_stopien(odpytywana_tonacja)

    def podaj_swoj_kod_bezwzgledny(self) -> int:
        """
        Zwraca bezwzględny kod dźwięku.
        <numer oktawy> * 12 + <dzwiek, gdzie c = 0, a h = 11>
        """
        kod: int = 12 * self._oktawa_dzwieku
        for kod_bezwzgledny in enum_bezwzgledne_kody_dzwiekow.BezwzgledneKodyDzwiekow:
            if kod_bezwzgledny.name.lower() == self._nazwa_dzwieku.value[0]:
                kod += kod_bezwzgledny.value
                for znak in self._nazwa_dzwieku.value[1:]:
                    if znak == '#':
                        kod += 1
                    elif znak == 'b':
                        kod -= 1
                return kod
