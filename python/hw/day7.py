# Create empty inventory list
inventory = []

# Function to add items
def add_item(item):
    inventory.append(item)

# Recursive function to count items
def count_items(items):
    if not items:  # Base case
        return 0
    return 1 + count_items(items[1:])  # Recursive step

# Lambda function to display items
show_item = lambda item: print(f"Item in Stock: {item}")

# Main function
def main():
    # Add items
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    # Display items
    for item in inventory:
        show_item(item)

    # Count total items
    total = count_items(inventory)
    print("Total number of items:", total)

# Run the program
main()