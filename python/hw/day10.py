from abc import ABC, abstractmethod

# Abstract base class
class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    # Concrete method
    def account_age(self):
        return 2025 - self.account_year

    # Abstract method
    @abstractmethod
    def get_role(self):
        pass


# Admin subclass
class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"Admin User: {self.name}, Account Age: {self.account_age()} years"


# Guest subclass
class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"Guest User: {self.name}, Account Age: {self.account_age()} years"


# Create objects
admin = Admin("Asha", 2019)
guest = Guest("Rahul", 2022)

# Print details
print("Role:", admin.get_role())
print("Account Age:", admin.account_age())
print(admin)   # calls __str__()

print("\nRole:", guest.get_role())
print("Account Age:", guest.account_age())
print(guest)   # calls __str__()