import enum


class KrzyzowaniaGlosow(enum.Enum):
    """
    Typ enumeracyjny zwracający informację nt. krzyżowania się głosów w przejściach między akordami.
    """
    SOPRAN_I_ALT = 12
    SOPRAN_I_TENOR = 13
    SOPRAN_I_BAS = 14
    ALT_I_TENOR = 23
    ALT_I_BAS = 24
    TENOR_I_BAS = 34

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value