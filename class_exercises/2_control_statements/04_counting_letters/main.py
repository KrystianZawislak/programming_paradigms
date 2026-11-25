string = input("Enter string: ")
result = 0

for char in string:
    result += char in 'aA'

print(f'The string contains {result} a, and A.')
