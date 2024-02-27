import unittest
import akord
import dzwiek
import tonacja


class TestyKlasyAKord(unittest.TestCase):
    def test_zwroc_dlugosc_nuty(self):
        nowy_akord = akord.Akord(dzwiek.Dzwiek(2, 'c'), dzwiek.Dzwiek(2, 'c'), dzwiek.Dzwiek(2, 'c'), dzwiek.Dzwiek(2, 'c'), 3.0)
        self.assertEqual(nowy_akord.podaj_dlugosc(), wartosci_nut.WartosciNut.POLNUTA_Z_KROPKA)

    def test_ustal_funkcje_1(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_funkcje(tonacja.Tonacja('C')) == funkcje.Funkcja.SUBDOMINANTA)

    def test_ustal_funkcje_2(self):
        d_b = dzwiek.Dzwiek(2, 'c')
        d_t = dzwiek.Dzwiek(3, 'e')
        d_a = dzwiek.Dzwiek(4, 'g')
        d_s = dzwiek.Dzwiek(4, 'c')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_funkcje(tonacja.Tonacja('C')) == funkcje.Funkcja.TONIKA)

    def test_ustal_funkcje_3(self):
        d_b = dzwiek.Dzwiek(2, 'g')
        d_t = dzwiek.Dzwiek(3, 'h')
        d_a = dzwiek.Dzwiek(4, 'd')
        d_s = dzwiek.Dzwiek(4, 'g')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_funkcje(tonacja.Tonacja('C')) == funkcje.Funkcja.DOMINANTA)

    def test_ustal_funkcje_4(self):
        d_b = dzwiek.Dzwiek(2, 'g')
        d_t = dzwiek.Dzwiek(3, 'h')
        d_a = dzwiek.Dzwiek(4, 'd')
        d_s = dzwiek.Dzwiek(4, 'f')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_funkcje(tonacja.Tonacja('C')) == funkcje.Funkcja.DOMINANTA_SEPTYMOWA)

    def test_ustal_funkcje_5(self):
        d_b = dzwiek.Dzwiek(2, 'c')
        d_t = dzwiek.Dzwiek(3, 'eb')
        d_a = dzwiek.Dzwiek(4, 'g')
        d_s = dzwiek.Dzwiek(4, 'c')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_funkcje(tonacja.Tonacja('c')) == funkcje.Funkcja.MOLL_TONIKA)

    def test_ustal_funkcje_6(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'ab')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_funkcje(tonacja.Tonacja('c')) == funkcje.Funkcja.MOLL_SUBDOMINANTA)

    def test_ustal_funkcje_10(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'd')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertFalse(nowy_akord.ustal_funkcje(tonacja.Tonacja('C')) == funkcje.Funkcja.SUBDOMINANTA)

    def test_ustal_funkcje_11(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_funkcje(tonacja.Tonacja('F')) != funkcje.Funkcja.DOMINANTA)

    def test_ustal_przewrot_1(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_przewrot(tonacja.Tonacja('F')) == przewroty.Przewrot.POSTAC_ZASADNICZA)

    def test_ustal_przewrot_2(self):
        d_b = dzwiek.Dzwiek(2, 'a')
        d_t = dzwiek.Dzwiek(3, 'f')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_przewrot(tonacja.Tonacja('F')) == przewroty.Przewrot.PIERWSZY)

    def test_ustal_przewrot_3(self):
        d_b = dzwiek.Dzwiek(2, 'c')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'f')
        d_s = dzwiek.Dzwiek(4, 'f')

        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_przewrot(tonacja.Tonacja('F')) == przewroty.Przewrot.DRUGI)

    def test_ustal_przewrot_4(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_przewrot(tonacja.Tonacja('Hb')) == przewroty.Przewrot.POSTAC_ZASADNICZA)

    def test_ustal_przewrot_5(self):
        d_b = dzwiek.Dzwiek(2, 'f')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_przewrot(tonacja.Tonacja('hb')) == przewroty.Przewrot.POSTAC_ZASADNICZA)

    def test_ustal_przewrot_6(self):
        d_b = dzwiek.Dzwiek(2, 'd')
        d_t = dzwiek.Dzwiek(3, 'a')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_przewrot(tonacja.Tonacja('Hb')) == przewroty.Przewrot.NIE_ZDEFINIOWANO)

    def test_ustal_przewrot_7(self):
        d_b = dzwiek.Dzwiek(2, 'db')
        d_t = dzwiek.Dzwiek(3, 'ab')
        d_a = dzwiek.Dzwiek(4, 'c')
        d_s = dzwiek.Dzwiek(4, 'f')
        nowy_akord = akord.Akord(d_s, d_a, d_t, d_b, 1.0)
        self.assertTrue(nowy_akord.ustal_przewrot(tonacja.Tonacja('C')) == przewroty.Przewrot.NIE_ZDEFINIOWANO)


if __name__ == '__main__':
    unittest.main()
