roman_numeral = input()

individual_roman_to_arabic_numerals = {
    "I":1,"V":5,"X":10,
    "L":50,"C":100,"D":500,"M":1000
}

two_character_roman_to_arabic_numerals = {
    "IV":4,"IX":9,"XL":40,
    "XC":90,"CD":400,"CM":900
}

index = 0
arabic_numeral = 0
while index <= len(roman_numeral)-2:
    slice = roman_numeral[index:index+2]
    if slice in two_character_roman_to_arabic_numerals:
        arabic_numeral += two_character_roman_to_arabic_numerals[slice]
        index+=2
    else:
        arabic_numeral += individual_roman_to_arabic_numerals[slice[:1]]
        index+=1

if roman_numeral[-2:] not in two_character_roman_to_arabic_numerals:
    arabic_numeral += individual_roman_to_arabic_numerals[roman_numeral[-1]]

print(arabic_numeral)
