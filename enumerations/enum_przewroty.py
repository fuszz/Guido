import enum


class Przewrot(enum.Enum):
    """ Typ wyliczeniowy przechowuje informację o przewrocie: 0 - post. zasadnicza, 1 - 1. przewrót, 2 - 2. przewrót,
    3 - 3. przewrót, -1 - gdy dźwięki nie są poprawnym akordem i przewrót nie jest możliwy do określenia.
    """
    POSTAC_ZASADNICZA = 0
    PIERWSZY = 1
    DRUGI = 2
    TRZECI = 3
    NIE_ZDEFINIOWANO = -1
