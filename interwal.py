from tonacja import Tonacja
from enumerations.enum_nazwy_interwalow import NazwyInterwalow
from dzwiek import Dzwiek

INTERWALY_DUR = [['1', '2', '3', '4', '5', '6', '7'],
                 ['7', '1', '2', '3>', '4', '5', '6'],
                 ['6>', '7', '1', '2>', '3>', '4', '5'],
                 ['5', '6', '7<', '1', '2', '3', '4<'],
                 ['4', '5', '6', '7', '1', '2', '3'],
                 ['3>', '4', '5', '6>', '7', '1', '2'],
                 ['2>', '3>', '4', '5>', '6', '7', '1']]

INTERWALY_MOLL = [['1', '2', '3>', '4', '5', '6>', '7<'],
                  ['7', '1', '2>', '3>', '4', '5>', '6'],
                  ['6', '7', '1', '2', '3', '4', '5<'],
                  ['5', '6', '7', '1', '2', '3>', '4<'],
                  ['4', '5', '6>', '7', '1', '2>', '3'],
                  ['3', '4<', '5', '6', '7<', '1', '2<'],
                  ['2>', '3>', '4>', '5>', '6>', '7>', '1']]


class Interwal:

    def __eq__(self, other):
        return (type(self) == type(other) and
                self._liczba_oktaw == other.podaj_liczbe_oktaw() and
                self._interwal == other.podaj_interwal())

    def __lt__(self, other):
        return (type(self) == type(other) and
                self._liczba_oktaw < other.podaj_liczbe_oktaw() or
                (self._liczba_oktaw == other.podaj_liczbe_oktaw() and
                 self._interwal < other.podaj_interwal()))

    def __gt__(self, other):
        return (type(self) == type(other) and
                self._liczba_oktaw > other.podaj_liczbe_oktaw() or
                (self._liczba_oktaw == other.podaj_liczbe_oktaw() and
                 self._interwal > other.podaj_interwal()))

    def __init__(self, liczba_oktaw: int, interwal: NazwyInterwalow):
        self._liczba_oktaw = liczba_oktaw
        self._interwal: NazwyInterwalow = interwal

    def podaj_interwal(self) -> NazwyInterwalow:
        return self._interwal

    def podaj_liczbe_oktaw(self) -> int:
        return self._liczba_oktaw

    @classmethod
    def stworz_z_dzwiekow(cls, dzwiek_a: Dzwiek, dzwiek_b: Dzwiek, badana_tonacja: Tonacja) -> 'Interwal':
        """
        Podaje, jaki interwał leży pomiędzy dźwiękami a i b. Nieczuły na kolejność dźwięków. Dźwięki muszą znajdować się
        w tonacji badana_tonacja, w przeciwnym razie podniesie BladDzwiekPozaTonacją.
        :param dzwiek_a: dzwiek a, dzwiek.Dzwiek
        :param dzwiek_b: dzwiek b, dzwiek.Dzwiek
        :param badana_tonacja: tonacja, w ktorej leżą oba dźwięki, instancja tonacja.Tonacja.
        :return: (int, Interwal), gdzie int jest liczbą pełnych oktaw znajdujących się między dźwiękami,
        a Interwał to instancja klasy enum_interwal.Interwal.
        """

        if dzwiek_a.podaj_swoj_kod_midi() > dzwiek_b.podaj_swoj_kod_midi():
            dzwiek_a, dzwiek_b = dzwiek_b, dzwiek_a
        pelnych_oktaw = (dzwiek_b.podaj_swoj_kod_midi() - dzwiek_a.podaj_swoj_kod_midi()) // 12

        stopien_a = dzwiek_a.podaj_swoj_stopien(badana_tonacja)
        stopien_b = dzwiek_b.podaj_swoj_stopien(badana_tonacja)

        symbol = INTERWALY_DUR[stopien_a][stopien_b] if badana_tonacja.czy_dur() else INTERWALY_MOLL[stopien_a][
            stopien_b]
        return Interwal(pelnych_oktaw, NazwyInterwalow.interwal_z_symbolu(symbol))

    def __str__(self) -> str:
        return str(str(self._liczba_oktaw) + ", " + str(self._interwal.name))

    def czy_oktawa_czysta(self) -> bool:
        return self._interwal == NazwyInterwalow.PRYMA_CZYSTA and self._liczba_oktaw > 0

    def czy_kwinta_czyta(self) -> bool:
        return self._interwal == NazwyInterwalow.KWINTA_CZYSTA
