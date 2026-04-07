# Initial grocery list
grocery_list = ["milk", "bread", "eggs"]

# Function to add an item
def add_item(item):
    grocery_list.append(item)

# Function to remove last item
def remove_last_item():
    if grocery_list:
        grocery_list.pop()

# Lambda function to display items
display_items = lambda items: [print("Item:", item) for item in items]

# Recursive function to count characters
def count_characters(items):
    if not items:  # base case
        return 0
    return len(items[0]) + count_characters(items[1:])

# --- Using the functions ---

# Add items
add_item("butter")
add_item("cheese")

# Remove last item
remove_last_item()

# Display list
display_items(grocery_list)

# Count total characters
total_chars = count_characters(grocery_list)
print("Total characters in all items:", total_chars)