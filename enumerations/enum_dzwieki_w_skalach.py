import enum


class DzwiekiWSkalach(enum.Enum):
    """
    Typ wyliczeniowy używany do przekazania informacji, czy dźwięk znajduje się w skali danego głosu (0),  poniżej (-1)
    lub powyżej (1)  tej skali.
    """
    PONIZEJ_SKALI = -1
    W_SKALI = 0
    POWYZEJ_SKALI = 1

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value