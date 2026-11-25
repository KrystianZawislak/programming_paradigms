space = " "
print(space*3,'|', end='')

for a in range(1,11):
    print(f"{space}{a:3}", end="")
print()

for a in range(45):
    print('-', end='')
print()

for a in range(1,11):
     print(f"{space}{a:2}{space}|", end='')
     for b in range(1,11):
        print(f"{a*b:4}", end='')
     print()
