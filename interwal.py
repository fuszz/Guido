from tonacja import Tonacja
from enumerations.enum_nazwy_interwalow import NazwaInterwalu
from dzwiek import Dzwiek
from akord import Akord

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
        return (isinstance(other, Interwal) and
                self._liczba_oktaw == other.podaj_liczbe_oktaw() and
                self._interwal == other.podaj_nazwe())

    def __lt__(self, other):
        return (isinstance(other, Interwal) and
                self._liczba_oktaw < other.podaj_liczbe_oktaw() or
                (self._liczba_oktaw == other.podaj_liczbe_oktaw() and
                 self._interwal < other.podaj_nazwe()))

    def __gt__(self, other):
        return (isinstance(other, Interwal) and
                self._liczba_oktaw > other.podaj_liczbe_oktaw() or
                (self._liczba_oktaw == other.podaj_liczbe_oktaw() and
                 self._interwal > other.podaj_nazwe()))

    def __init__(self, liczba_oktaw: int, interwal: NazwaInterwalu):
        self._liczba_oktaw = liczba_oktaw
        self._interwal: NazwaInterwalu = interwal

    def podaj_nazwe(self) -> NazwaInterwalu:
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

        if dzwiek_a.podaj_kod_midi() > dzwiek_b.podaj_kod_midi():
            dzwiek_a, dzwiek_b = dzwiek_b, dzwiek_a
        pelnych_oktaw = (dzwiek_b.podaj_kod_midi() - dzwiek_a.podaj_kod_midi()) // 12

        stopien_a = dzwiek_a.podaj_stopien_w_tonacji(badana_tonacja)
        stopien_b = dzwiek_b.podaj_stopien_w_tonacji(badana_tonacja)

        symbol = INTERWALY_DUR[stopien_a][stopien_b] if badana_tonacja.czy_dur() else INTERWALY_MOLL[stopien_a][
            stopien_b]
        return Interwal(pelnych_oktaw, NazwaInterwalu.stworz_z_symbolu(symbol))

    def __str__(self) -> str:
        return str(str(self._liczba_oktaw) + ", " + str(self._interwal.name))

    def czy_oktawa_czysta(self) -> bool:
        return self._interwal == NazwaInterwalu.PRYMA_CZYSTA and self._liczba_oktaw > 0

    def czy_kwinta_czysta(self) -> bool:
        return self._interwal == NazwaInterwalu.KWINTA_CZYSTA

    @classmethod
    def podaj_interwaly_w_akordzie(cls, akord: Akord, badana_tonacja) -> list['Interwal']:
        """Zwraca krotkę interwałów (klasa Interwal) pomiędzy głosami w następującej kolejności: 
        S-A, S-T, S-B, A-T, A-B, T-B."""
        return [Interwal.stworz_z_dzwiekow(akord.podaj_sopran(), akord.podaj_alt(), badana_tonacja),
                Interwal.stworz_z_dzwiekow(akord.podaj_sopran(), akord.podaj_tenor(), badana_tonacja),
                Interwal.stworz_z_dzwiekow(akord.podaj_sopran(), akord.podaj_bas(), badana_tonacja),
                Interwal.stworz_z_dzwiekow(akord.podaj_alt(), akord.podaj_tenor(), badana_tonacja),
                Interwal.stworz_z_dzwiekow(akord.podaj_alt(), akord.podaj_bas(), badana_tonacja),
                Interwal.stworz_z_dzwiekow(akord.podaj_tenor(), akord.podaj_bas(), badana_tonacja)]

    def czy_zwiekszony(self) -> bool:
        return self._interwal.czy_zwiekszony()
