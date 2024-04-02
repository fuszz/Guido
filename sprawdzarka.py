import dzwiek
import enumerations.enum_interwal as intr
import tonacja

INTERWALY_DUR = [['1', '2', '3', '4', '5', '6', '7'],
                 ['7', '1', '2', '3>', '4', '5', '6'],
                 ['6>', '7', '1', '2>', '3>', '4', '5'],
                 ['5', '6', '7<', '1', '2', '3', '4<'],
                 ['4', '5', '6', '7', '1', '2', '3'],
                 ['3>', '4', '5', '6>', '7', '1', '2'],
                 ['2>', '3>', '4', '5>', '6', '7', '1']]

INTERWALY_MOLL = [['1', '2', '3>', '4', '5', '6>', '7<'],
                  ['7', '1', '2>', '3>', '4', '5>', '6'],
                  ['6', '7', '1', '2', '3', '4', '5<'],
                  ['5', '6', '7', '1', '2', '3>', '4<'],
                  ['4', '5', '6>', '7', '1', '2>', '3'],
                  ['3', '4<', '5', '6', '7<', '1', '2<'],
                  ['2>', '3>', '4>', '5>', '6>', '7>', '1']]


def podaj_interwal(dzwiek_a: dzwiek.Dzwiek, dzwiek_b: dzwiek.Dzwiek, badana_tonacja: tonacja.Tonacja) -> \
        (int, intr.Interwal):
    """
    Podaje, jaki interwał leży pomiędzy dźwiękami a i b. Nieczuły na kolejność dźwięków. Dźwięki muszą znajdować się w
    tonacji badana_tonacja, w przeciwnym razie podniesie BladDzwiekPozaTonacją.
    :param dzwiek_a: dzwiek a, dzwiek.Dzwiek
    :param dzwiek_b: dzwiek b, dzwiek.Dzwiek
    :param badana_tonacja: tonacja, w ktorej leżą oba dźwięki, instancja tonacja.Tonacja.
    :return: (int, Interwal), gdzie int jest liczbą pełnych oktaw znajdujących się między dźwiękami,
    a Interwał to instancja klasy enum_interwal.Interwal.
    """

    if dzwiek_a.podaj_swoj_kod_bezwzgledny() > dzwiek_b.podaj_swoj_kod_bezwzgledny():
        dzwiek_a, dzwiek_b = dzwiek_b, dzwiek_a
    pelnych_oktaw = (dzwiek_b.podaj_swoj_kod_bezwzgledny() - dzwiek_a.podaj_swoj_kod_bezwzgledny()) // 12

    stopien_a = dzwiek_a.podaj_swoj_stopien(badana_tonacja)
    stopien_b = dzwiek_b.podaj_swoj_stopien(badana_tonacja)
    symbol = INTERWALY_DUR[stopien_a][stopien_b] if badana_tonacja.czy_dur() else INTERWALY_MOLL[stopien_a][stopien_b]
    return pelnych_oktaw, intr.Interwal(symbol)
