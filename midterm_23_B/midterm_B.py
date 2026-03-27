from os import replace
Kun = "Příliš žluťoučký kůň úpěl ďábelské ódy!"
DIAKRITIKA = ["á", "é", "í", "ó", "ú", "ý", "č", "ď", "ě", "ň", "ř", "š", "ť", "ž", "ů"]
SPECIALNI_ZNAKY = ["@", "#", "$", "~", "^", "&", "*", "{", "}", "[", "]", "(", ")", ",", ".", "!", "?", ">", "<", ";", "§"]
NAHRADA = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "ý": "y",
    "č": "c",
    "ď": "d",
    "ě": "e",
    "ň": "n",
    "ř": "r",
    "š": "s",
    "ť": "t",
    "ž": "z",
    "ů": "u"
}
SIPHER = {
        "a":"z",
        "b":"y",
        "c":"x",
        "d":"w",
        "e":"v",
        "f":"u",
        "g":"t",
        "h":"s",
        "i":"r",
        "j":"q",
        "k":"p",
        "l":"o",
        "m":"n",
        "n":"m",
        "o":"l",
        "p":"k",
        "q":"j",
        "r":"i",
        "s":"h",
        "t":"g",
        "u":"f",
        "v":"e",
        "w":"d",
        "x":"c",
        "y":"b",
        "z":"a",
        " ":" "
    }
polybius = {
    "p": 11, "o": 12, "l": 13, "y": 14, "b": 15,
    "i": 21, "s": 22, "a": 23, "c": 24, "d": 25,
    "e": 31, "f": 32, "g": 33, "h": 34, "j": 35,
    "k": 41, "m": 42, "n": 43, "q": 44, "r": 45,
    "t": 51, "u": 52, "v": 53, "w": 54, "x": 54, "z": 55,
    " ": 0
}

def uprava(message):
    vysledek = ""
    if message == "":
        return False

    else:
        for char in message:
            char = char.lower()
            if char in DIAKRITIKA:
                vysledek += NAHRADA[char]
            elif char in SPECIALNI_ZNAKY:
                continue
            elif char.isdigit():
                continue
            else:
                vysledek += char

    return vysledek


def hebrejci(vysledek):
    vysledek_hebrejci = ""
    
    if vysledek == "":
        return False
    else:
        for char in vysledek:
            vysledek_hebrejci += SIPHER[char]

    return vysledek_hebrejci
            

def polybiuv_ctverec_sifrovani(vysledek_hebrejci):
    if vysledek_hebrejci == []:
        return False

    siphered_message = ""

    for char in vysledek_hebrejci:
        siphered_message.append(polybius[char])

    return siphered_message




def main():
    uprava(Kun)
    hebrejci(uprava(Kun))
    polybiuv_ctverec_sifrovani(hebrejci(uprava(Kun)))



