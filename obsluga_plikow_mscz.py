import xml.etree.ElementTree as ET
import akord
import dzwiek
import partytura
import tonacja
import blad
from enumerations import enum_metrum, enum_wartosci_nut
from typing import TextIO

""" MAŁA ŚCIĄGAWKA:

src = 'przyklady\przyklad0.mscx'
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

ADRES_INFO_O_METRUM_LICZNIK = ".//Score//Staff//Measure//voice//TimeSig//sigN"
ADRES_INFO_O_METRUM_MIANOWNIK = ".//Score//Staff//Measure//voice//TimeSig//sigD"


def wczytaj_z_pliku_mscx(adres: str) -> partytura.Partytura:
    """Wczytuje informacje podane w pliku mscx (zdekompresowany mscz) i zwraca je w postaci instancji klasy partytura.
    Zwraca takie same rodzaję błędów co odpowiadająca funkcja wczytaj_z_pliku_txt"""

    partytura = ET.parse(adres).getroot()

    # Tworzenie nowej partytury
    nowe_metrum: enum_metrum.Metrum = enum_metrum.Metrum(str(partytura.find(ADRES_INFO_O_METRUM_LICZNIK).text) + '/' +
                                                         str(partytura.find(ADRES_INFO_O_METRUM_MIANOWNIK).text))

    print(nowe_metrum.name)

wczytaj_z_pliku_mscx("przyklady\przyklad0.mscx")