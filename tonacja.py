class Tonacja:

    _WSZYSTKIE_DUROWE_TONACJE = ['Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Hb', 'F', 'C', 'G', 'D', 'A', 'E', 'H', 'F#', 'C#']
    _WSZYSTKIE_MOLOWE_TONACJE = ['ab', 'eb', 'hb', 'f', 'c', 'g', 'd', 'a', 'e', 'h', 'f#', 'c#', 'g#', 'd#', 'a#']

    _SLOWNIK_DZWIEKOW_DUROWE = {
        'Cb': ['cb', 'db', 'eb', 'fb', 'gb', 'ab', 'hb'],
        'Gb': ['gb', 'ab', 'hb', 'cb', 'db', 'eb', 'f'],
        'Db': ['db', 'eb', 'f', 'gb', 'ab', 'hb', 'c'],
        'Ab': ['ab', 'hb', 'c', 'db', 'eb', 'f', 'g'],
        'Eb': ['eb', 'f', 'g', 'ab', 'hb', 'c', 'd'],
        'Hb': ['hb', 'c', 'd', 'eb', 'f', 'g', 'a'],
        'F': ['f', 'g', 'a', 'hb', 'c', 'd', 'e'],
        'C': ['c', 'd', 'e', 'f', 'g', 'a', 'h'],
        'G': ['g', 'a', 'h', 'c', 'd', 'e', 'f#'],
        'D': ['d', 'e', 'f#', 'g', 'a', 'h', 'c#'],
        'A': ['a', 'h', 'c#', 'd', 'e', 'f#', 'g#'],
        'E': ['e', 'f#', 'g#', 'a', 'h', 'c#', 'd#'],
        'H': ['h', 'c#', 'd#', 'e', 'f#', 'g#', 'a#'],
        'F#': ['f#', 'g#', 'a#', 'h', 'c#', 'd#', 'e#'],
        'C#': ['c#', 'd#', 'e#', 'f#', 'g#', 'a#', 'h#']
    }

    _SLOWNIK_DZWIEKOW_MOLOWE = {
        'ab': ['ab', 'hb', 'cb', 'db', 'eb', 'fb', 'g'],
        'eb': ['eb', 'f', 'gb', 'ab', 'hb', 'cb', 'd'],
        'hb': ['hb', 'c', 'db', 'eb', 'f', 'gb', 'a'],
        'f':  ['f', 'g', 'ab', 'hb', 'c', 'db', 'e'],
        'c':  ['c', 'd', 'eb', 'f', 'g', 'ab', 'h'],
        'g':  ['g', 'a', 'hb', 'c', 'd', 'eb', 'f#'],
        'd':  ['d', 'e', 'f', 'g', 'a', 'hb', 'c#'],
        'a':  ['a', 'h', 'c', 'd', 'e', 'f', 'g#'],
        'e':  ['e', 'f#', 'g', 'a', 'h', 'c', 'd#'],
        'h':  ['h', 'c#', 'd', 'e', 'f#', 'g', 'a#'],
        'f#': ['f#', 'g#', 'a', 'h', 'c#', 'd', 'e#'],
        'c#': ['c#', 'd#', 'e', 'f#', 'g#', 'a', 'h#'],
        'g#': ['g#', 'a#', 'h', 'c#', 'd#', 'e', 'f##'],
        'd#': ['d#', 'e#', 'f#', 'g#', 'a#', 'h', 'c##'],
        'a#': ['a#', 'h#', 'c#', 'd#', 'e#', 'f#', 'g##']
    }

    def __init__(self, nazwa_tonacji: str):
        if nazwa_tonacji in self._WSZYSTKIE_DUROWE_TONACJE:
            self._nazwa: str = nazwa_tonacji
            self._czy_dur: bool = True
            self._nazwy_dzwiekow_tonacji: list[str] = self._SLOWNIK_DZWIEKOW_DUROWE[self._nazwa]

        elif nazwa_tonacji in self._WSZYSTKIE_MOLOWE_TONACJE:
            self._nazwa: str = nazwa_tonacji
            self._czy_dur: bool = False
            self._nazwy_dzwiekow_tonacji: list[str] = self._SLOWNIK_DZWIEKOW_MOLOWE[self._nazwa]

        else:
            raise ValueError("Podana nazwa nie stanowi nazwy tonacji.")

    def podaj_nazwe(self) -> str:
        return self._nazwa
        
    def czy_dur(self) -> bool:
        """Funkcja zwraca True dla durowej tonacji i False dla molowej."""
        return self._czy_dur

    def podaj_liste_nazw_dzwiekow(self) -> list[str]:
        """Zwraca listę dźwięków występujących w tonacji."""
        return self._nazwy_dzwiekow_tonacji


