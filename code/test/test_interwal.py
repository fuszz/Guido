import unittest
from dzwiek import Dzwiek
from enumerations.enum_nazwy_interwalow import NazwaInterwalu
from interwal import Interwal
from tonacja import Tonacja
import blad


class TestInterwal(unittest.TestCase):
    def test_podaj_interwal_test1(self):
        dzwiek_a = Dzwiek(2, 'c')
        dzwiek_b = Dzwiek(2, 'd')
        self.assertEqual(Interwal(0, NazwaInterwalu.SEKUNDA_WIELKA),
                         Interwal.stworz_z_dzwiekow(dzwiek_a, dzwiek_b, Tonacja.C_DUR))

    def test_podaj_interwal_test2(self):
        dzwiek_a = Dzwiek(2, 'c')
        dzwiek_b = Dzwiek(2, 'd')
        self.assertEqual(Interwal(0, NazwaInterwalu.SEKUNDA_WIELKA),
                         Interwal.stworz_z_dzwiekow(dzwiek_a, dzwiek_b, Tonacja.A_MOLL))

    def test_podaj_interwal_test3(self):
        dzwiek_a = Dzwiek(2, 'c#')
        dzwiek_b = Dzwiek(2, 'd')
        with self.assertRaises(blad.BladDzwiekPozaTonacja):
            Interwal.stworz_z_dzwiekow(dzwiek_a, dzwiek_b, Tonacja.A_MOLL)

    def test_podaj_interwal_test4(self):
        dzwiek_a = Dzwiek(3, 'c')
        dzwiek_b = Dzwiek(4, 'd')
        self.assertEqual(NazwaInterwalu.SEKUNDA_WIELKA,
                         Interwal.stworz_z_dzwiekow(dzwiek_a, dzwiek_b, Tonacja.A_MOLL).podaj_nazwe())


if __name__ == '__main__':
    unittest.main()
