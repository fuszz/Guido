import xml.etree.ElementTree as ET
import akord
import dzwiek
import partytura
import tonacja
import blad
from enumerations import enum_metrum, enum_wartosci_nut

""" MAŁA ŚCIĄGAWKA:

src = 'przyklady\\przyklad0.mscx'
tree = ET.parse(src)
root = tree.getroot()

# Sposób na wysupłanie konkretnych wartości z XMLa
instrument = root.find(".//Score//Order//family")
print(instrument.tag)
print(instrument.text)
print(instrument.attrib)


# Powtarzające się nazwy:
meta_tagi = root.findall(".//Score//metaTag")
print([(x.tag, x.attrib, x.text) for x in meta_tagi])
"""

ADRES_INFO_O_METRUM_LICZNIK = "./Score/Staff/Measure/voice/TimeSig/sigN"
ADRES_INFO_O_METRUM_MIANOWNIK = "./Score/Staff/Measure/voice/TimeSig/sigD"
ADRES_WYZSZEJ_PIECIOLINI = './Score/Staff[@id="1"]'
ADRES_NIZSZEJ_PIECIOLINI = './Score/Staff[@id="2"]'
ADRES_LICZBA_ZNAKOW_PRZYKLUCZOWYCH = './Score/Staff[1]/Measure[1]/voice[1]/KeySig/concertKey'
ADRES_PODTYTUL_INFO_O_TONACJI = './Score/Staff[1]/VBox/Text[2]/text'
SLOWNIK_WARTOSCI_NUT = {"whole": 8, "half": 4, "quarter": 2, "eighth": 1}
MAPA_TPC = {
    -1: 'fbb', 0: 'cbb', 1: 'gbb',
    2: 'gbb', 3: 'abb', 4: 'ebb',
    5: 'hbb', 6: 'fb', 7: 'cb',
    8: 'hb', 9: 'db', 10: 'ab',
    11: 'eb', 12: 'bb', 13: 'f',
    14: 'c', 15: 'g', 16: 'd',
    17: 'a', 18: 'e', 19: 'h',
    20: 'f#', 21: 'c#', 22: 'g#',
    23: 'd#', 24: 'a#', 25: 'e#',
    26: 'h#', 27: 'f##', 28: 'c##',
    29: 'g##', 30: 'd##', 31: 'a##',
    32: 'e##', 33: 'h##'
}


def oblicz_ile_taktow(rodzic: ET.ElementTree) -> int:
    """Funckja iteruje po zawartości tagu Staff id=1 i zlicza wystąpienia tagu Measure"""
    licznik: int = 0
    rodzic = rodzic.find(ADRES_WYZSZEJ_PIECIOLINI)
    for dziecko in rodzic:
        if dziecko.tag == "Measure":
            licznik += 1
    return licznik


def utworz_partyture(rodzic: ET.ElementTree) -> partytura.Partytura:
    try:
        nowe_metrum: enum_metrum.Metrum = enum_metrum.Metrum(
            str(rodzic.find(ADRES_INFO_O_METRUM_LICZNIK).text) +
            '/' +
            str(rodzic.find(ADRES_INFO_O_METRUM_MIANOWNIK).text))
    except blad.BladTworzeniaMetrum:
        raise blad.BladWczytywaniaZPliku("Niepoprawne metrum")
    except IOError:
        raise blad.BladWczytywaniaZPliku("Nieznany błąd pliku. Sprawdź plik")

    try:
        nowa_liczba_taktow: int = oblicz_ile_taktow(rodzic)
        if nowa_liczba_taktow < 1:
            raise blad.BladWczytywaniaZPliku("Niepoprawna liczba taktów")
    except (blad.BladTworzeniaMetrum, ValueError, TypeError):
        raise blad.BladWczytywaniaZPliku("Niepoprawna liczba taktów")
    except IOError:
        raise blad.BladWczytywaniaZPliku("Nieznany błąd pliku. Sprawdź plik")

    try:
        nowa_tonacja: tonacja.Tonacja = tonacja.Tonacja.tonacja_z_symbolu(
            rodzic.find(ADRES_PODTYTUL_INFO_O_TONACJI).text)

    except blad.BladTworzeniaTonacji:
        raise blad.BladWczytywaniaZPliku("Niepoprawna nazwa tonacji")
    except IOError:
        raise blad.BladWczytywaniaZPliku("Nieznany błąd pliku. Sprawdź plik")

    return partytura.Partytura(nowa_tonacja, nowe_metrum, nowa_liczba_taktow)


def info_z_pliku_w_wartosc_nuty(tag_chord: ET.Element) -> enum_wartosci_nut.WartosciNut:
    dlugosc: str = str(tag_chord.find('./durationType').text)
    wezel_liczby_kropek: ET.Element = tag_chord.find('./dots')
    liczba_kropek: int = 0 if wezel_liczby_kropek is None else int(wezel_liczby_kropek.text)

    if dlugosc not in SLOWNIK_WARTOSCI_NUT.keys() or liczba_kropek > 1:
        raise blad.BladWczytywaniaZPliku("Niepoprawne wartości nut")
    wartosc_nuty: int = SLOWNIK_WARTOSCI_NUT[dlugosc] + liczba_kropek
    return enum_wartosci_nut.WartosciNut(wartosc_nuty)


def info_z_pliku_w_dzwiek(tag_chord: ET.Element) -> dzwiek.Dzwiek:
    kod_midi: int = int(tag_chord.find("./Note/pitch").text)
    kod_tpc: int = int(tag_chord.find("./Note/tpc").text)
    return dzwiek.Dzwiek(kod_midi // 12 - 1, MAPA_TPC[kod_tpc])


def wypelnij_partyture_akordami(rodzic: ET.ElementTree, nowa_partytura: partytura.Partytura) -> partytura.Partytura:
    pieciolinia_wyzsza: ET.Element = rodzic.find(ADRES_WYZSZEJ_PIECIOLINI)
    pieciolinia_nizsza: ET.Element = rodzic.find(ADRES_NIZSZEJ_PIECIOLINI)

    takty_wyzszej_pieciolinii: list[ET.Element] = [dziecko for dziecko in pieciolinia_wyzsza if
                                                   dziecko.tag == "Measure"]
    takty_nizszej_pieciolinii: list[ET.Element] = [dziecko for dziecko in pieciolinia_nizsza if
                                                   dziecko.tag == "Measure"]
    liczba_znakow_przykluczowych: int = int(rodzic.find(ADRES_LICZBA_ZNAKOW_PRZYKLUCZOWYCH).text)

    if len(takty_nizszej_pieciolinii) != len(takty_wyzszej_pieciolinii):
        raise blad.BladWczytywaniaZPliku("Różna liczba taktów w pięcioliniach")

    for numer_taktu in range(nowa_partytura.podaj_zadeklarowana_liczbe_taktow()):
        tagi_chord_sopranu: list[ET.Element] = takty_wyzszej_pieciolinii[numer_taktu].findall('./voice[1]/Chord')
        tagi_chord_altu: list[ET.Element] = takty_wyzszej_pieciolinii[numer_taktu].findall('./voice[2]/Chord')
        tagi_chord_tenoru: list[ET.Element] = takty_nizszej_pieciolinii[numer_taktu].findall('./voice[1]/Chord')
        tagi_chord_basu: list[ET.Element] = takty_nizszej_pieciolinii[numer_taktu].findall('./voice[2]/Chord')

        if len(tagi_chord_sopranu) != len(tagi_chord_altu) != len(tagi_chord_tenoru) != len(tagi_chord_basu):
            raise blad.BladWczytywaniaZPliku("Różna liczba dźwięków w głosach")

        for numer_akordu in range(len(tagi_chord_sopranu)):
            dlugosc_akordu = (info_z_pliku_w_wartosc_nuty(tagi_chord_sopranu[numer_akordu]))
            dzwiek_sopranu = info_z_pliku_w_dzwiek(tagi_chord_sopranu[numer_akordu])
            dzwiek_altu = info_z_pliku_w_dzwiek(tagi_chord_altu[numer_akordu])
            dzwiek_tenoru = info_z_pliku_w_dzwiek(tagi_chord_tenoru[numer_akordu])
            dzwiek_basu = info_z_pliku_w_dzwiek(tagi_chord_basu[numer_akordu])
            nowa_partytura.dodaj_akord(
                akord.Akord(dzwiek_sopranu, dzwiek_altu, dzwiek_tenoru, dzwiek_basu, dlugosc_akordu))
        nowa_partytura.zakoncz_takt()

    return nowa_partytura


def wczytaj_z_pliku_mscx(adres: str) -> partytura.Partytura:
    """Wczytuje informacje podane w pliku mscx (zdekompresowany mscz) i zwraca je w postaci instancji klasy partytura.
    Zwraca takie same rodzaję błędów co odpowiadająca funkcja wczytaj_z_pliku_txt"""

    rodzic = ET.parse(adres).getroot()
    nowa_partytura: partytura.Partytura = utworz_partyture(rodzic)
    return wypelnij_partyture_akordami(rodzic, nowa_partytura)


