import os

# Get user input
item = input("Enter a new item: ")

# File name
filename = "items.txt"

# Check if file exists
if not os.path.exists(filename):
    # Create file and write item
    with open(filename, "w") as file:
        file.write(item + "\n")
else:
    # Append item to existing file
    with open(filename, "a") as file:
        file.write(item + "\n")

# Read and display all items
print("\nItems in the list:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())