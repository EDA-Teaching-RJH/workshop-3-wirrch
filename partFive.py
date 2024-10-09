dayName = str.lower(input("Enter a day of the week: "))

match dayName:
    case "saturday" | "sunday":
        print("It's the weekend!")
    case _:
        print("It's a weekday.")