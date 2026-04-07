# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Derived class Employee
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")


# Derived class PartTime
class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")


# Multiple inheritance class
class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        # Initialize Person through Employee
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, "
              f"Working Hours: {self.working_hours}, Project: {self.project_name}")


# Create objects
person = Person("Asha", 25)
employee = Employee("Rahul", 30, "E101")
part_time = PartTime("Neha", 22, 4.5)
consultant = Consultant("Vikram", 35, "E202", 6.0, "AI Project")

# Display details
person.show_details()
employee.show_details()
part_time.show_details()
consultant.show_details()