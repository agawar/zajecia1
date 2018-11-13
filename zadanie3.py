def silnia(n):
    wynik = 1
    i = 1
    while i < n:
        i = i + 1
        wynik = wynik * i
    return wynik

print(silnia(3))
print(silnia(5))

def suma_silni(n):
    sumasilni = 0
    for i in range(n):
        sumasilni = sumasilni + silnia(i+1)
    return sumasilni

for i in range(3,6):
    print("{0}: {1:>5}".format(i, suma_silni(i)))