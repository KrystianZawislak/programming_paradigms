match input("Provide the day of the week: "):
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6" | "7":
        print("WEEKEND!")
    case _:
        print("Invalid data!")
