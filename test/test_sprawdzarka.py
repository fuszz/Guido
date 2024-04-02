import unittest
from enumerations import enum_interwal
import dzwiek
import blad
import sprawdzarka
import tonacja


class TestSprawdzarka(unittest.TestCase):
    def test_podaj_interwal_test1(self):
        dzwiek_a = dzwiek.Dzwiek(2, 'c')
        dzwiek_b = dzwiek.Dzwiek(2, 'd')
        self.assertEqual((0, enum_interwal.Interwal.SEKUNDA_WIELKA),
                         sprawdzarka.podaj_interwal(dzwiek_a, dzwiek_b, tonacja.Tonacja.C_DUR))

    def test_podaj_interwal_test2(self):
        dzwiek_a = dzwiek.Dzwiek(2, 'c')
        dzwiek_b = dzwiek.Dzwiek(2, 'd')
        self.assertEqual((0, enum_interwal.Interwal.SEKUNDA_WIELKA),
                         sprawdzarka.podaj_interwal(dzwiek_a, dzwiek_b, tonacja.Tonacja.A_MOLL))

    def test_podaj_interwal_test3(self):
        dzwiek_a = dzwiek.Dzwiek(2, 'c#')
        dzwiek_b = dzwiek.Dzwiek(2, 'd')
        with self.assertRaises(blad.BladDzwiekPozaTonacja):
            sprawdzarka.podaj_interwal(dzwiek_a, dzwiek_b, tonacja.Tonacja.A_MOLL)

    def test_podaj_interwal_test4(self):
        dzwiek_a = dzwiek.Dzwiek(3, 'c')
        dzwiek_b = dzwiek.Dzwiek(4, 'd')
        self.assertEqual((1, enum_interwal.Interwal.SEKUNDA_WIELKA),
                         sprawdzarka.podaj_interwal(dzwiek_a, dzwiek_b, tonacja.Tonacja.A_MOLL))


if __name__ == '__main__':
    unittest.main()
