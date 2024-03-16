import unittest
import obsluga_plikow
import partytura
import tonacja
from enumerations import enum_metrum, enum_bledy

class TestyObslugiPlikow(unittest.TestCase):

    def test_utworz_partyture_1(self):
        """Sprawdza działanie metody utworz_partyture dla prawidłowych danych wejściowych"""
        with open("../przyklady/partytura_0.txt", "r") as plik:
            p1: partytura.Partytura = obsluga_plikow.utworz_partyture(plik)

        self.assertEqual(p1.podaj_tonacje().podaj_nazwe(), tonacja.Tonacja("C").podaj_nazwe())
        self.assertEqual(p1.podaj_zadeklarowana_liczbe_taktow(), 4)
        self.assertEqual(p1.podaj_metrum(), enum_metrum.Metrum("4/4"))

    def test_utworz_partyture_2(self):
        """Sprawdza, czy w braku oznaczenia tonacji zwracany jest odpowiedni wyjątek"""
        with open("../przyklady/partytura_1.txt", "r") as plik:
            self.assertRaises(enum_bledy.BladWczytywaniaZPliku, lambda: obsluga_plikow.utworz_partyture(plik))

    def test_utworz_partyture_3(self):
        """Sprawdza, czy w braku tonacji zwracany jest odpowiedni komunikat wyjątku"""
        with open("../przyklady/partytura_1.txt", "r") as plik:
            with self.assertRaises(enum_bledy.BladWczytywaniaZPliku) as context:
                obsluga_plikow.utworz_partyture(plik)
            self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Niepoprawna nazwa tonacji")

    def test_utworz_partyture_4(self):
        """Sprawdza, czy w braku oznaczonej liczby taktów zwracany jest odpowiedni wyjątek"""
        with open("../przyklady/partytura_2.txt", "r") as plik:
            self.assertRaises(enum_bledy.BladWczytywaniaZPliku, lambda: obsluga_plikow.utworz_partyture(plik))

    def test_utworz_partyture_5(self):
        """Sprawdza, czy w braku oznaczenia liczby taktów zwracany jest odpowiedni komunikat wyjątku"""
        with open("../przyklady/partytura_2.txt", "r") as plik:
            with self.assertRaises(enum_bledy.BladWczytywaniaZPliku) as context:
                obsluga_plikow.utworz_partyture(plik)
            self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Niepoprawna liczba taktów")

    def test_utworz_partyture_6(self):
        """Sprawdza, czy w razie nieodpowiedniej liczby taktów zwracany jest odpowiedni wyjątek"""
        with open("../przyklady/partytura_3.txt", "r") as plik:
            self.assertRaises(enum_bledy.BladWczytywaniaZPliku, lambda: obsluga_plikow.utworz_partyture(plik))

    def test_utworz_partyture_7(self):
        """Sprawdza, czy w braku metrum zwracany jest odpowiedni wyjątek i komunikat wyjątku"""
        with open("../przyklady/partytura_4.txt", "r") as plik:
            with self.assertRaises(enum_bledy.BladWczytywaniaZPliku) as context:
                obsluga_plikow.utworz_partyture(plik)
            self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Niepoprawne metrum")

    def test_utworz_partyture_7(self):
        """Sprawdza, czy w razie podania nieodpowiedniego metrum zwracany jest odpowiedni wyjątek i komunikat wyjątku"""
        with open("../przyklady/partytura_5.txt", "r") as plik:
            with self.assertRaises(enum_bledy.BladWczytywaniaZPliku) as context:
                obsluga_plikow.utworz_partyture(plik)
            self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Niepoprawne metrum")





