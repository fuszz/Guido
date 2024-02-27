import unittest

from enum import enum_krzyzowania_glosow, enum_niepoprawne_stopnie
import sprawdzarka
import akord
import dzwiek
from venv.enum import enum_dzwieki_w_skalach
import tonacja


class MyTestCase(unittest.TestCase):
    def test_czy_glosy_w_skalach_1(self):
        db = dzwiek.Dzwiek(0, 'c')
        dt = dzwiek.Dzwiek(3, 'c')
        da = dzwiek.Dzwiek(2, 'd')
        ds = dzwiek.Dzwiek(4, 'c')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_w_swoich_skalach(a_test),
                         [enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI,
                          enum_dzwieki_w_skalach.DzwiekiWSkalach.PONIZEJ_SKALI,
                          enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI,
                          enum_dzwieki_w_skalach.DzwiekiWSkalach.PONIZEJ_SKALI])

    def test_czy_glosy_w_skalach_2(self):
        db = dzwiek.Dzwiek(3, 'c')
        dt = dzwiek.Dzwiek(3, 'g')
        da = dzwiek.Dzwiek(4, 'e')
        ds = dzwiek.Dzwiek(5, 'c')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_w_swoich_skalach(a_test),
                         [enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI,
                          enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI,
                          enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI,
                          enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI])

    def test_czy_glosy_w_skalach_3(self):
        db = dzwiek.Dzwiek(5, 'c')
        dt = dzwiek.Dzwiek(3, 'c##')
        da = dzwiek.Dzwiek(2, 'd')
        ds = dzwiek.Dzwiek(4, 'c')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_w_swoich_skalach(a_test),
                         [enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI,
                          enum_dzwieki_w_skalach.DzwiekiWSkalach.PONIZEJ_SKALI,
                          enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI,
                          enum_dzwieki_w_skalach.DzwiekiWSkalach.POWYZEJ_SKALI])

    def test_czy_glosy_nie_skrzyzowane_1(self):
        db = dzwiek.Dzwiek(0, 'c')
        dt = dzwiek.Dzwiek(3, 'c##')
        da = dzwiek.Dzwiek(4, 'c')
        ds = dzwiek.Dzwiek(4, 'c')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_nie_skrzyzowane(a_test), [])

    def test_czy_glosy_nie_skrzyzowane_2(self):
        db = dzwiek.Dzwiek(5, 'c')
        dt = dzwiek.Dzwiek(3, 'c##')
        da = dzwiek.Dzwiek(4, 'c')
        ds = dzwiek.Dzwiek(4, 'c')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_nie_skrzyzowane(a_test),
                         [enum_krzyzowania_glosow.KrzyzowaniaGlosow.SOPRAN_I_BAS,
                          enum_krzyzowania_glosow.KrzyzowaniaGlosow.ALT_I_BAS,
                          enum_krzyzowania_glosow.KrzyzowaniaGlosow.TENOR_I_BAS])

    def test_czy_glosy_nie_skrzyzowane_3(self):
        db = dzwiek.Dzwiek(5, 'c')
        dt = dzwiek.Dzwiek(3, 'd')
        da = dzwiek.Dzwiek(4, 'c')
        ds = dzwiek.Dzwiek(4, 'c')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_nie_skrzyzowane(a_test),
                         [enum_krzyzowania_glosow.KrzyzowaniaGlosow.SOPRAN_I_BAS,
                          enum_krzyzowania_glosow.KrzyzowaniaGlosow.ALT_I_BAS,
                          enum_krzyzowania_glosow.KrzyzowaniaGlosow.TENOR_I_BAS])

    def test_czy_glosy_nie_skrzyzowane_4(self):
        db = dzwiek.Dzwiek(2, 'c')
        dt = dzwiek.Dzwiek(3, 'c##')
        da = dzwiek.Dzwiek(4, 'd')
        ds = dzwiek.Dzwiek(4, 'c')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_nie_skrzyzowane(a_test),
                         [enum_krzyzowania_glosow.KrzyzowaniaGlosow.SOPRAN_I_ALT])

    def test_czy_glosy_sa_stopniami_tonacji_1(self):
        db = dzwiek.Dzwiek(2, 'c')
        dt = dzwiek.Dzwiek(3, 'f')
        da = dzwiek.Dzwiek(4, 'h')
        ds = dzwiek.Dzwiek(4, 'a')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_sa_stopniami_tonacji(a_test, tonacja.Tonacja('C')), [])

    def test_czy_glosy_sa_stopniami_tonacji_2(self):
        db = dzwiek.Dzwiek(2, 'c#')
        dt = dzwiek.Dzwiek(3, 'f')
        da = dzwiek.Dzwiek(4, 'h#')
        ds = dzwiek.Dzwiek(4, 'a')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_sa_stopniami_tonacji(a_test, tonacja.Tonacja('C')),
                         [enum_niepoprawne_stopnie.NiepoprawneStopnie.ALT,
                          enum_niepoprawne_stopnie.NiepoprawneStopnie.BAS])

    def test_czy_glosy_sa_stopniami_tonacji_3(self):
        db = dzwiek.Dzwiek(2, 'c')
        dt = dzwiek.Dzwiek(3, 'f')
        da = dzwiek.Dzwiek(4, 'h')
        ds = dzwiek.Dzwiek(4, 'a')
        a_test = akord.Akord(ds, da, dt, db, 1.0)
        self.assertEqual(sprawdzarka.Sprawdzarka.czy_glosy_sa_stopniami_tonacji(a_test, tonacja.Tonacja('C#')), [
            enum_niepoprawne_stopnie.NiepoprawneStopnie.SOPRAN,
            enum_niepoprawne_stopnie.NiepoprawneStopnie.ALT,
            enum_niepoprawne_stopnie.NiepoprawneStopnie.TENOR,
            enum_niepoprawne_stopnie.NiepoprawneStopnie.BAS
        ])


if __name__ == '__main__':
    unittest.main()
