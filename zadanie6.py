def suma_dzielnikow(dzielna):
    sumaDzielnikow = 0
    dzielniki = []

    for dzielnik in range(1, dzielna):

        if dzielna % dzielnik == 0:
            sumaDzielnikow = sumaDzielnikow + dzielnik
            dzielniki.append(dzielnik)

    return dzielniki

print(suma_dzielnikow(6))
