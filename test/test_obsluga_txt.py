import unittest

import blad
import akord
import obsluga_txt as obsluga_plikow
import partytura
import tonacja
from enumerations import enum_metrum, enum_wartosci_nut


# DZIAŁA, NIE DOTYKAJ!!!!

class TestyObslugiPlikow(unittest.TestCase):

    def test_utworz_partyture_1(self):
        """Sprawdza działanie metody utworz_partyture dla prawidłowych danych wejściowych"""
        with open("../przyklady/txt/partytura_0.txt", "r") as plik:
            p1: partytura.Partytura = obsluga_plikow.utworz_partyture(plik)

        self.assertEqual(p1.podaj_tonacje().podaj_symbol(), tonacja.Tonacja.tonacja_z_symbolu("C").podaj_symbol())
        self.assertEqual(p1.podaj_zadeklarowana_liczbe_taktow(), 4)
        self.assertEqual(p1.podaj_metrum(), enum_metrum.Metrum("4/4"))

    def test_utworz_partyture_2(self):
        """Sprawdza, czy w braku oznaczenia tonacji zwracany jest odpowiedni wyjątek"""
        with open("../przyklady/txt/partytura_1.txt", "r") as plik:
            self.assertRaises(blad.BladWczytywaniaZPliku, lambda: obsluga_plikow.utworz_partyture(plik))

    def test_utworz_partyture_3(self):
        """Sprawdza, czy w braku tonacji zwracany jest odpowiedni komunikat wyjątku"""
        with open("../przyklady/txt/partytura_1.txt", "r") as plik:
            with self.assertRaises(blad.BladWczytywaniaZPliku) as context:
                obsluga_plikow.utworz_partyture(plik)
            self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Niepoprawna nazwa tonacji")

    def test_utworz_partyture_4(self):
        """Sprawdza, czy w braku oznaczonej liczby taktów zwracany jest odpowiedni wyjątek"""
        with open("../przyklady/txt/partytura_2.txt", "r") as plik:
            self.assertRaises(blad.BladWczytywaniaZPliku, lambda: obsluga_plikow.utworz_partyture(plik))

    def test_utworz_partyture_5(self):
        """Sprawdza, czy w braku oznaczenia liczby taktów zwracany jest odpowiedni komunikat wyjątku"""
        with open("../przyklady/txt/partytura_2.txt", "r") as plik:
            with self.assertRaises(blad.BladWczytywaniaZPliku) as context:
                obsluga_plikow.utworz_partyture(plik)
            self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Niepoprawna liczba taktów")

    def test_utworz_partyture_6(self):
        """Sprawdza, czy w razie nieodpowiedniej liczby taktów zwracany jest odpowiedni wyjątek"""
        with open("../przyklady/txt/partytura_3.txt", "r") as plik:
            self.assertRaises(blad.BladWczytywaniaZPliku, lambda: obsluga_plikow.utworz_partyture(plik))

    def test_utworz_partyture_7(self):
        """Sprawdza, czy w braku metrum zwracany jest odpowiedni wyjątek i komunikat wyjątku"""
        with open("../przyklady/txt/partytura_4.txt", "r") as plik:
            with self.assertRaises(blad.BladWczytywaniaZPliku) as context:
                obsluga_plikow.utworz_partyture(plik)
            self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Niepoprawne metrum")

    def test_utworz_partyture_8(self):
        """Sprawdza, czy w razie podania nieodpowiedniego metrum zwracany jest odpowiedni wyjątek i komunikat wyjątku"""
        with open("../przyklady/txt/partytura_5.txt", "r") as plik:
            with self.assertRaises(blad.BladWczytywaniaZPliku) as context:
                obsluga_plikow.utworz_partyture(plik)
            self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Niepoprawne metrum")

    def test_wypelnij_partyture_akordami_1(self):
        """Sprawdza, czy metoda obsluga_plikow.wypelnij_partyture_akordami() działa poprawnie dla prawidłowych danych"""
        with open("../przyklady/txt/partytura_6.txt", "r") as plik_wejsciowy:
            nowa_partytura: partytura.Partytura = obsluga_plikow.utworz_partyture(plik_wejsciowy)
            nowa_partytura = obsluga_plikow.wypelnij_partyture_akordami(plik_wejsciowy, nowa_partytura)
        self.assertEqual(nowa_partytura.podaj_liste_akordow()[0].podaj_dlugosc(), enum_wartosci_nut.WartosciNut(4))
        self.assertEqual(nowa_partytura.czy_poprawna_liczba_taktow(), True)
        self.assertEqual(nowa_partytura.podaj_liste_akordow()[-1], "T")
        self.assertEqual(isinstance(nowa_partytura.podaj_liste_akordow()[-2], akord.Akord), True)

    def test_wypelnij_partyture_akordami_2(self):
        """Sprawdza, czy metoda obsluga_plikow.wypelnij_partyture_akordami() zwraca odpowiedni wyjątek, gdy uszkodzone
        są dane dot. akordów : brak jednego z dźwięków"""
        with open("../przyklady/txt/partytura_7.txt", "r") as plik:
            with self.assertRaises(blad.BladWczytywaniaZPliku) as context:
                nowa_partytura: partytura.Partytura = obsluga_plikow.utworz_partyture(plik)
                nowa_partytura = obsluga_plikow.wypelnij_partyture_akordami(plik, nowa_partytura)
            self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Niepoprawny dźwięk w linii 4.")

    def test_wypelnij_partyture_akordami_3(self):
        """Sprawdza, czy metoda obsluga_plikow.wypelnij_partyture_akordami() zwraca odpowiedni wyjątek, gdy uszkodzone
        są dane dot. akordów: brak długości trwania akordu"""
        with open("../przyklady/txt/partytura_8.txt", "r") as plik:
            with self.assertRaises(blad.BladWczytywaniaZPliku) as context:
                nowa_partytura: partytura.Partytura = obsluga_plikow.utworz_partyture(plik)
                nowa_partytura = obsluga_plikow.wypelnij_partyture_akordami(plik, nowa_partytura)
            self.assertEqual(str(context.exception),
                             "Błąd wczytywania pliku: Niepoprawna długość dźwięku w linii 4.")

    def test_wczytaj_z_pliku_txt_1(self):
        """Sprawdza, czy metoda obsluga_plikow.wczytaj_z_pliku_txt() działa poprawnie dla poprawnych danych"""
        nowa_partytura = obsluga_plikow.wczytaj_z_pliku_txt("../przyklady/txt/partytura_6.txt")
        self.assertEqual(nowa_partytura.czy_poprawna_liczba_taktow(), True)
        self.assertEqual(nowa_partytura.podaj_tonacje().podaj_symbol(), tonacja.Tonacja.tonacja_z_symbolu("C").podaj_symbol())
        self.assertEqual(nowa_partytura.podaj_metrum().value, enum_metrum.Metrum("4/4").value)

    def test_wczytaj_z_pliku_txt_2(self):
        """Sprawdza, czy metoda obsluga_plikow.wczytaj_z_pliku_txt() podnosi odpowiednie wyjątki: brak wskazanego pliku"""
        with self.assertRaises(blad.BladWczytywaniaZPliku) as context:
            obsluga_plikow.wczytaj_z_pliku_txt("Sciezka_do_pliku_ktorego_nie_ma")
        self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Plik nie istnieje")

    def test_wczytaj_z_pliku_txt_3(self):
        """Sprawdza, czy metoda obsluga_plikow.wczytaj_z_pliku_txt() podnosi odpowiednie wyjątki: brak wskazanego pliku"""
        with self.assertRaises(blad.BladWczytywaniaZPliku) as context:
            obsluga_plikow.wczytaj_z_pliku_txt("../przyklady/txt/partytura_9.txt")
        self.assertEqual(str(context.exception), "Błąd wczytywania pliku: Błędna liczba taktów w partyturze")
