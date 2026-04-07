import os

filename = "students.txt"

# Check if file exists
if os.path.exists(filename):
    print("Existing student names:")
    with open(filename, "r") as file:
        lines = file.readlines()
        if lines:
            for line in lines:
                print(line.strip())
        else:
            print("(No names found)")
else:
    print("File does not exist. A new file will be created.")

# Ask number of students
n = int(input("\nHow many student names do you want to add? "))

# Add new names
with open(filename, "a") as file:
    for i in range(n):
        name = input(f"Enter name {i+1}: ")
        file.write(name + "\n")

# Display updated list
print("\nUpdated student list:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())