present = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))

percentage = (present / total) * 100

print("Attendance:", percentage, "%")

if percentage >= 75:
    print("You are eligible")
else:
    count = 0

    while percentage < 75:
        present = present + 1
        total = total + 1
        count = count + 1
        percentage = (present / total) * 100

    print("Attend", count, "more classes")