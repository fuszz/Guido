import wyniki_warstwa_1 as w1
import wyniki_warstwa_2 as w2
import wyniki_warstwa_3 as w3
import wyniki_warstwa_4 as w4
from partytura import Partytura
import obsluga_wyswietlania as ow


def sprawdzaj(partytura: Partytura) -> str:
    wynik = f"{ow.OSTRZEZENIE} Warstwa 1 - poprawność i integralność danych{ow.NORMALNY} \n"
    wynik += w1.wyniki_warstwy_1(partytura)

    if not w1.poprawnosc_warstwy_1(partytura):
        wynik += f"{ow.BLAD} Wykryto błąd w warstwie 1. Dalsze sprawdzanie niemożliwe{ow.NORMALNY} \n"
        return wynik

    wynik += f"{ow.OSTRZEZENIE} Warstwa 2 - występowanie błędów pionowych{ow.NORMALNY} \n"
    wynik += w2.wyniki_warstwy_2(partytura)

    if not w2.poprawnosc_warstwy_2(partytura):
        wynik += f"{ow.BLAD} Wykryto błąd w warstwie 2. Dalsze sprawdzanie niemożliwe{ow.NORMALNY} \n"
        return wynik

    wynik += f"{ow.OSTRZEZENIE} Warstwa 3 - kolejność ułożenia akordów{ow.NORMALNY} \n"
    wynik += w3.wyniki_warstwy_3(partytura)

    if not w3.poprawnosc_warstwy_3(partytura):
        wynik += f"{ow.BLAD} Wykryto błąd w warstwie 3. Dalsze sprawdzanie niemożliwe{ow.NORMALNY} \n"
        return wynik

    wynik += f"{ow.OSTRZEZENIE} Warstwa 4 - poprawność połączeń akordów{ow.NORMALNY} \n"
    wynik += w4.wyniki_warstwy_4(partytura)

    if not w4.poprawnosc_warstwy_4(partytura):
        wynik += f"{ow.BLAD} Wykryto błąd w warstwie 4. Wynik negatywny{ow.NORMALNY} \n"
    else:
        wynik += f"{ow.OK} Nie wykryto błędów w partyturze. Wynik pozytywny{ow.NORMALNY} \n"

    return wynik
