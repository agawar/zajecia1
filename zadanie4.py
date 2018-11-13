def podatek(kwota):
    podatek_do_zaplaty = 0
    pierwszy_prog = 44490
    drugi_prog = 85528

    if(kwota <= pierwszy_prog):
        podatek_do_zaplaty = podatek_do_zaplaty + 0.19 * kwota

    if(kwota <= drugi_prog):
        podatek_do_zaplaty = 0.19* pierwszy_prog + 0.30 * (kwota - pierwszy_prog)

    if(kwota > drugi_prog):
        podatek_do_zaplaty = 0.19* pierwszy_prog + 0.30 * drugi_prog + 0.40 * (kwota - drugi_prog)

    return podatek_do_zaplaty
print(podatek(85528))