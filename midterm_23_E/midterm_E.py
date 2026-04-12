MOL_WEIGHT = [
    ('H', 2.2), ('Li', 0.97), ('Na', 1.00), ('K', 0.91), ('Rb', 0.89), ('Cs', 0.86), ('Fr', 0.86), ('Be', 1.50),
    ('Mg', 1.20), ('Ca', 1.00), ('Sr', 0.99), ('Ba', 0.97), ('Ra', 0.97), ('Sc', 1.20), ('Y', 1.10), ('Ti', 1.30),
    ('Zr', 1.20), ('Hf', 1.20), ('Rf', 1.04), ('V', 1.50), ('Nb', 1.20), ('Ta', 1.30), ('Db', 1.05), ('Cr', 1.60),
    ('Mo', 1.30), ('W', 1.30), ('Sg', 1.06), ('Mn', 1.60), ('Tc', 1.40), ('Re', 1.50), ('Bh', 1.07), ('Fe', 1.60),
    ('Ru', 1.40), ('Os', 1.50), ('Hs', 1.08), ('Co', 1.70), ('Rh', 1.40), ('Ir', 1.50), ('Mt', 1.09), ('Ni', 1.70),
    ('Pd', 1.40), ('Pt', 1.40), ('Ds', 1.10), ('Cu', 1.70), ('Ag', 1.40), ('Au', 1.40), ('Rg', 1.11), ('Zn', 1.70),
    ('Cd', 1.50), ('Hg', 1.40), ('Cn', 1.12), ('B', 2.00), ('Al', 1.50), ('Ga', 1.80), ('In', 1.50), ('TI', 1.40),
    ('Nh', 1.13), ('C', 2.50), ('Si', 2.00), ('Ge', 2.00), ('Sn', 1.70), ('Pb', 1.50), ('FI', 1.14), ('N', 3.10),
    ('P', 2.10), ('As', 2.20), ('Sb', 1.80), ('Bi', 1.70), ('Mc', 1.15), ('O', 3.50), ('S', 2.40), ('Se', 2.50),
    ('Te', 2.00), ('Po', 1.80), ('Lv', 1.16), ('F', 4.10), ('Cl', 2.80), ('Br', 2.70), ('I', 2.20), ('At', 1.90),
    ('Ts', 1.17), ('He', 2), ('Ne', 1.0), ('Ar', 1.8), ('Kr', 3.6), ('Xe', 5.4), ('Rn', 8.6), ('Og', 1.18)
]


def decomposition(molecules):
    if len(molecules) == 0 or len(molecules) > 1:

        return "analyticka reakce neni mozna"

    molecule = molecules[0]
    result = []
    current = ""

    for char in molecule:
        if char.isupper():   # заглавная буква
            if current != "":
                result.append(current)
            current = char
        elif char.islower():   # маленькая буква
            current += char
        elif char.isdigit():   # цифра
            pass

    if current != "":
        result.append(current)

    return result

def molecular_weight(molecules):
    if len(molecules) == 0 or len(molecules) > 1:
        print("vypocet molekularni hmotnosti neni mozny")
        return

    atoms = decomposition(molecules)

    total_weight = 0

    for atom in atoms:
        for symbol, weight in MOL_WEIGHT:
            if atom == symbol:
                total_weight += weight

    return [str(total_weight) + " mol"]

def synthesis(molecules):
    if len(molecules) == 0 or len(molecules) < 2:
        return "synteza neni mozna"

    normalized = []

    for molecule in molecules:
        if molecule[0].isdigit():
            number = molecule[0]
            rest = molecule[1:]
            normalized.append(rest + number)

        elif molecule[-1].isdigit():
            number = molecule[-1]
            rest = molecule[:-1]
            normalized.append(number + rest)

        else:
            normalized.append(molecule)

    result = ""
    for molecule in normalized:
        result += molecule

    return result