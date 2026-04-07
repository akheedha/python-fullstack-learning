# Create lists
fruits = ["Apple", "Banana", "Mango"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Tea", "Coffee", "Water"]

# Add a new item to fruits
fruits.append("Orange")

# Insert item at second position in vegetables
vegetables.insert(1, "Onion")

# Remove last item from beverages
beverages.pop()

# Combine into nested list
inventory = [fruits, vegetables, beverages]

# Slicing - first two fruits
print("First two fruits:", fruits[:2])

# Negative indexing - last vegetable
print("Last vegetable:", vegetables[-1])

# List comprehension - lengths of fruit names
fruit_lengths = [len(item) for item in fruits]
print("Lengths of fruit names:", fruit_lengths)

# Check if "Water" is in beverages
print("Is 'Water' in beverages?", "Water" in beverages)

# Tuple of first item from each section
first_items = (fruits[0], vegetables[0], beverages[0])
print("First items tuple:", first_items)