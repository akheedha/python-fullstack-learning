import random

# Store juice volumes
apple = 15.5
orange = 20
grape = 10.25

# Calculate total volume
total_volume = apple + orange + grape
print("Total volume (float):", total_volume)

# Convert to integer
total_int = int(total_volume)
print("Total volume (int):", total_int)

# Convert to string and print with message
total_str = str(total_int)
print("Total volume sold: " + total_str)

# Add random bonus between 5 and 10 (inclusive)
bonus = random.randint(5, 10)

# Final total
final_total = total_int + bonus
print("Final total after bonus:", final_total)