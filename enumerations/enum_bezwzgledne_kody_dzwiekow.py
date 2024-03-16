import enum


class BezwzgledneKodyDzwiekow(enum.Enum):
    "Typ wyliczeniowy, za pomocą którego wyliczane są bezwzględne kody dźwięków."
    C = 0
    D = 2
    E = 4
    F = 5
    G = 7
    A = 9
    H = 11

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.value == other.value