money = int(input("Input an amount of money you want to check:"))
results = 0
for a in range(money//10+1):
    for b in range(money//5+1):
        for c in range(money//2+1):
            if (a*10 + b*5 + c*2) == money:
                results += 1

print(results)


