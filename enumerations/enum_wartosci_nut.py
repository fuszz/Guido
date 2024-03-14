import enum


class WartosciNut(enum.Enum):
    """ Typ wyliczeniowy przypisuje poszczególnym wartościom nut liczby naturalne całkowite, które na potrzeby naszego
    programu będą definiować długość ich trwania."""
    CALA_NUTA = 8
    POLNUTA_Z_KROPKA = 6
    POLNUTA = 4
    CWIERCNUTA_Z_KROPKA = 3
    CWIERCNUTA = 2
    OSEMKA = 1
