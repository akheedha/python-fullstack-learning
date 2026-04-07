# Multiline string for receipt header
header = """\n\tBOOKSTORE RECEIPT
\t----------------------\n"""

# Book details
book1_title = "Python Basics"
book1_price = 450

book2_title = "Data Science Intro"
book2_price = 600

# Format each book line using {} and format()
line1 = "\tBook: {} \t Price: ₹{}".format(book1_title, book1_price)
line2 = "\tBook: {} \t Price: ₹{}".format(book2_title, book2_price)

# Calculate total
total = book1_price + book2_price
total_line = "\n\tTotal: ₹{}".format(total)

# Thank you message
thank_you = "\n\tThank you for shopping with us!"

# Combine everything
receipt = header + line1 + "\n" + line2 + total_line + thank_you

# Display in uppercase
print(receipt.upper())