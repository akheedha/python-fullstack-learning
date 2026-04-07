import random
import math

# Get input from user
names_input = input("Enter guest names (comma-separated): ")

# Convert to list and remove extra spaces
names_list = [name.strip() for name in names_input.split(",")]

# Remove duplicates using set
unique_names = list(set(names_list))

# Randomly select one name
selected_name = random.choice(unique_names)

# Reverse the selected name
reversed_name = selected_name[::-1]

# Count unique names
count = len(unique_names)

# Square root and round
sqrt_value = round(math.sqrt(count))

# Display results
print("\nUnique Names:", unique_names)
print("Selected Name:", selected_name)
print("Reversed Name:", reversed_name)
print("Total Unique Names:", count)
print("Rounded Square Root:", sqrt_value)