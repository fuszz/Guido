import enum_krzyzowania_glosow
import enum_przewroty
import partytura
import akord
import dzwiek
import enum_dzwieki_w_skalach
import enum_niepoprawne_stopnie
import tonacja
import enum_funkcje
import enum_zdwojony_skladnik


class Sprawdzarka:

    def czy_glosy_w_swoich_skalach(sprawdzany_akord: akord.Akord) -> list[enum_dzwieki_w_skalach.DzwiekiWSkalach]:
        kod_bezwzgledny_sopranu: int = sprawdzany_akord.podaj_sopran().podaj_swoj_kod_bezwzgledny()
        kod_bezwzgledny_altu: int = sprawdzany_akord.podaj_alt().podaj_swoj_kod_bezwzgledny()
        kod_bezwzgledny_tenoru: int = sprawdzany_akord.podaj_tenor().podaj_swoj_kod_bezwzgledny()
        kod_bezwzgledny_basu: int = sprawdzany_akord.podaj_bas().podaj_swoj_kod_bezwzgledny()
        wynik = []
        if kod_bezwzgledny_sopranu <= 69:
            if kod_bezwzgledny_sopranu >= 48:
                wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI)
            else:
                wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.PONIZEJ_SKALI)
        else:
            wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.POWYZEJ_SKALI)

        if kod_bezwzgledny_altu <= 62:
            if kod_bezwzgledny_altu >= 41:
                wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI)
            else:
                wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.PONIZEJ_SKALI)
        else:
            wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.POWYZEJ_SKALI)

        if kod_bezwzgledny_tenoru <= 57:
            if kod_bezwzgledny_tenoru >= 36:
                wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI)
            else:
                wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.PONIZEJ_SKALI)
        else:
            wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.POWYZEJ_SKALI)

        if kod_bezwzgledny_basu <= 50:
            if kod_bezwzgledny_basu >= 29:
                wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.W_SKALI)
            else:
                wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.PONIZEJ_SKALI)
        else:
            wynik.append(enum_dzwieki_w_skalach.DzwiekiWSkalach.POWYZEJ_SKALI)
        return wynik

    def czy_glosy_nie_skrzyzowane(sprawdzany_akord: akord.Akord) -> list[enum_krzyzowania_glosow.KrzyzowaniaGlosow]:
        kod_bezwzgledny_sopranu: int = sprawdzany_akord.podaj_sopran().podaj_swoj_kod_bezwzgledny()
        kod_bezwzgledny_altu: int = sprawdzany_akord.podaj_alt().podaj_swoj_kod_bezwzgledny()
        kod_bezwzgledny_tenoru: int = sprawdzany_akord.podaj_tenor().podaj_swoj_kod_bezwzgledny()
        kod_bezwzgledny_basu: int = sprawdzany_akord.podaj_bas().podaj_swoj_kod_bezwzgledny()
        wynik = []
        if kod_bezwzgledny_sopranu < kod_bezwzgledny_altu:
            wynik.append(enum_krzyzowania_glosow.KrzyzowaniaGlosow.SOPRAN_I_ALT)
        if kod_bezwzgledny_sopranu < kod_bezwzgledny_tenoru:
            wynik.append(enum_krzyzowania_glosow.KrzyzowaniaGlosow.SOPRAN_I_TENOR)
        if kod_bezwzgledny_sopranu < kod_bezwzgledny_basu:
            wynik.append(enum_krzyzowania_glosow.KrzyzowaniaGlosow.SOPRAN_I_BAS)
        if kod_bezwzgledny_altu < kod_bezwzgledny_tenoru:
            wynik.append(enum_krzyzowania_glosow.KrzyzowaniaGlosow.ALT_I_TENOR)
        if kod_bezwzgledny_altu < kod_bezwzgledny_basu:
            wynik.append(enum_krzyzowania_glosow.KrzyzowaniaGlosow.ALT_I_BAS)
        if kod_bezwzgledny_tenoru < kod_bezwzgledny_basu:
            wynik.append(enum_krzyzowania_glosow.KrzyzowaniaGlosow.TENOR_I_BAS)
        return wynik

    def czy_glosy_sa_stopniami_tonacji(sprawdzany_akord: akord.Akord, odpytywana_tonacja: tonacja.Tonacja) -> list[
        enum_niepoprawne_stopnie.NiepoprawneStopnie]:
        wynik = []
        try:
            sprawdzany_akord.podaj_sopran().podaj_swoj_stopien(odpytywana_tonacja)
        except ValueError:
            wynik.append(enum_niepoprawne_stopnie.NiepoprawneStopnie.SOPRAN)
        try:
            sprawdzany_akord.podaj_alt().podaj_swoj_stopien(odpytywana_tonacja)
        except ValueError:
            wynik.append(enum_niepoprawne_stopnie.NiepoprawneStopnie.ALT)
        try:
            sprawdzany_akord.podaj_tenor().podaj_swoj_stopien(odpytywana_tonacja)
        except ValueError:
            wynik.append(enum_niepoprawne_stopnie.NiepoprawneStopnie.TENOR)
        try:
            sprawdzany_akord.podaj_bas().podaj_swoj_stopien(odpytywana_tonacja)
        except ValueError:
            wynik.append(enum_niepoprawne_stopnie.NiepoprawneStopnie.BAS)
        return wynik

    def czy_poprawna_funkcja(sprawdzany_akord: akord.Akord, odpytywana_tonacja: tonacja.Tonacja) -> bool:
        if sprawdzany_akord.ustal_funkcje(odpytywana_tonacja) == enum_funkcje.Funkcja.BLAD:
            return False
        else:
            return True

    def czy_poprawne_dwojenia(sprawdzany_akord: akord.Akord, odpytywana_tonacja: tonacja.Tonacja) -> bool:
        podwojony_skladnik: enum_zdwojony_skladnik.ZdwojonySkladnik = sprawdzany_akord.ustal_dwojenie(
            odpytywana_tonacja)
        if sprawdzany_akord.ustal_funkcje(odpytywana_tonacja) == enum_funkcje.Funkcja.DOMINANTA_SEPTYMOWA:
            return True
        przewrot_akordu: enum_przewroty.Przewrot = sprawdzany_akord.ustal_przewrot(odpytywana_tonacja)
        if przewrot_akordu == enum_przewroty.Przewrot.POSTAC_ZASADNICZA:
            if podwojony_skladnik == enum_zdwojony_skladnik.ZdwojonySkladnik.PRYMA:
                return True
            else:
                return False
        elif przewrot_akordu == enum_przewroty.Przewrot.PIERWSZY:
            if podwojony_skladnik == enum_zdwojony_skladnik.ZdwojonySkladnik.PRYMA or \
                    podwojony_skladnik == enum_zdwojony_skladnik.ZdwojonySkladnik.KWINTA:
                return True
            else:
                return False
        elif przewrot_akordu == enum_przewroty.Przewrot.DRUGI:
            if podwojony_skladnik == enum_zdwojony_skladnik.ZdwojonySkladnik.KWINTA:
                return True
            else:
                return False
        else:
            return False
