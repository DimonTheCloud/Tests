X = ['b', 'c', 'č', 'd', 'ď', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ň',
     'p', 'q', 'r', 'ř', 's', 'š', 't', 'ť', 'v', 'w', 'x', 'z', 'ž']

O = ['a', 'á', 'e', 'é', 'ě', 'i', 'í', 'o', 'ó', 'u', 'ú', 'ů', 'y', 'ý']
import csv


def read_words_data(filename):
    data = []
    with open(filename, "r", encoding="windows-1250") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            word = row[0].lower()
            freq = int(row[1])
            data.append((word, freq))

    return data


def select_popular_words(data, threshold = 1000):
    result = []

    for word, freq in data:
        if freq > threshold:
            result.append((word, freq))

    return result


def get_words_with_letter_restriction(data, allowed_letters):
    result = []

    for word, freq in data:
        is_valid = True

        for letter in word:
            if letter not in allowed_letters:
                is_valid = False

        if is_valid:
            result.append((word, freq))

    return result

def get_words_by_template(data, template):
    result = []

    for word, freq in data:
        word_template = ""

        for letter in word:
            if letter in X:
                word_template += "x"
            elif letter in O:
                word_template += "o"

        if word_template == template:
            result.append((word, freq))

    return result


def main(file_name, threshold, allowed_letters, templates):
    data = read_words_data(file_name)
    data = select_popular_words(data, threshold)
    data = get_words_with_letter_restriction(data, allowed_letters)

    result = []

    for template in templates:
        matched = get_words_by_template(data, template)

        for item in matched:
            result.append(item)

    if len(result) == 0:
        return "Nebyla nalezena žádná slova pro zadané podmínky."

    return result






