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


def hebrejci(text):
    vysledek_hebrejci = ""
    
    if text == "":
        return False
    else:
        for char in text:
            vysledek_hebrejci += SIPHER[char]

    return vysledek_hebrejci
            

def polybiuv_ctverec_sifrovani():




























def main():
    pass