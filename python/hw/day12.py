try:
    # Get user input
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    # Check for empty inputs
    if name.strip() == "" or feedback.strip() == "":
        raise ValueError("Name and feedback cannot be empty!")

    # If valid
    print("Thank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)

except ValueError as e:
    print("Error:", e)

finally:
    print("Feedback process completed.")