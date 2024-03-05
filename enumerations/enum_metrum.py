import enum
from enumerations import enum_bledy
class Metrum(enum.Enum):
    """Typ wyliczeniowy przechowujący wartości metrum. Ograniczamy się do 3/4 i 4/4"""
    TRZY_CZWARTE = '3/4'
    CZTERY_CZWARTE = '4/4'

    def _missing_(cls, value):
        raise enum_bledy.BladTworzeniaMetrum(f'{value} nie jest prawidłową wartością dla {cls.__name__}')

    def podaj_pozadana_wartosc_nut_w_takcie(self) -> int:
        """
        Funkcja zwraca sumę wartości wartości nut wg typu WartosciNut dla każdego z przewidzianych metrum jako int
        """
        if self == Metrum.TRZY_CZWARTE:
            return 6
        elif self == Metrum.CZTERY_CZWARTE:
            return 8

