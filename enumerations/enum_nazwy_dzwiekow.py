import enum


class NazwyDzwiekow(enum.Enum):
    """
    Typ wyliczeniowy, wiąże nazwy dźwięków w języku naturalnym z tymi w konwencji przyjętej dla Guido'a
    """
    CESES = 'cbb'
    CES = 'cb'
    C = 'c'
    CIS = 'c#'
    CISIS = 'c##'

    DESES = 'dbb'
    DES = 'db'
    D = 'd'
    DIS = 'd#'
    DISIS = 'd##'

    ESES = 'ebb'
    ES = 'eb'
    E = 'e'
    EIS = 'e#'
    EISIS = 'e##'

    FESES = 'fbb'
    FES = 'fb'
    F = 'f'
    FIS = 'f#'
    FISIS = 'f##'

    GESES = 'gbb'
    GES = 'gb'
    G = 'g'
    GIS = 'g#'
    GISIS = 'g##'

    ASAS = 'abb'
    AS = 'ab'
    A = 'a'
    AIS = 'a#'
    AISIS = 'a##'

    HESES = 'hbb'
    B = 'hb'
    H = 'h'
    HIS = 'h#'
    HISIS = 'h##'

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value
