marks = []

for i in range(3):
    m = int(input("Enter exam marks: "))
    marks.append(m)

print("Exam marks:", marks)

if marks[2] > marks[0]:
    print("Performance improved")
elif marks[2] < marks[0]:
    print("Performance decreased")
else:
    print("Performance is the same")

average = sum(marks) / 3

print("Average marks:", average)