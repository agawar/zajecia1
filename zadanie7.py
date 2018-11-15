def klasyfikator(napis):
    for slowo in napis.split():
        if len(slowo) < 6:
            znak = '+'
        else:
            znak = '-'
        print("{0} {1}".format(znak, slowo))

klasyfikator("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")