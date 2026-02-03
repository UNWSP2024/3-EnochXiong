def hotdog_cost():

    total = 0.0

    print("Hot Dog Types:")
    print("Hot Dog ($3.50)")
    print("Chili Dog ($4.50)")
    hotdog = input("Enter 1 for Hot Dog or 2 for Chili Dog: ")

    if hotdog == "1":
        total += 3.50
    elif hotdog == "2":
        total += 4.50

    cheese = input("Add cheese for $0.50? (y or n): ")
    if cheese.lower() == "y":
        total += 0.50

    pepper = input("Add cheese for $0.75? (y or n): ")
    if pepper.lower() == "y":
        total += 0.75

    grilled_onions = input("Add grilled onions for $1.00? (y or n): ")
    if grilled_onions.lower() == "y":
        total += 1.00

    tax = total * .07
    final_total = total + tax

    print("Cost of hot dog: $", format(total, ".2f"))
    print("Tax: $", format(tax, ".2f"))
    print("Total cost: $", format(final_total, ".2f"))

hotdog_cost()
