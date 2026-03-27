def geneticka_predispozice_lecby(string):
    score = 0

    if len(string) > 15:
        score += 3

    if string.count("M") >= 5:
        score += 5

    if string.count("Z") < 3:
        score += 4

    if string.count("A") > 6:
        score -= 6

    if score > 5:
        return 3
    else:
        return 9

def vyber_leku(string, score):

    if string.count("M") >= 5 > score:
        return "jablko"
    elif string.count("A") == 5 and string.count("M") < 2:
        return "injekce"
    else:
        return "prasky"


def samovona_mutace(string, leky):
    pass