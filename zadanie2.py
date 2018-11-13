def piramida_do_lewej(wysokosc):
    for poziom in range(wysokosc):
        print("#" * (2*poziom+1))

piramida_do_lewej(5)

def piramida(wysokosc):
    for poziom in range(wysokosc):
        print((" " * (wysokosc-poziom)),"#" * (2*poziom+1))

piramida(5)