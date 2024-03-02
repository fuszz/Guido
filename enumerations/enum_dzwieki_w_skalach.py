import enum


class DzwiekiWSkalach(enum.Enum):
    """
    Typ wyliczeniowy używany do przekazania informacji, czy dźwięk znajduje się w skali danego głosu (1),
    lub poniżej-0 (powyżej-2) tej skali.
    """
    PONIZEJ_SKALI = 0
    W_SKALI = 1
    POWYZEJ_SKALI = 2
