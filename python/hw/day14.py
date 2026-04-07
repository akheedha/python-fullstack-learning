import random
import math

# Get input
names_input = input("Enter customer names (comma-separated): ")

# Convert to list and clean spaces
names_list = [name.strip() for name in names_input.split(",")]

# Remove duplicates
unique_names = list(set(names_list))

# Shuffle names
random.shuffle(unique_names)

# Pick 2 winners (ensure at least 2 participants)
if len(unique_names) >= 2:
    winners = random.sample(unique_names, 2)
else:
    winners = unique_names

# Reverse winner names
reversed_winners = [name[::-1] for name in winners]

# Count participants
count = len(unique_names)

# Square root and round
sqrt_value = round(math.sqrt(count))

# Display results
print("\nShuffled Participants:", unique_names)
print("Winners (reversed names):", reversed_winners)
print("Total Unique Participants:", count)
print("Rounded Square Root:", sqrt_value)