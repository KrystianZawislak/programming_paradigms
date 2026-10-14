money = int(input("Input an amount of money you want to check:"))
results = 0
for a in range(money//10+1):
    for b in range(money//5+1):
        rest = money - (a*10 + b*5)
        if rest >= 0 and rest % 2 == 0:
            results += 1

print(results)


