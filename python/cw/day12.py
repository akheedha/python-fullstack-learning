try:
    # Get user input
    title = input("Enter book title: ")
    year = input("Enter publication year: ")

    # Validate title (only alphabets and spaces)
    if not all(char.isalpha() or char.isspace() for char in title):
        raise ValueError("Invalid title! Only alphabets and spaces allowed.")

    # Validate year (must be 4-digit starting with 19 or 20)
    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Invalid year! Must be a 4-digit year starting with 19 or 20.")

    # If valid
    print("Book accepted!")
    print("Title:", title)
    print("Year:", year)

except ValueError as e:
    print("Error:", e)

finally:
    print("Program execution completed.")