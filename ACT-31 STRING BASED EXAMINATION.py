key = ["A", "B", "C", "D", "A"]

correct = 0
wrong = 0
unanswered = 0

for i in range(5):
    ans = input("Enter answer: ").upper()

    if ans == "":
        unanswered = unanswered + 1
    elif ans == key[i]:
        correct = correct + 1
    else:
        wrong = wrong + 1

print("Correct answers:", correct)
print("Wrong answers:", wrong)
print("Unanswered:", unanswered)

print("Total marks:", correct)