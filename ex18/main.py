list = [[0 for a in range(5)] for b in range(3)]
digit = 1
for a in range(3):
    for b in range(5):
        list[a][b] = digit**2
        digit += 1

print(list)