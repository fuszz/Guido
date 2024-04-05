import unittest
import dzwiek
import tonacja
from enumerations import enum_nazwy_dzwiekow
import blad


# Testy są ok - 14.03.2024

class MyTestCase(unittest.TestCase):
    def test_konstruktora_1(self):
        d1 = dzwiek.Dzwiek(1, "c")
        self.assertEqual(d1.podaj_nazwe_dzwieku().value, "c")
        self.assertEqual(d1.podaj_oktawe(), 1)

    def test_konstruktora_2(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            d = dzwiek.Dzwiek(2, 'cbbb')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna nazwa")

    def test_konstruktora_3(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            d = dzwiek.Dzwiek(2, '###')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna nazwa")

    def test_konstruktora_4(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            d = dzwiek.Dzwiek(10, 'c')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna oktawa")

    def test_konstruktora_5(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            d = dzwiek.Dzwiek("###", 'c')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna oktawa")

    def test_konstruktora_6(self):
        with self.assertRaises(blad.BladTworzeniaDzwieku) as context:
            d = dzwiek.Dzwiek(-100, 'c')
        self.assertEqual(str(context.exception), "Błąd tworzenia dźwięku: Niepoprawna oktawa")

    def test_dzwiek_z_kodu_midi_w_podanej_tonacji(self):
        CIS_DUR = ['c#', 'd#', 'e#', 'f#', 'g#', 'a#', 'h#']
        CES_DUR = ['cb', 'db', 'eb', 'fb', 'gb', 'ab', 'hb']
        C_DUR = ['c', 'd', 'e', 'f', 'g', 'a', 'h']
        AS_MOLL = ['ab', 'hb', 'cb', 'db', 'eb', 'fb', 'g']
        A_MOLL = ['a', 'h', 'c', 'd', 'e', 'f', 'g#']
        AIS_MOLL = ['a#', 'h#', 'c#', 'd#', 'e#', 'f#', 'g##']

        for i in range(0, 9):
            for j in range(0, 7):
                self.assertEqual(dzwiek.Dzwiek(i, CIS_DUR[j]), dzwiek.Dzwiek.dzwiek_z_kodu_midi(tonacja.Tonacja.CIS_DUR, dzwiek.Dzwiek(i, CIS_DUR[j]).podaj_swoj_kod_midi()))
                self.assertEqual(dzwiek.Dzwiek(i, CES_DUR[j]), dzwiek.Dzwiek.dzwiek_z_kodu_midi(tonacja.Tonacja.CES_DUR, dzwiek.Dzwiek(i, CES_DUR[j]).podaj_swoj_kod_midi()))
                self.assertEqual(dzwiek.Dzwiek(i, C_DUR[j]), dzwiek.Dzwiek.dzwiek_z_kodu_midi(tonacja.Tonacja.C_DUR, dzwiek.Dzwiek(i, C_DUR[j]).podaj_swoj_kod_midi()))
                self.assertEqual(dzwiek.Dzwiek(i, AS_MOLL[j]), dzwiek.Dzwiek.dzwiek_z_kodu_midi(tonacja.Tonacja.AS_MOLL, dzwiek.Dzwiek(i, AS_MOLL[j]).podaj_swoj_kod_midi()))
                self.assertEqual(dzwiek.Dzwiek(i, AIS_MOLL[j]), dzwiek.Dzwiek.dzwiek_z_kodu_midi(tonacja.Tonacja.AIS_MOLL, dzwiek.Dzwiek(i, AIS_MOLL[j]).podaj_swoj_kod_midi()))
                self.assertEqual(dzwiek.Dzwiek(i, A_MOLL[j]), dzwiek.Dzwiek.dzwiek_z_kodu_midi(tonacja.Tonacja.A_MOLL, dzwiek.Dzwiek(i, A_MOLL[j]).podaj_swoj_kod_midi()))



    def test_podaj_oktawe1(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_oktawe(), 1)

    def test_podaj_nazwe_dzwieku1(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_nazwe_dzwieku(), enum_nazwy_dzwiekow.NazwyDzwiekow("d"))

    def test_podaj_swoj_stopien_1(self):
        d = dzwiek.Dzwiek(1, 'c')
        self.assertEqual(d.podaj_swoj_stopien(tonacja.Tonacja.tonacja_z_symbolu('C')), 0)

    def test_podaj_swoj_stopien_2(self):
        d = dzwiek.Dzwiek(1, 'c#')
        self.assertRaises(blad.BladDzwiekPozaTonacja,
                          lambda: d.podaj_swoj_stopien(tonacja.Tonacja.tonacja_z_symbolu('C')))

    def test_podaj_swoj_kod_wzgledny_1(self):
        d = dzwiek.Dzwiek(1, 'c#')
        self.assertRaises(blad.BladDzwiekPozaTonacja,
                          lambda: d.podaj_swoj_kod_wzgledny(tonacja.Tonacja.tonacja_z_symbolu('C')))

    def test_podaj_swoj_kod_wzgledny_2(self):
        d = dzwiek.Dzwiek(1, 'fb')
        self.assertRaises(blad.BladDzwiekPozaTonacja,
                          lambda: d.podaj_swoj_kod_wzgledny(tonacja.Tonacja.tonacja_z_symbolu('C')))

    def test_podaj_swoj_kod_3(self):
        d = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d.podaj_swoj_kod_wzgledny(tonacja.Tonacja.tonacja_z_symbolu('C')), 8)

    def test_spojnosci_oktawy_i_kodu_wzglednego_1(self):
        d = dzwiek.Dzwiek(2, 'd')
        self.assertEqual(d.podaj_oktawe(), d.podaj_swoj_kod_wzgledny(tonacja.Tonacja.tonacja_z_symbolu('C')) // 7)

    def test_spojnosci_oktawy_i_kodu_wzglednego_2(self):
        d = dzwiek.Dzwiek(2, 'd')
        self.assertEqual(d.podaj_swoj_stopien(tonacja.Tonacja.tonacja_z_symbolu('C')),
                         d.podaj_swoj_kod_wzgledny(tonacja.Tonacja.tonacja_z_symbolu('C')) % 7)

    def test_kodu_midi_1(self):
        d1 = dzwiek.Dzwiek(1, 'c##')
        d2 = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d1.podaj_swoj_kod_midi(), d2.podaj_swoj_kod_midi())

    def test_kodu_bezwzglednego_2(self):
        d1 = dzwiek.Dzwiek(1, 'c##')
        d2 = dzwiek.Dzwiek(1, 'db')
        self.assertNotEqual(d1.podaj_swoj_kod_midi(), d2.podaj_swoj_kod_midi())

    def test_kodu_midi_3(self):
        d1 = dzwiek.Dzwiek(1, 'c')
        self.assertEqual(d1.podaj_swoj_kod_midi(), 24)

    def test_kodu_midi_4(self):
        d1 = dzwiek.Dzwiek(1, 'c#')
        self.assertEqual(d1.podaj_swoj_kod_midi(), 25)

    def test_kodu_midi_5(self):
        d1 = dzwiek.Dzwiek(1, 'd')
        self.assertEqual(d1.podaj_swoj_kod_midi(), 26)

    def test_kodu_midi_6(self):
        d1 = dzwiek.Dzwiek(2, 'cb')
        self.assertEqual(d1.podaj_swoj_kod_midi(), 35)

    def test_kodu_midi_7(self):
        d1 = dzwiek.Dzwiek(2, 'c')
        self.assertEqual(d1.podaj_swoj_kod_midi(), 36)


if __name__ == '__main__':
    unittest.main()
