def categorize_age(age):
    ageCategory = "TBD"

    if age <= 1:
        ageCategory = "infant"
    elif age < 13:
        ageCategory = "child"
    elif age < 20:
        ageCategory = "teenager"
    else:
        ageCategory = "adult"

    return ageCategory

if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)

