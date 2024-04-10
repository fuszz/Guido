import sprawdzarka_warstwa_3 as spr_w_3
from partytura import Partytura
import obsluga_wyswietlania as ow


def wyswietl_czy_pierwsza_i_ostatnia_tonika(badana_partytura: Partytura) -> bool:
    print("Tonika jako pierwszy i ostatni akord: ", end='')
    if spr_w_3.czy_pierwsza_i_ostatnia_tonika(badana_partytura):
        print(f"{ow.OK} TAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} NIE {ow.NORMALNY}")
        return False


def wyswietl_czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura: Partytura) -> bool:
    print("Ostateczne rozwiązanie w drugim przewrocie", end='')
    if spr_w_3.czy_pierwsza_i_ostatnia_tonika(badana_partytura):
        print(f"{ow.OK} NIE {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} TAK {ow.NORMALNY}")
        return False


def wyswietl_sygn_subdominant_po_dominancie(badana_partytura: Partytura) -> bool:
    print("Subdominanty umieszczone bezpośrednio po dominancie: ", end='')
    if not spr_w_3.sygn_subdominant_po_dominancie(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :",
              ow.sygn_akordow_w_str(spr_w_3.sygn_subdominant_po_dominancie(badana_partytura)),
              f"{ow.NORMALNY}")
        return False


def wyswietl_numery_taktow_gdzie_drugi_przewrot_na_raz(badana_partytura: Partytura) -> bool:
    print("Takty, w których na \"raz\" występuje drugi przewrót akordu: ", end='')
    if not spr_w_3.nr_taktu_gdzie_drugi_przewrot_na_raz(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :",
              ow.nr_taktow_w_str(spr_w_3.nr_taktu_gdzie_drugi_przewrot_na_raz(badana_partytura)),
              f"{ow.NORMALNY}")
        return False


def wyswietl_nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura: Partytura) -> bool:
    print("Takty, do których przez kreskę taktową przetrzymano funkcję ", end='')
    if not spr_w_3.nr_taktu_z_przetrzymana_przez_kreske_taktowa_funkcja(badana_partytura):
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :",
              ow.nr_taktow_w_str(spr_w_3.nr_taktu_z_przetrzymana_przez_kreske_taktowa_funkcja(badana_partytura)),
              f"{ow.NORMALNY}")
        return False


def sprawdz_warstwe_3(badana_partytura: Partytura) -> bool:
    czy_sprawdzenie_poprawne = True
    if not wyswietl_sygn_subdominant_po_dominancie(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_czy_pierwsza_i_ostatnia_tonika(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_numery_taktow_gdzie_drugi_przewrot_na_raz(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura):
        czy_sprawdzenie_poprawne = False
    return czy_sprawdzenie_poprawne
