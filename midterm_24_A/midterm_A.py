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
    if string.count("M") >= 5 and score < 5:
        return "jablko"
    elif string.count("A") == 5 and string.count("M") < 2:
        return "injekce"
    else:
        return "prasky"

def samovolna_mutace(string, lek):
    if lek == "jablko":
        return "Pokemon se uzdravil bez mutace"

    elif lek == "prasky":
        string = string.replace("A", "M")
        skore = string.count("M") * 3

        if skore > 10:
            return "Pokemon se vyvinul na jeho dalsi level"
        else:
            return "Pokemon se uzdravil, ale nema dostatecnou energii se vyvinout"

    elif lek == "injekce":
        string = string.replace("T", "M")
        string = string.replace("Z", "M")
        skore = string.count("M") * 3
