import blad
import enum


# CZY TA KLASA NIE POWINNA BYĆ W ZASADZIE ENUMEM???

class Tonacja(enum.Enum):
    # Tonacje durowe

    CES_DUR = {
        "tryb": "+",
        "symbol": "Cb",
        "dzwieki": ['cb', 'db', 'eb', 'fb', 'gb', 'ab', 'hb']
    }
    GES_DUR = {
        "tryb": "+",
        "symbol": "Gb",
        "dzwieki": ['gb', 'ab', 'hb', 'cb', 'db', 'eb', 'f']
    }
    DES_DUR = {
        "tryb": "+",
        "symbol": "Db",
        "dzwieki": ['db', 'eb', 'f', 'gb', 'ab', 'hb', 'c']
    }
    AES_DUR = {
        "tryb": "+",
        "symbol": "Ab",
        "dzwieki": ['ab', 'hb', 'c', 'db', 'eb', 'f', 'g']
    }
    ES_DUR = {
        "tryb": "+",
        "symbol": "Eb",
        "dzwieki": ['eb', 'f', 'g', 'ab', 'hb', 'c', 'd']
    }
    B_DUR = {
        "tryb": "+",
        "symbol": "Hb",
        "dzwieki": ['hb', 'c', 'd', 'eb', 'f', 'g', 'a']
    }
    F_DUR = {
        "tryb": "+",
        "symbol": "F",
        "dzwieki": ['f', 'g', 'a', 'hb', 'c', 'd', 'e']
    }
    C_DUR = {
        "tryb": "+",
        "symbol": "C",
        "dzwieki": ['c', 'd', 'e', 'f', 'g', 'a', 'h']
    }
    G_DUR = {
        "tryb": "+",
        "symbol": "G",
        "dzwieki": ['g', 'a', 'h', 'c', 'd', 'e', 'f#']
    }
    D_DUR = {
        "tryb": "+",
        "symbol": "D",
        "dzwieki": ['d', 'e', 'f#', 'g', 'a', 'h', 'c#']
    }
    A_DUR = {
        "tryb": "+",
        "symbol": "A",
        "dzwieki": ['a', 'h', 'c#', 'd', 'e', 'f#', 'g#']
    }
    E_DUR = {
        "tryb": "+",
        "symbol": "E",
        "dzwieki": ['e', 'f#', 'g#', 'a', 'h', 'c#', 'd#']
    }
    H_DUR = {
        "tryb": "+",
        "symbol": "H",
        "dzwieki": ['h', 'c#', 'd#', 'e', 'f#', 'g#', 'a#']
    }
    FIS_DUR = {
        "tryb": "+",
        "symbol": "F#",
        "dzwieki": ['f#', 'g#', 'a#', 'h', 'c#', 'd#', 'e#']
    }
    CIS_DUR = {
        "tryb": "+",
        "symbol": "C#",
        "dzwieki": ['c#', 'd#', 'e#', 'f#', 'g#', 'a#', 'h#']
    }

    # Tonacje molowe

    AS_MOLL = {
        "tryb": "-",
        "symbol": "ab",
        "dzwieki": ['ab', 'hb', 'cb', 'db', 'eb', 'fb', 'g']
    }
    ES_MOLL = {
        "tryb": "-",
        "symbol": "eb",
        "dzwieki": ['eb', 'f', 'gb', 'ab', 'hb', 'cb', 'd']
    }
    B_MOLL = {
        "tryb": "-",
        "symbol": "hb",
        "dzwieki": ['hb', 'c', 'db', 'eb', 'f', 'gb', 'a']
    }
    F_MOLL = {
        "tryb": "-",
        "symbol": "f",
        "dzwieki": ['f', 'g', 'ab', 'hb', 'c', 'db', 'e']
    }
    C_MOLL = {
        "tryb": "-",
        "symbol": "c",
        "dzwieki": ['c', 'd', 'eb', 'f', 'g', 'ab', 'h']
    }
    G_MOLL = {
        "tryb": "-",
        "symbol": "g",
        "dzwieki": ['g', 'a', 'hb', 'c', 'd', 'eb', 'f#']
    }
    D_MOLL = {
        "tryb": "-",
        "symbol": "d",
        "dzwieki": ['d', 'e', 'f', 'g', 'a', 'hb', 'c#']
    }
    A_MOLL = {
        "tryb": "-",
        "symbol": "a",
        "dzwieki": ['a', 'h', 'c', 'd', 'e', 'f', 'g#']
    }
    E_MOLL = {
        "tryb": "-",
        "symbol": "e",
        "dzwieki": ['e', 'f#', 'g', 'a', 'h', 'c', 'd#']
    }
    H_MOLL = {
        "tryb": "-",
        "symbol": "h",
        "dzwieki": ['h', 'c#', 'd', 'e', 'f#', 'g', 'a#']
    }
    FIS_MOLL = {
        "tryb": "-",
        "symbol": "f#",
        "dzwieki": ['f#', 'g#', 'a', 'h', 'c#', 'd', 'e#']
    }
    CIS_MOLL = {
        "tryb": "-",
        "symbol": "c#",
        "dzwieki": ['c#', 'd#', 'e', 'f#', 'g#', 'a', 'h#']
    }
    GIS_MOLL = {
        "tryb": "-",
        "symbol": "g#",
        "dzwieki": ['g#', 'a#', 'h', 'c#', 'd#', 'e', 'f##']
    }

    DIS_MOLL = {
        "tryb": "-",
        "symbol": "d#",
        "dzwieki": ['d#', 'e#', 'f#', 'g#', 'a#', 'h', 'c##']
    }

    AIS_MOLL = {
        "tryb": "-",
        "symbol": "a#",
        "dzwieki": ['a#', 'h#', 'c#', 'd#', 'e#', 'f#', 'g##']
    }

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name

    @classmethod
    def stworz_z_symbolu(cls, symbol_tonacji: str) -> 'Tonacja':
        """
        Konstruktor inicjuje instancję klasy Tonacja. Rzuca BladTworzeniaTonacji(), gdy nazwa tonacji jest niepoprawna.
        """
        for element in cls:
            if element.value["symbol"] == symbol_tonacji:
                return element
        raise blad.BladTworzeniaTonacji("Sprawdź, czy podana nazwa tonacji jest poprawna.")

    def podaj_symbol(self) -> str:
        return self.value["symbol"]

    def czy_dur(self) -> bool:
        """Funkcja zwraca True dla durowej tonacji i False dla molowej."""
        return True if self.value["tryb"] == "+" else False

    def podaj_liste_nazw_dzwiekow(self) -> list[str]:
        """Zwraca listę dźwięków występujących w tonacji."""
        return self.value["dzwieki"]
