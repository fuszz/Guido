import enum


class Funkcja(enum.Enum):
    """
    Typ wyliczeniowy przechowujący informację o dopuszczalnych w Guido funkcjach harmonicznych: tonice (moll tonice),
    subdominancie (moll subdominancie), dominancie, dominancie septymowej. Jeśli dźwięki nie stanowią żadnej z w/w
    funkcji, mamy błąd.
    """
    TONIKA = 'T'
    MOLL_TONIKA = 'mT'
    SUBDOMINANTA = 'S'
    MOLL_SUBDOMINANTA = 'mS'
    DOMINANTA = 'D'
    DOMINANTA_SEPTYMOWA = 'D7'
    BLAD = 'Błąd'
