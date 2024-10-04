import unittest
import funkcja as f
import blad
from enumerations import enum_przewroty, enum_skladnik_funkcji, enum_zdwojony_skladnik_funkcji


class TestyFunkcja(unittest.TestCase):
    def test_konstruktora_1(self):
        """Sprawdza poprawność działania stałej metody Funkcja.funkcja_z_listy_stopni
        dla poprawnych danych"""
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([2, 2, 0, 4], True), f.Funkcja.TONIKA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([0, 2, 0, 4], True), f.Funkcja.TONIKA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([0, 2, 0, 4], False), f.Funkcja.MOLL_TONIKA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([4, 2, 4, 0], False), f.Funkcja.MOLL_TONIKA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([3, 5, 0, 5], True), f.Funkcja.SUBDOMINANTA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([5, 3, 3, 0], True), f.Funkcja.SUBDOMINANTA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([3, 5, 0, 5], False), f.Funkcja.MOLL_SUBDOMINANTA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([5, 3, 3, 0], False), f.Funkcja.MOLL_SUBDOMINANTA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([4, 6, 1, 4], False), f.Funkcja.DOMINANTA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([6, 6, 4, 1], False), f.Funkcja.DOMINANTA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([4, 6, 1, 4], True), f.Funkcja.DOMINANTA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([6, 6, 4, 1], True), f.Funkcja.DOMINANTA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([3, 6, 1, 4], False), f.Funkcja.DOMINANTA_SEPTYMOWA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([3, 6, 4, 1], False), f.Funkcja.DOMINANTA_SEPTYMOWA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([3, 6, 1, 4], True), f.Funkcja.DOMINANTA_SEPTYMOWA)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([3, 6, 4, 1], True), f.Funkcja.DOMINANTA_SEPTYMOWA)

    def test_konstruktora_2(self):
        """Sprawdza poprawność działania metody Funkcja.funkcja_z_listy_stopni
        dla niepoprawnych danych: niepoprawny typ elementów listy stopni"""
        self.assertRaises(blad.BladTworzeniaFunkcji,
                          lambda: f.Funkcja.funkcja_z_listy_stopni(["b", "a", -10, '\t'], True))

    def test_konstruktora_3(self):
        """Sprawdza poprawność działania metody Funkcja.funkcja_z_listy_stopni
        dla niepoprawnych danych: czy_dur jako nie-bool"""
        self.assertRaises(blad.BladTworzeniaFunkcji, lambda: f.Funkcja.funkcja_z_listy_stopni([0, 2, 2, 4], "O"))

    def test_konstruktora_4(self):
        """Sprawdza poprawność działania metody Funkcja.funkcja_z_listy_stopni
        dla niepoprawnych danych: czy_dur jako nie-bool"""
        self.assertRaises(blad.BladTworzeniaFunkcji, lambda: f.Funkcja.funkcja_z_listy_stopni([0, 2, -7, 4], False))

    def test_konstruktora_5(self):
        """Sprawdza poprawność działania metody Funkcja.funkcja_z_listy_stopni
        dla niepoprawnych danych: choć podane są poprawne argumenty, to lista stopni nie opisuje żadnej funkcji"""
        with self.assertRaises(blad.BladStopienPozaFunkcja) as context:
            f.Funkcja.funkcja_z_listy_stopni([0, 1, 2, 3], False)
        self.assertEqual(str(context.exception), "Podane stopnie nie są funkcją")

    def test_konstruktora_6(self):
        """Sprawdza poprawność działania metody Funkcja.funkcja_z_listy_stopni
        dla niepoprawnych danych: choć podane są poprawne argumenty, to lista stopni nie opisuje żadnej funkcji"""
        with self.assertRaises(blad.BladStopienPozaFunkcja) as context:
            f.Funkcja.funkcja_z_listy_stopni([0, 2, 2, 0], False)
        self.assertEqual(str(context.exception), "Podane stopnie nie są funkcją")

    def test_konstruktora_7(self):
        """Sprawdza poprawność działania metody Funkcja.funkcja_z_listy_stopni
        dla niepoprawnych danych: choć podane są poprawne argumenty, to lista stopni nie opisuje żadnej funkcji"""
        with self.assertRaises(blad.BladStopienPozaFunkcja) as context:
            f.Funkcja.funkcja_z_listy_stopni([3, 3, 3, 1], False)
        self.assertEqual(str(context.exception), "Podane stopnie nie są funkcją")

    def test_stopien_tonacji_w_skladnik_funkcji(self):
        """ Testuje metodę dla poprawnych danych """
        self.assertEqual(f.Funkcja.TONIKA.stopien_tonacji_w_skladnik(0),
                         enum_skladnik_funkcji.SkladnikFunkcji.PRYMA)
        self.assertEqual(f.Funkcja.MOLL_TONIKA.stopien_tonacji_w_skladnik(0),
                         enum_skladnik_funkcji.SkladnikFunkcji.PRYMA)
        self.assertEqual(f.Funkcja.DOMINANTA.stopien_tonacji_w_skladnik(1),
                         enum_skladnik_funkcji.SkladnikFunkcji.KWINTA)
        self.assertEqual(f.Funkcja.DOMINANTA_SEPTYMOWA.stopien_tonacji_w_skladnik(3),
                         enum_skladnik_funkcji.SkladnikFunkcji.SEPTYMA)

    def test_stopien_tonacji_w_skladnik_funkcji_bledy(self):
        """ Sprawdza działanie metody dla niepoprawnych danych wejściowych:
            1. Niepoprawny typ stopien_basu
            2. Wartości stopien_basu, które nie występują w przywoływanej funkcji"""

        with self.assertRaises(blad.BladNiepoprawneArgumenty) as context:
            f.Funkcja.TONIKA.stopien_tonacji_w_skladnik("a")
        self.assertEqual(str(context.exception), "Niepoprawne argumenty: funkcja.okresl_przewrot():"
                                                 " stopień musi być intem")

        with self.assertRaises(blad.BladNiepoprawneArgumenty) as context:
            f.Funkcja.TONIKA.stopien_tonacji_w_skladnik(1.0)
        self.assertEqual(str(context.exception), "Niepoprawne argumenty: funkcja.okresl_przewrot():"
                                                 " stopień musi być intem")

        with self.assertRaises(blad.BladNiepoprawneArgumenty) as context:
            f.Funkcja.TONIKA.stopien_tonacji_w_skladnik(100)
        self.assertEqual(str(context.exception), "Niepoprawne argumenty: funkcja.okresl_przewrot():"
                                                 " stopień musi być w [0, 6]")

        with self.assertRaises(blad.BladStopienPozaFunkcja) as context:
            f.Funkcja.TONIKA.stopien_tonacji_w_skladnik(3)
        self.assertEqual(str(context.exception), "3 nie należy do funkcji T")

        with self.assertRaises(blad.BladStopienPozaFunkcja) as context:
            f.Funkcja.DOMINANTA.okresl_przewrot(3)
        self.assertEqual(str(context.exception), "3 nie należy do funkcji D")

    def test_czy_dur(self):
        """Sprawdza poprawność działania metody czy_dur()"""
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([2, 2, 0, 4], True).czy_dur(), True)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([0, 2, 0, 4], False).czy_dur(), False)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([5, 3, 3, 0], True).czy_dur(), True)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([5, 3, 3, 0], False).czy_dur(), False)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([4, 6, 1, 4], False).czy_dur(), True)
        self.assertEqual(f.Funkcja.funkcja_z_listy_stopni([3, 6, 1, 4], False).czy_dur(), True)

    def test_okresl_przewrot_T_mT(self):
        self.assertEqual(f.Funkcja.TONIKA.okresl_przewrot(0), enum_przewroty.Przewrot.POSTAC_ZASADNICZA)
        self.assertEqual(f.Funkcja.MOLL_TONIKA.okresl_przewrot(0), enum_przewroty.Przewrot.POSTAC_ZASADNICZA)

        self.assertEqual(f.Funkcja.TONIKA.okresl_przewrot(2), enum_przewroty.Przewrot.PIERWSZY)
        self.assertEqual(f.Funkcja.MOLL_TONIKA.okresl_przewrot(2), enum_przewroty.Przewrot.PIERWSZY)

        self.assertEqual(f.Funkcja.TONIKA.okresl_przewrot(4), enum_przewroty.Przewrot.DRUGI)
        self.assertEqual(f.Funkcja.MOLL_TONIKA.okresl_przewrot(4), enum_przewroty.Przewrot.DRUGI)

    def test_okresl_przewrot_S_mS(self):
        self.assertEqual(f.Funkcja.SUBDOMINANTA.okresl_przewrot(3), enum_przewroty.Przewrot.POSTAC_ZASADNICZA)
        self.assertEqual(f.Funkcja.MOLL_SUBDOMINANTA.okresl_przewrot(3), enum_przewroty.Przewrot.POSTAC_ZASADNICZA)

        self.assertEqual(f.Funkcja.SUBDOMINANTA.okresl_przewrot(5), enum_przewroty.Przewrot.PIERWSZY)
        self.assertEqual(f.Funkcja.MOLL_SUBDOMINANTA.okresl_przewrot(5), enum_przewroty.Przewrot.PIERWSZY)

        self.assertEqual(f.Funkcja.SUBDOMINANTA.okresl_przewrot(0), enum_przewroty.Przewrot.DRUGI)
        self.assertEqual(f.Funkcja.MOLL_SUBDOMINANTA.okresl_przewrot(0), enum_przewroty.Przewrot.DRUGI)

    def test_okresl_przewrot_D(self):
        self.assertEqual(f.Funkcja.DOMINANTA.okresl_przewrot(4), enum_przewroty.Przewrot.POSTAC_ZASADNICZA)
        self.assertEqual(f.Funkcja.DOMINANTA.okresl_przewrot(6), enum_przewroty.Przewrot.PIERWSZY)
        self.assertEqual(f.Funkcja.DOMINANTA.okresl_przewrot(1), enum_przewroty.Przewrot.DRUGI)

    def test_okresl_przewrot_D7(self):
        self.assertEqual(f.Funkcja.DOMINANTA_SEPTYMOWA.okresl_przewrot(4), enum_przewroty.Przewrot.POSTAC_ZASADNICZA)
        self.assertEqual(f.Funkcja.DOMINANTA_SEPTYMOWA.okresl_przewrot(6), enum_przewroty.Przewrot.PIERWSZY)
        self.assertEqual(f.Funkcja.DOMINANTA_SEPTYMOWA.okresl_przewrot(1), enum_przewroty.Przewrot.DRUGI)
        self.assertEqual(f.Funkcja.DOMINANTA_SEPTYMOWA.okresl_przewrot(3), enum_przewroty.Przewrot.TRZECI)

    def test_okresl_przewrot_bledy(self):
        """ Sprawdza działanie metody funkcja.okresl_przewrot dla niepoprawnych danych wejściowych:
            1. Niepoprawny typ stopien_basu
            2. Wartości stopien_basu, które nie występują w przywoływanej funkcji"""

        with self.assertRaises(blad.BladNiepoprawneArgumenty) as context:
            f.Funkcja.TONIKA.okresl_przewrot("a")
        self.assertEqual(str(context.exception), "Niepoprawne argumenty: funkcja.okresl_przewrot():"
                                                 " stopień musi być intem")

        with self.assertRaises(blad.BladNiepoprawneArgumenty) as context:
            f.Funkcja.TONIKA.okresl_przewrot(1.0)
        self.assertEqual(str(context.exception), "Niepoprawne argumenty: funkcja.okresl_przewrot():"
                                                 " stopień musi być intem")

        with self.assertRaises(blad.BladNiepoprawneArgumenty) as context:
            f.Funkcja.TONIKA.okresl_przewrot(100)
        self.assertEqual(str(context.exception), "Niepoprawne argumenty: funkcja.okresl_przewrot():"
                                                 " stopień musi być w [0, 6]")

        with self.assertRaises(blad.BladStopienPozaFunkcja) as context:
            f.Funkcja.TONIKA.okresl_przewrot(3)
        self.assertEqual(str(context.exception), "3 nie należy do funkcji T")

        with self.assertRaises(blad.BladStopienPozaFunkcja) as context:
            f.Funkcja.MOLL_TONIKA.okresl_przewrot(3)
        self.assertEqual(str(context.exception), "3 nie należy do funkcji mT")

    def test_dwojenie_jako_skladnik_funkcji(self):
        self.assertEqual(f.Funkcja.TONIKA.podaj_dwojenie_jako_skladnik(0),
                         enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.PRYMA)
        self.assertEqual(f.Funkcja.MOLL_SUBDOMINANTA.podaj_dwojenie_jako_skladnik(0),
                         enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.KWINTA)
        self.assertEqual(f.Funkcja.DOMINANTA_SEPTYMOWA.podaj_dwojenie_jako_skladnik(0),
                         enum_zdwojony_skladnik_funkcji.ZdwojonySkladnikFunkcji.BRAK)

    def test_dwojenie_jako_skladnik_funkcji_bledy(self):
        with self.assertRaises(blad.BladNiepoprawneArgumenty) as context:
            f.Funkcja.TONIKA.podaj_dwojenie_jako_skladnik("a")
        self.assertEqual(str(context.exception), "Niepoprawne argumenty: funkcja.okresl_przewrot():"
                                                 " stopień musi być intem")

        with self.assertRaises(blad.BladNiepoprawneArgumenty) as context:
            f.Funkcja.TONIKA.podaj_dwojenie_jako_skladnik(10)
        self.assertEqual(str(context.exception), "Niepoprawne argumenty: funkcja.okresl_przewrot():"
                                                 " stopień musi być w [0, 6]")
        with self.assertRaises(blad.BladStopienPozaFunkcja) as context:
            f.Funkcja.TONIKA.podaj_dwojenie_jako_skladnik(3)
        self.assertEqual(str(context.exception), "3 nie należy do funkcji T")

        with self.assertRaises(blad.BladStopienPozaFunkcja) as context:
            f.Funkcja.TONIKA.podaj_dwojenie_jako_skladnik(5)
        self.assertEqual(str(context.exception), "5 nie należy do funkcji T")


if __name__ == '__main__':
    unittest.main()
