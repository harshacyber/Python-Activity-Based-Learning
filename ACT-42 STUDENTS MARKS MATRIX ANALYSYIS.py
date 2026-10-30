marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    row = []

    for j in range(3):
        m = int(input("Enter subject marks: "))
        row.append(m)

    marks.append(row)

for i in range(n):
    total = sum(marks[i])
    average = total / 3

    print("Student", i + 1)
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", average)