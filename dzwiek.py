import tonacja
import nazwy_dzwiekow
class Dzwiek:
    _oktawa_dzwieku: int
    _nazwa_dzwieku: nazwy_dzwiekow.NazwyDzwiekow

    def __init__(self, nowa_oktawa_dzwieku: int, nowa_nazwa_dzwieku: str):
        self._oktawa_dzwieku = nowa_oktawa_dzwieku
        self._nazwa_dzwieku = nazwy_dzwiekow.NazwyDzwiekow(nowa_nazwa_dzwieku)

    def podaj_oktawe(self) -> int:
        """Zwraca względną oktawę, gdzie znajduje się dźwięk."""
        return self._oktawa_dzwieku

    def podaj_nazwe_dzwieku(self) -> str:
        """Zwraca nazwę dźwięku"""
        return self._nazwa_dzwieku.value

    def podaj_swoj_stopien(self, odpytywana_tonacja: tonacja.Tonacja) -> int:
        '''
        w przypadku nieporawnego dżwięu (względem danej tonacji)
        wyrzuca ValueError
        '''
        dzwieki_odpytywanej_tonacji = odpytywana_tonacja.podaj_liste_nazw_dzwiekow()
        return dzwieki_odpytywanej_tonacji.index(self._nazwa_dzwieku.value)

    def podaj_swoj_kod(self, nazwa_tonacji: str) -> int:
        if self.podaj_swoj_stopien(nazwa_tonacji) == -1:
            return -1
        else:
            return self._oktawa_dzwieku * 7 + self.podaj_swoj_stopien(nazwa_tonacji)
