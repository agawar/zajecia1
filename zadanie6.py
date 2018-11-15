def suma_dzielnikow(dzielna):
    sumaDzielnikow = 0

    for dzielnik in range(1, dzielna):

        if dzielna % dzielnik == 0:
            sumaDzielnikow = sumaDzielnikow + dzielnik

    return sumaDzielnikow

print(suma_dzielnikow(6))
