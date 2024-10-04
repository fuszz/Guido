import enum


class WartosciNut(enum.Enum):
    """ Typ wyliczeniowy przypisuje poszczególnym wartościom nut liczby naturalne, które
    będą definiować długość ich trwania."""

    CALA_NUTA = 8
    POLNUTA_Z_KROPKA = 6
    POLNUTA = 4
    CWIERCNUTA_Z_KROPKA = 3
    CWIERCNUTA = 2
    OSEMKA = 1

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value
