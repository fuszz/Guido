OK = '\033[92m'
BLAD = '\033[91m'
OSTRZEZENIE = '\033[93m'
NORMALNY = '\033[0m'


def nr_taktow_w_str(lista: list[int]) -> str:
    wyjscie = ''
    for element in lista[:-2]:
        wyjscie += str(element + 1)
        wyjscie += ', '
    wyjscie += str(lista[-1] + 1)
    return wyjscie


def sygn_akordow_w_str(lista: list[(int, int)]) -> str:
    wyjscie = ''
    for element in lista[:-1]:
        wyjscie += str(element[0]) + '.' + str(element[1]) + ", "
    wyjscie += str(lista[-1][0]) + '.' + str(lista[-1][1])
    return wyjscie


def sygn_i_glosy_w_str(lista: list[(int, int, str)]) -> str:
    wyjscie = ''
    for element in lista[:-1]:
        wyjscie += str(element[0]) + '.' + str(element[1]) + " (" + str(element[2]) + "), "
    wyjscie += str(lista[-1][0]) + '.' + str(lista[-1][1]) + " (" + str(lista[-1][2]) + ")"
    return wyjscie
