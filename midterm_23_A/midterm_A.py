souradnice = [(0.563, 0.917, 0.909), (0.585, 0.912, 0.909), (0.574, 0.919, 0.911), (0.550, 0.921, 0.903), (0.552, 0.910, 0.900), (0.562, 0.910, 0.908), (0.566, 0.909, 0.911), (0.553, 0.924, 0.899), (0.594, 0.909, 0.920), (0.561, 0.897, 0.909), (0.563, 0.911, 0.908), (0.555, 0.915, 0.906), (0.572, 0.916, 0.908), (0.534, 0.917, 0.905), (0.545, 0.919, 0.904), (0.564, 0.910, 0.905), (0.561, 0.908, 0.908), (0.557, 0.918, 0.908), (0.542, 0.912, 0.906), (0.553, 0.924, 0.905), (0.569, 0.908, 0.911), (0.572, 0.916, 0.907), (0.574, 0.911, 0.907), (0.547, 0.920, 0.898), (0.557, 0.909, 0.906), (0.573, 0.914, 0.916), (0.564, 0.914, 0.907), (0.560, 0.912, 0.909), (0.560, 0.915, 0.908), (0.573, 0.917, 0.908), (0.569, 0.906, 0.908), (0.548, 0.917, 0.905), (0.570, 0.906, 0.908), (0.537, 0.917, 0.900), (0.562, 0.914, 0.905), (0.564, 0.912, 0.909), (0.565, 0.911, 0.909), (0.549, 0.914, 0.902), (0.558, 0.912, 0.906), (0.558, 0.909, 0.899), (0.547, 0.924, 0.900)]

def kontrola(coordinates):
    for ntice in coordinates:
        for n in ntice:
            if not isinstance(n, (int, float)):
                return False
    return True


def separuj(coordinates):
    list_x = []
    for ntice in coordinates:
        list_x.append(ntice[0])
    return list_x


def analyzuj(list_x):
    minimum_x = min(list_x)
    maximum_x = max(list_x)

    rozsah = maximum_x - minimum_x
    if rozsah > 0.05:
        return -1

    sorted_x = sorted(list_x)
    sorted_clean_x = sorted_x[5:-5]

    prumer = sum(sorted_clean_x)/len(sorted_clean_x)

    hranice = 0.15 * rozsah
    dolni_mez = prumer - hranice
    horni_mez = prumer + hranice

    pocet_mimo = 0
    for hodnota in list_x:
        if hodnota < horni_mez or hodnota > dolni_mez:
            pocet_mimo += 1

    procento = (pocet_mimo/len(list_x)) * 100

    return procento


def main(list_x):
    kontrola(souradnice)
    separuj(souradnice)
    analyzuj(list_x)


...
