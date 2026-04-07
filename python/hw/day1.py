import random

# Prices per kg (₹)
rice_price = 45
sugar_price = 40
oil_price = 130

# Quantities (kg)
rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

# Calculate total for each item
rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty

print("Rice total:", rice_total)
print("Sugar total:", sugar_total)
print("Oil total:", oil_total)

# Final total bill (float)
total_bill = rice_total + sugar_total + oil_total
print("Total bill (float):", total_bill)

# Convert to integer
total_int = int(total_bill)
print("Total bill (int):", total_int)

# Convert to string
total_str = str(total_int)
print("Total bill as string: ₹" + total_str)

# Random delivery charge between 5 and 10
delivery_charge = random.randint(5, 10)

# Final bill including delivery
final_bill = total_int + delivery_charge
print("Delivery charge:", delivery_charge)
print("Final bill including delivery: ₹", final_bill)