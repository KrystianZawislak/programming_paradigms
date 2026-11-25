while True:
    conifer_height = int(input("Conifer Height: "))
    conifer_char = '*'
    end = 0
    
    if (conifer_height == 7):
        end = 1
    
    if (conifer_height % 2):
        conifer_char = '#'
    
    for a in range(1, conifer_height + 1):
        print((" " * (conifer_height - 1)) + (((2*a)-1)*conifer_char))
        conifer_height -= 1
    
    if end:
        break
