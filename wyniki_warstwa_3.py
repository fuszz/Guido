import sprawdzarka_warstwa_3 as spr_w_3
from partytura import Partytura
import obsluga_wyswietlania as ow


def wyswietl_czy_pierwsza_i_ostatnia_tonika(badana_partytura: Partytura) -> str:
    wynik = "Tonika jako pierwszy i ostatni akord: "
    if spr_w_3.czy_pierwsza_i_ostatnia_tonika(badana_partytura):
        wynik += f"{ow.OK} TAK {ow.NORMALNY}"
    else:
        wynik += f"{ow.BLAD} NIE {ow.NORMALNY}"
    return wynik


def wyswietl_czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura: Partytura):
    wynik = "Ostateczne rozwiązanie w drugim przewrocie"
    if spr_w_3.czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura):
        wynik += f"{ow.OK} NIE {ow.NORMALNY}"
    else:
        wynik += f"{ow.BLAD} TAK {ow.NORMALNY}"
    return wynik


def wyswietl_sygn_subdominant_po_dominancie(badana_partytura: Partytura) -> str:
    wyjscie = "Subdominanty umieszczone bezpośrednio po dominancie: "
    wynik = spr_w_3.sygn_subdominant_po_dominancie(badana_partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :" + ow.sygn_akordow_w_str(wynik) + f"{ow.NORMALNY}"
    return wyjscie


def wyswietl_numery_taktow_gdzie_drugi_przewrot_na_raz(badana_partytura: Partytura) -> str:
    wyjscie = "Takty, w których na \"raz\" występuje drugi przewrót akordu: "
    wynik = spr_w_3.nr_taktu_gdzie_drugi_przewrot_na_raz(badana_partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :" + ow.nr_taktow_w_str(wynik) + f"{ow.NORMALNY}"
    return wyjscie


def wyswietl_nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura: Partytura) -> str:
    wyjscie = "Takty, do których przez kreskę taktową przetrzymano funkcję "
    wynik = spr_w_3.nr_taktu_z_przetrzymana_przez_kreske_taktowa_funkcja(badana_partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w głosach akordów nr :" + ow.nr_taktow_w_str(wynik) + f"{ow.NORMALNY}"
    return wyjscie


def wyniki_warstwy_3(badana_partytura: Partytura) -> str:
    wynik = wyswietl_czy_pierwsza_i_ostatnia_tonika(badana_partytura) + '\n'
    wynik += wyswietl_sygn_subdominant_po_dominancie(badana_partytura) + '\n'
    wynik += wyswietl_numery_taktow_gdzie_drugi_przewrot_na_raz(badana_partytura) + '\n'
    wynik += wyswietl_czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura) + '\n'
    wynik += wyswietl_nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura) + '\n'
    return wynik


def poprawnosc_warstwy_3(badana_partytura: Partytura) -> bool:
    if not spr_w_3.czy_pierwsza_i_ostatnia_tonika(badana_partytura):
        return False
    if spr_w_3.sygn_subdominant_po_dominancie(badana_partytura):
        return False
    if spr_w_3.nr_taktu_gdzie_drugi_przewrot_na_raz(badana_partytura):
        return False
    if not spr_w_3.czy_ostateczne_rozwiazanie_nie_w_drugim_przewrocie(badana_partytura):
        return False
    if wyswietl_nr_taktu_z_ta_sama_funkcja_na_raz(badana_partytura):
        return False
    return True
