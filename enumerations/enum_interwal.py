import enum


class Interwal(enum.Enum):
    PRYMA_CZYSTA = '1'
    SEKUNDA_MALA = '2>'
    SEKUNDA_WIELKA = '2'
    TERCJA_MALA = '3>'
    TERCJA_WIELKA = '3'
    KWARTA_ZMNIEJSZONA = '4>'
    KWARTA_CZYSTA = '4'
    KWARTA_ZWIEKSZONA = '4<'
    KWINTA_ZMNIEJSZONA = '5>'
    KWINTA_CZYSTA = '5'
    KWINTA_ZWIEKSZONA = '5<'
    SEKSTA_MALA = '6>'
    SEKSTA_WIELKA = '6'
    SEPTYMA_ZMIEJSZONA = '7>'
    SEPTYMA_MALA = '7'
    SEPTYMA_WIELKA = '7<'
    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value

