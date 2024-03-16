import enum


class Interwal(enum.Enum):
    """
    Typ enumeracyjny zwracający odpowiednie interwały, występujące naturalnie między stopniami skali durowej naturalnej
    i mollowej harmonicznej.
    """
    PRYMA_CZYSTA = (0, '1')
    SEKUNDA_MALA = (1, '2>')
    SEKUNDA_WIELKA = (2, '2')
    SEKUNDA_ZWIEKSZONA = (3, '2<')
    TERCJA_MALA = (3, '3>')
    TERCJA_WIELKA = (4, '3')
    KWARTA_CZYSTA = (5, '4')
    KWARTA_ZWIEKSZONA = (6, '4<')
    KWINTA_ZMNIEJSZONA = (6, '5>')
    KWINTA_CZYSTA = (7, '5')
    KWINTA_ZWIEKSZONA = (8, '5<')
    SEKSTA_MALA = (8, '6>')
    SEKSTA_WIELKA = (9, '6')
    SEPTYMA_MALA = (10, '7')
    SEPTYMA_WIELKA = (11, '7<')
    OKTAWA = (12, '8')

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value

    @classmethod
    def interwal_z_odleglosci(cls, odleglosc_miedzy_poltonami: int):
        for interwal in cls:
            if interwal.value[0] == odleglosc_miedzy_poltonami:
                return interwal
        raise ValueError("Nie ma interwału o podanej przez Ciebie odległości")

