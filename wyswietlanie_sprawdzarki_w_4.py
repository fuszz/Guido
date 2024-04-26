import sprawdzarka_warstwa_4 as spr_w_4
import obsluga_wyswietlania as ow
from partytura import Partytura
from enumerations.enum_nazwy_interwalow import NazwaInterwalu


def wyswietl_sygn_i_glosy_akordow_z_kwintami_rownoleglymi(partytura: Partytura) -> bool:
    print("Kwinty równoległe w połączeniach: ", end='')
    wynik = spr_w_4.sygn_i_glosy_z_rownoleglosciami(partytura, NazwaInterwalu.KWINTA_CZYSTA)
    if not wynik:
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: ", ow.sygn_i_glosy_w_str(wynik), f"{ow.NORMALNY}")
        return False


def wyswietl_sygn_i_glosy_akordow_z_oktawami_rownoleglymi(partytura: Partytura) -> bool:
    print("Oktawy równoległe w połączeniach: ", end='')
    wynik = spr_w_4.sygn_i_glosy_z_rownoleglosciami(partytura, NazwaInterwalu.PRYMA_CZYSTA)
    if not wynik:
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: ", ow.sygn_i_glosy_w_str(wynik), f"{ow.NORMALNY}")
        return False


def wyswietl_sygn_akordow_gdzie_ruch_glosow_w_jednym_kierunku(partytura: Partytura) -> bool:
    print("Wszystkie głosy w jednym kierunku w połączeniach: ", end='')
    wynik = spr_w_4.sygn_gdzie_ruch_glosow_w_tym_samym_kierunku(partytura)
    if not wynik:
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: ", ow.sygn_akordow_w_str(wynik), f"{ow.NORMALNY}")
        return False


def wyswietl_sygn_i_glosy_z_ruchem_o_interwal_zwiekszony(partytura: Partytura) -> bool:
    print("Ruch o interwał zwiększony w połączeniach: ", end='')
    wynik = spr_w_4.sygn_i_glosy_gdzie_ruch_glosu_o_interwal_zwiekszony(partytura)
    if not wynik:
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: ", ow.sygn_i_glosy_w_str(wynik), f"{ow.NORMALNY}")
        return False


def wyswietl_sygn_i_glosy_z_ruchem_o_septyme(partytura: Partytura) -> bool:
    print("Ruch o zbyt duży interwał w połączeniach: ", end='')
    wynik = spr_w_4.sygn_i_glosy_gdzie_ruch_o_septyme(partytura)
    if not wynik:
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} WYSTĘPUJĄ w połączeniach przed akordami nr: ", ow.sygn_i_glosy_w_str(wynik), f"{ow.NORMALNY}")
        return False


def wyswietl_sygn_niepoprawnych_rozwiazan_dominant(partytura: Partytura) -> bool:
    print("Niepoprawne rozwiązania dominant: ", end='')
    wynik = spr_w_4.sygn_niepoprawnych_rozwiazan_dominant(partytura)
    if not wynik:
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD}AKORDY nr: ", ow.sygn_akordow_w_str(wynik), f"{ow.NORMALNY}")
        return False


def wyswietl_sygn_niepoprawnych_rozwiazan_dominant_septymowych(partytura: Partytura) -> bool:
    print("Niepoprawne rozwiązania dominant septymowych: ", end='')
    wynik = spr_w_4.sygn_niepoprawnych_rozwiazan_dominant_septymowych(partytura)
    if not wynik:
        print(f"{ow.OK} BRAK {ow.NORMALNY}")
        return True
    else:
        print(f"{ow.BLAD} AKORDY nr: ", ow.sygn_akordow_w_str(wynik), f"{ow.NORMALNY}")
        return False


def sprawdz_warstwe_4(partytura: Partytura) -> bool:
    czy_sprawdzenie_poprawne: bool = True
    if not wyswietl_sygn_i_glosy_akordow_z_kwintami_rownoleglymi(partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_sygn_i_glosy_akordow_z_oktawami_rownoleglymi(partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_sygn_akordow_gdzie_ruch_glosow_w_jednym_kierunku(partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_sygn_i_glosy_z_ruchem_o_interwal_zwiekszony(partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_sygn_i_glosy_z_ruchem_o_septyme(partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_sygn_niepoprawnych_rozwiazan_dominant(partytura):
        czy_sprawdzenie_poprawne = False
    if not wyswietl_sygn_niepoprawnych_rozwiazan_dominant_septymowych(partytura):
        czy_sprawdzenie_poprawne = False

    return czy_sprawdzenie_poprawne
