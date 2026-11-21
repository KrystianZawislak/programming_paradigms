writing = input()
chars = set(writing)

for unique_char in chars:
    counter = 0
    print(unique_char + ":", end="")
    for index, char in enumerate(writing):
        if char == unique_char:
            counter+=1
            print(" "+str(index), end=" ")
    
    print(f"({counter})")
