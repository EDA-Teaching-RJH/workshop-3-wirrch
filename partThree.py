score = int(input("Enter score: "))

if score >= 90 and score < 100:
    print("A, well done!")
elif score >= 80:
    print("B, good!")
elif score >= 70:
    print("C, nice.")
elif score >= 60:
    print("D, meh")
elif score < 60:
    print("F, uh oh")
else:
    print("Invalid entry")