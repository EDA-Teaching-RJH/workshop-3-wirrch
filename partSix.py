userAge = int(input("Enter age: "))
userStudent = str.lower(input("Are you a student (yes/no): "))

if userAge < 12 or userAge >= 65:
    price = 5
elif userStudent == "yes":
    price = 8
else:
    price = 10

print(f"Your ticket price is £{price}")
