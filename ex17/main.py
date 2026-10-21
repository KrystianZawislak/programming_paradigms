def convert_writing_to_int(string):
    if " " in string:
        dozens, unity=string.split()
        return dic[dozens] + dic[unity]
    else:
        return dic[string]
        

dic = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "twenty": 20, "thirty": 30, "forty": 40, 
    "fifty": 50
}

string = convert_writing_to_int(input())
print(string)
