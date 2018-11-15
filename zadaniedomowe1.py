def bmi(masa, wzrost):
    BMI = round(masa/(wzrost**2), 2)
    return BMI

def komentarz(bmi):
    if bmi < 18.5:
        komentarz_bmi = "Niedowaga"
    elif bmi < 25:
        komentarz_bmi = "Wartość prawidłowa"
    else:
        komentarz_bmi = "Nadwaga"

    print("{0}: {1}".format(bmi, komentarz_bmi))

def komentarz_rozszerzony(bmi):
    if bmi < 16:
        komentarz_bmi = "Wygłodzenie"
    elif bmi < 17:
        komentarz_bmi = "Wychudzenie"
    elif bmi < 18.5:
        komentarz_bmi = "Niedowaga"
    elif bmi < 25:
        komentarz_bmi = "Wartość prawidłowa"
    elif bmi < 30:
        komentarz_bmi = "Nadwaga"
    elif bmi < 35:
        komentarz_bmi = "I stopień otyłości"
    elif bmi < 40:
        komentarz_bmi = "II stopień otyłości - otyłość kliniczna"
    else:
        komentarz_bmi = "III stopień otyłości - otyłość skrajna"

    print("BMI = {0}: {1}".format(bmi, komentarz_bmi))

komentarz(bmi(100, 1.8))
komentarz_rozszerzony(bmi(100, 1.8))




