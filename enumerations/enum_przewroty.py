import enum


class Przewrot(enum.Enum):
    """ Typ wyliczeniowy przechowuje informację o przewrocie: 0 - post. zasadnicza, 1 - 1. przewrót, 2 - 2. przewrót,
    3 - 3. przewrót.
    """
    POSTAC_ZASADNICZA = 0
    PIERWSZY = 1
    DRUGI = 2
    TRZECI = 3

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value
