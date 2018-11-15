import math

def jakzaplacic(kwota):
    nominaly = [20, 10, 5, 2, 1]
    liczbamonetlubbanknotow = []

    for nominal in nominaly:
        suma = ilemonetlubbanotow(kwota, nominal)
        liczbamonetlubbanknotow.append(suma)
        kwota = kwota - suma*nominal
        print("{1} bankotow/monet {0} zł".format(nominal, suma))

    print(liczbamonetlubbanknotow)

def ilemonetlubbanotow(pieniadze, nominal):
    return math.trunc(pieniadze/nominal)



jakzaplacic(123)