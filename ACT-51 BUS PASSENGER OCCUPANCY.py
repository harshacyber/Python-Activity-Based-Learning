passengers = 0
capacity = 50

for i in range(5):
    print("Stop", i + 1)

    boarding = int(input("Passengers boarding: "))
    leaving = int(input("Passengers leaving: "))

    passengers = passengers - leaving + boarding

    if passengers > capacity:
        print("Bus is overloaded")
    else:
        print("Passengers inside bus:", passengers)

    if passengers < 0:
        print("Invalid passenger count")
        passengers = 0

print("Final passengers:", passengers)