for i in range(3):
    print("Day", i + 1)

    prepared = int(input("Enter prepared meals: "))
    served = int(input("Enter served meals: "))

    waste = prepared - served

    percentage = (waste / prepared) * 100

    print("Wasted meals:", waste)
    print("Waste percentage:", percentage, "%")

    if percentage > 20:
        print("High food waste")
    else:
        print("Food waste is normal")