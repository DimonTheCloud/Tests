from collections import OrderedDict

NOT_ALLOWED = {
    "VIIII": "IX",
    "LXXXX": "XC",
    "DCCCC": "CM",
    "IIII": "IV",
    "XXXX": "XL",
    "CCCC": "CD"
}

def roman_validator(number):
    if not isinstance(number, str):
        return False, None

    for char in number:
        if char not in ["I", "V", "X", "L", "C", "D", "M"]:
            return False, None

    corrected = number

    for long_form, short_form in NOT_ALLOWED.items():
        corrected = corrected.replace(long_form, short_form)

    return True, corrected

def roman_to_arabic(roman):
    total = 0
    previous_value = 0

    for char in reversed(roman):
        value = MAP_R2A.get(char, None)

        if value < previous_value:
            total -= value
        else:
            total += value

        previous_value = value

    return total


def arabic_to_roman(number):
    roman = ""
    for value, symbol in MAP_A2R.items():
        while number >= value:
            roman += symbol
            number -= value

    is_valid, corrected = roman_validator(roman)
    return corrected


def sort_and_convert(numbers):
    roman_numbers = []
    arabic_numbers = []

    for number in numbers:
        is_roman, corrected = roman_to_arabic(number)

        if is_roman:
            arabic_value = arabic_to_roman(number)
            arabic_numbers.append(arabic_value)
        else:
            roman_value = roman_to_arabic(number)
            roman_numbers.append(roman_value)


    return roman_numbers, arabic_numbers













MAP_R2A = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
MAP_A2R = OrderedDict({1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"})

