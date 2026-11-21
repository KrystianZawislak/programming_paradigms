string = input("Enter string: ")

for i, char in enumerate(string):
    if (char == 'a' or char == 'A'):
        print(i, char)
