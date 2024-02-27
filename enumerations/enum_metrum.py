import enum


class Metrum(enum.Enum):
    TRZY_CZWARTE = '3/4'
    CZTERY_CZWARTE = '4/4'

    def podaj_pozadana_wartosc_nut_w_takcie(self):
        if self == Metrum.TRZY_CZWARTE:
            return 6
        elif self == Metrum.CZTERY_CZWARTE:
            return 8
        else:
            return ValueError