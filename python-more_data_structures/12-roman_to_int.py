#!/usr/bin/python3
def roman_to_int(roman_string=str):
    my_list = []
    num = 0
    index = 0
    index_next = 0
    my_dict = {"M": 1000, "MM": 2000, "MMM": 3000, "C": 100, "CC": 200, "CCC":
               300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800,
               "CM": 900, "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50,
               "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90, "I": 1, "II": 2,
               "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8,
               "IX": 9}
    if roman_string[index] == 'M':
        index_next = roman_string.find('C')
        if roman_string.find('D') < index_next or index_next == -1:
            index_next = roman_string.find('D')
        if index_next == -1:
            my_list.append(roman_string[index:])
        else:
            my_list.append(roman_string[index:index_next])
        index = index_next
    if roman_string[index] == 'C' or roman_string[index] == 'D':
        index_next = roman_string.find('X')
        if roman_string.find('L') < index_next or index_next == -1:
            index_next = roman_string.find('L')
        if index_next == -1:
            my_list.append(roman_string[index:])
        else:
            my_list.append(roman_string[index:index_next])
        index = index_next
    if roman_string[index] == 'X' or roman_string[index] == 'L':
        index_next = roman_string.find('I')
        if roman_string.find('V') < index_next or index_next == -1:
            index_next = roman_string.find('V')
        if index_next == -1:
            my_list.append(roman_string[index:])
        else:
            my_list.append(roman_string[index:index_next])
        index = index_next
    if roman_string[index] == 'I' or roman_string[index] == 'V':
        my_list.append(roman_string[index:])
    for i in my_list:
        num += my_dict[i]
    return num


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
