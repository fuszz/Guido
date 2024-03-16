import enum


class NazwyDzwiekow(enum.Enum):
    """
    Typ wyliczeniowy, wiąże nazwy dźwięków w języku naturalnym z tymi w konwencji przyjętej dla Guido'a
    """
    CES = 'cb'
    C = 'c'
    CIS = 'c#'
    CISIS = 'c##'
    DES = 'db'
    D = 'd'
    DIS = 'd#'
    ES = 'eb'
    E = 'e'
    EIS = 'e#'
    FES = 'fb'
    F = 'f'
    FIS = 'f#'
    FISIS = 'f##'
    GES = 'gb'
    G = 'g'
    GIS = 'g#'
    GISIS = 'g##'
    AS = 'ab'
    A = 'a'
    AIS = 'a#'
    B = 'hb'
    H = 'h'
    HIS = 'h#'

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value