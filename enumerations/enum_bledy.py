class BladListyAkordow(Exception):
    """
    Podnoszony, gdy problemem jest lista akordów zwracana przez instancję klasy Partytura, np. w razie problemu
    z indeksowaniem lub dwoma znakami końca taktu z rzędu.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Błąd listy akordów: {self.message}"


class BladWczytywaniaZPliku(Exception):
    """
    Podnoszony, gdy występują problemy na etapie wczytania z pliku partytury, np. nieprawidłowe wartości wprowadzanych
    nut, nieprawidłowe tonacje, nieprawidłowe metrum, ...
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Błąd wczytywania pliku: {self.message}"


class BladTworzeniaObiektu(Exception):
    """
    Klasa bazowa dla błędów podnoszonych podczas tworzenia innych obiektów (np. metrum, akord, ...)
    """

    def __init__(self, message):
        self.message = message


class BladTworzeniaPartytury(BladTworzeniaObiektu):
    """
    Błąd podnoszony w razie problemu z utworzeniem nowej partytury
    """

    def __str__(self):
        return f"Błąd tworzenia partytury : {self.message}"


class BladTworzeniaTonacji(BladTworzeniaObiektu):
    """
    Błąd w razie problemu z utworzeniem instancji Tonacji.
    Najbardziej prawdopodobna przyczyna to niepoprawna nazwa tonacji.
    """

    def __str__(self):
        return f"Błąd oznaczenia tonacji: {self.message}"


class BladTworzeniaMetrum(BladTworzeniaObiektu):
    """
    Błąd w razie problemu z utworzeniem instancji Metrum.
    Najbardziej prawdopodobna przyczyna to niepoprawna nazwa metrum.
    """

    def __str__(self):
        return f"Błąd oznaczenia metrum: {self.message}"


class BladTworzeniaDzwieku(BladTworzeniaObiektu):
    """
    Błąd w razie problemu z utworzeniem instancji Dzwiek.
    Podnoszone w razie problemu z nazwą dźwięku lub oktawą. .
    """

    def __str__(self):
        return f"Błąd tworzenia nowego dźwięku: {self.message}"


class BladTworzeniaAkordu(BladTworzeniaObiektu):
    """
    Błąd w razie problemu z utworzeniem instancji Akordu.
    Nie powinien występować, ale licho nie śpi.
    """

    def __str__(self):
        return f"Błąd tworzenia nowego akordu: {self.message}"


class BladDzwiekPozaTonacja(Exception):
    """
    Podnoszony, gdy dźwięk znajduje się poza tonacją (pewien dźwięk nie jest stopniem tonacji), a sprawdzamy jego
    przynależność do niej.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Dźwięk nie przynależy do tonacji. {self.message}"
