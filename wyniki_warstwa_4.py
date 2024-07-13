import sprawdzarka_warstwa_4 as spr_w_4
import obsluga_wyswietlania as ow
from partytura import Partytura
from enumerations.enum_nazwy_interwalow import NazwaInterwalu


def wynik_sygn_i_glosy_akordow_z_kwintami_rownoleglymi(partytura: Partytura) -> str:
    wyjscie = "Kwinty równoległe w połączeniach: "
    wynik = spr_w_4.sygn_i_glosy_z_rownoleglosciami(partytura, NazwaInterwalu.KWINTA_CZYSTA)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: " + ow.sygn_i_glosy_w_str(
            wynik) + f"{ow.NORMALNY}"
    return wyjscie


def wynik_sygn_i_glosy_akordow_z_oktawami_rownoleglymi(partytura: Partytura) -> str:
    wyjscie = "Oktawy równoległe w połączeniach: "
    wynik = spr_w_4.sygn_i_glosy_z_rownoleglosciami(partytura, NazwaInterwalu.PRYMA_CZYSTA)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: " + ow.sygn_i_glosy_w_str(
            wynik) + f"{ow.NORMALNY}"
    return wyjscie


def wynik_sygn_akordow_gdzie_ruch_glosow_w_jednym_kierunku(partytura: Partytura) -> str:
    wyjscie = "Wszystkie głosy w jednym kierunku w połączeniach: "
    wynik = spr_w_4.sygn_gdzie_ruch_glosow_w_tym_samym_kierunku(partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: " + ow.sygn_akordow_w_str(
            wynik) + f"{ow.NORMALNY}"
    return wyjscie


def wynik_sygn_i_glosy_z_ruchem_o_interwal_zwiekszony(partytura: Partytura) -> str:
    wyjscie = "Ruch o interwał zwiększony w połączeniach: "
    wynik = spr_w_4.sygn_i_glosy_gdzie_ruch_glosu_o_interwal_zwiekszony(partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: " + ow.sygn_i_glosy_w_str(
            wynik) + f"{ow.NORMALNY}"
    return wyjscie


def wynik_sygn_i_glosy_z_ruchem_o_septyme(partytura: Partytura) -> str:
    wyjscie = "Ruch o zbyt duży interwał w połączeniach: "
    wynik = spr_w_4.sygn_i_glosy_gdzie_ruch_o_septyme(partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: ", ow.sygn_i_glosy_w_str(
            wynik), f"{ow.NORMALNY}"
    return wyjscie


def wynik_sygn_niepoprawnych_rozwiazan_dominant(partytura: Partytura) -> str:
    wyjscie = "Niepoprawne rozwiązania dominant: "
    wynik = spr_w_4.sygn_niepoprawnych_rozwiazan_dominant(partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD}AKORDY nr: ", ow.sygn_akordow_w_str(wynik), f"{ow.NORMALNY}"
    return wyjscie


def wynik_sygn_niepoprawnych_rozwiazan_dominant_septymowych(partytura: Partytura) -> str:
    wyjscie = "Niepoprawne rozwiązania dominant septymowych: "
    wynik = spr_w_4.sygn_niepoprawnych_rozwiazan_dominant_septymowych(partytura)
    if not wynik:
        wyjscie += f"{ow.OK} BRAK {ow.NORMALNY}"
    else:
        wyjscie += f"{ow.BLAD} AKORDY nr: ", ow.sygn_akordow_w_str(wynik), f"{ow.NORMALNY}"
    return wyjscie


def poprawnosc_warstwy_4(partytura: Partytura) -> bool:
    if not spr_w_4.sygn_i_glosy_z_rownoleglosciami(partytura, NazwaInterwalu.KWINTA_CZYSTA) == []:
        return False
    if not spr_w_4.sygn_i_glosy_z_rownoleglosciami(partytura, NazwaInterwalu.PRYMA_CZYSTA) == []:
        return False
    if not spr_w_4.sygn_gdzie_ruch_glosow_w_tym_samym_kierunku(partytura) == []:
        return False
    if not spr_w_4.sygn_i_glosy_gdzie_ruch_glosu_o_interwal_zwiekszony(partytura) == []:
        return False
    if not spr_w_4.sygn_i_glosy_gdzie_ruch_o_septyme(partytura) == []:
        return False
    if not spr_w_4.sygn_niepoprawnych_rozwiazan_dominant(partytura):
        return False
    if not spr_w_4.sygn_niepoprawnych_rozwiazan_dominant_septymowych(partytura) == []:
        return False
    return True


def wyniki_warstwy_4(partytura: Partytura) -> str:
    wynik = f"{wynik_sygn_i_glosy_akordow_z_kwintami_rownoleglymi(partytura)} \n"
    wynik += f"{wynik_sygn_i_glosy_akordow_z_oktawami_rownoleglymi(partytura)} \n"
    wynik += f"{wynik_sygn_akordow_gdzie_ruch_glosow_w_jednym_kierunku(partytura)} \n"
    wynik += f"{wynik_sygn_i_glosy_z_ruchem_o_interwal_zwiekszony(partytura)} \n"
    wynik += f"{wynik_sygn_i_glosy_z_ruchem_o_septyme(partytura)} \n"
    wynik += f"{wynik_sygn_niepoprawnych_rozwiazan_dominant(partytura)} \n"
    wynik += f"{wynik_sygn_niepoprawnych_rozwiazan_dominant_septymowych(partytura)} \n \n"
    return wynik
