from abc import ABC, abstractmethod

# Abstract base class
class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    # Method to calculate years on platform
    def years_on_platform(self):
        return 2025 - self.joining_year

    # Abstract method (forces subclasses to implement)
    @abstractmethod
    def get_role(self):
        pass

    # Common display method
    def display(self):
        print(f"Name: {self.name}, Role: {self.get_role()}, "
              f"Years on Platform: {self.years_on_platform()}")


# Customer class
class Customer(User):
    def get_role(self):
        return "Customer"


# Vendor class
class Vendor(User):
    def get_role(self):
        return "Vendor"


# Main program
customer = Customer("Asha", 2020)
vendor = Vendor("Rahul", 2018)

customer.display()
vendor.display()