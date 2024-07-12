import unittest
import dzwiek
import tonacja
from enumerations import enum_nazwy_dzwiekow
import blad


# Testy są ok - 14.03.2024

class MyTestCase(unittest.TestCase):
    def test_konstruktora_1(self):
        d1 = dzwiek.Dzwiek(1, "c")
        self.assertEqual(d1.podaj_nazwe().value, "c")
        self.assertEqual(d1.podaj_oktawe(), 1)

    def test_konstruktora_2(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            dzwiek.Dzwiek(2, 'cbbb')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna nazwa")

    def test_konstruktora_3(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            dzwiek.Dzwiek(2, '###')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna nazwa")

    def test_konstruktora_4(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            dzwiek.Dzwiek(10, 'c')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna oktawa")

    def test_konstruktora_5(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            dzwiek.Dzwiek("###", 'c')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna oktawa")

    def test_konstruktora_6(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            dzwiek.Dzwiek(-100, 'c')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna oktawa")

    def test_podaj_oktawe1(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_oktawe(), 1)

    def test_podaj_nazwe_dzwieku1(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_nazwe(), enum_nazwy_dzwiekow.NazwyDzwiekow("d"))

    def test_podaj_swoj_stopien_1(self):
        d = dzwiek.Dzwiek(1, 'c')
        self.assertEqual(d.podaj_stopien_w_tonacji(tonacja.Tonacja.stworz_z_symbolu('C')), 0)

    def test_podaj_swoj_stopien_2(self):
        d = dzwiek.Dzwiek(1, 'c#')
        self.assertRaises(blad.BladDzwiekPozaTonacja,
                          lambda: d.podaj_stopien_w_tonacji(tonacja.Tonacja.stworz_z_symbolu('C')))

    def test_kodu_midi_1(self):
        d1 = dzwiek.Dzwiek(1, 'c##')
        d2 = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d1.podaj_kod_midi(), d2.podaj_kod_midi())

    def test_kodu_bezwzglednego_2(self):
        d1 = dzwiek.Dzwiek(1, 'c##')
        d2 = dzwiek.Dzwiek(1, 'db')
        self.assertNotEqual(d1.podaj_kod_midi(), d2.podaj_kod_midi())

    def test_kodu_midi_3(self):
        d1 = dzwiek.Dzwiek(1, 'c')
        self.assertEqual(d1.podaj_kod_midi(), 24)

    def test_kodu_midi_4(self):
        d1 = dzwiek.Dzwiek(1, 'c#')
        self.assertEqual(d1.podaj_kod_midi(), 25)

    def test_kodu_midi_5(self):
        d1 = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d1.podaj_kod_midi(), 26)

    def test_kodu_midi_6(self):
        d1 = dzwiek.Dzwiek(2, 'cb')
        self.assertEqual(d1.podaj_kod_midi(), 35)

    def test_kodu_midi_7(self):
        d1 = dzwiek.Dzwiek(2, 'c')
        self.assertEqual(d1.podaj_kod_midi(), 36)


if __name__ == '__main__':
    unittest.main()
