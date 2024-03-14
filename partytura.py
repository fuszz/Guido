import tonacja
import akord
from enumerations import enum_metrum, enum_bledy
from typing import List, Union


# Napisane docstringi - 14.03.2024

class Partytura:

    def __init__(self, nowa_tonacja: tonacja.Tonacja, nowe_metrum: enum_metrum.Metrum, nowa_liczba_taktow: int):
        """
        Tworzy nową instancję obiektu klasy Partytura.
        :param nowa_tonacja: tonacja.Tonacja -> obiekt typu enumeracyjnego Tonacja
        :param nowe_metrum: enum_metrum.Metrum -> obiekt typu enumeracyjnego Metrum
        :param nowa_liczba_taktow: int -> liczba taktów, które powinna zawierać partytura. Jeśli faktyczna liczba taktów
         będzie inna, zostanie potem podniesiony wyjątek enum_bledy.BladListyAkordow
        """

        if not (isinstance(nowa_tonacja, tonacja.Tonacja) and isinstance(nowe_metrum, enum_metrum.Metrum)
                and isinstance(nowa_liczba_taktow, int)):
            raise enum_bledy.BladTworzeniaPartytury("Sprawdź, czy tworzysz partyturę z poprawnych elementów")
        if nowa_liczba_taktow < 1:
            raise enum_bledy.BladTworzeniaPartytury("Zadeklarowano niepoprawną liczbę taktów - mniejszą niż 1")

        self._lista_akordow: List[Union[akord.Akord, str]] = []
        self._tonacja: tonacja.Tonacja = nowa_tonacja
        self._metrum: enum_metrum.Metrum = nowe_metrum
        self._liczba_taktow: int = nowa_liczba_taktow

    def podaj_metrum(self) -> enum_metrum.Metrum:
        """
        Podaje metrum partytury. Nie sprawdza, czy akordy są faktycznie utrzymane w tym metrum.
        :return: metrum.Metrum <- instancja enuma Metrum.
        """
        return self._metrum

    def podaj_tonacje(self) -> tonacja.Tonacja:
        """
        Podaje tonację partytury. Nie sprawdza, czy akordy są utrzymane w tej tonacji.
        :return: tonacja.Tonacja <- instancja enuma Tonacja.
        """
        return self._tonacja

    def podaj_zadeklarowana_liczbe_taktow(self) -> int:
        """
        Podaje zadeklarowaną liczbę taktów w partyturze. Może być różna od obecnej długości listy.
        :return: int - zadeklarowana liczba taktów
        """
        return self._liczba_taktow

    def podaj_rzeczywista_liczbe_taktow(self) -> int:
        """
        Podaje obecną liczbę taktów w partyturze.
        :return: int <- liczba taktów
        """
        return self._lista_akordow.count('T')

    def dodaj_akord(self, nowy_akord: akord.Akord) -> None:
        """
        Funkcja dodaje akord podany w swoim argumencie na koniec listy akordów.
        Nie sprawdza, czy takt ma jeszcze miejsce.
        :return: None
        """
        self._lista_akordow.append(nowy_akord)

    def zakoncz_takt(self) -> None:
        """
        Funkcja dopisuje 'T' na koniec obecnej listy akordów.
        Nie sprawdza, czy takt jest kompletny (zawiera odpowiednią sumę wartości taktów).
        :return: None
        """
        self._lista_akordow.append('T')

    def czy_poprawna_liczba_taktow(self) -> bool:
        """True, jeśli poprawna liczba znaków końca taktu (T)"""
        if self._liczba_taktow == self._lista_akordow.count('T'):
            return True
        else:
            return False

    def podaj_liste_akordow(self) -> List[Union[akord.Akord, str]]:
        """
        Zwraca obecną zawartość zmiennych self._lista_akordow: lista obiektów klasy akord
        i liter 'T' - znaczniki końca taktu
        :return: List[Union[akord.Akord, str]]
        """
        return self._lista_akordow

    # Na potrzeby moich testów:
    def wyswietl_liste_akordow(self):
        for element in self._lista_akordow:
            if element == 'T':
                print("Koniec taktu")
            else:
                element.wyswietl_akord()
