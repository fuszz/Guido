import enum
import blad


class Metrum(enum.Enum):
    """Typ wyliczeniowy przechowujący wartości metrum. Ograniczamy się do 3/4 i 4/4"""
    TRZY_CZWARTE = '3/4'
    CZTERY_CZWARTE = '4/4'

    @classmethod
    def _missing_(cls, value):
        raise blad.BladTworzeniaMetrum(f'{value} nie jest prawidłową wartością dla {cls.__name__}')

    def podaj_pozadana_wartosc_nut_w_takcie(self) -> int:
        """
        Funkcja zwraca sumę wartości wartości nut wg typu WartosciNut dla każdego z przewidzianych metrum jako int
        """
        if self == Metrum.TRZY_CZWARTE:
            return 6
        elif self == Metrum.CZTERY_CZWARTE:
            return 8

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value
