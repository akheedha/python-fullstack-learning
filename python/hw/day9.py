# Base class
class Account:
    def __init__(self, name, balance):
        self._name = name          # protected
        self._balance = balance    # protected

    # Special method for + operator
    def __add__(self, other):
        return self._balance + other._balance


# SavingsAccount class
class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05


# CurrentAccount class
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02


# Main program
# Create objects
savings = SavingsAccount("Ravi", 10000)
current = CurrentAccount("Anjali", 15000)

# Display details
print("Savings Account:")
print("Name:", savings._name)
print("Balance:", savings._balance)
print("Interest:", savings.calculate_interest())

print("\nCurrent Account:")
print("Name:", current._name)
print("Balance:", current._balance)
print("Interest:", current.calculate_interest())

# Total balance using + operator
total_balance = savings + current
print("\nTotal Balance (Savings + Current):", total_balance)