# Base class
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}")


# Derived class Trainer
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}")


# Derived class YogaInstructor
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, Yoga Style: {self.yoga_style}")


# Multiple inheritance class
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Trainer.__init__(self, name, role, specialization)
        YogaInstructor.__init__(self, name, role, yoga_style)

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, "
              f"Specialization: {self.specialization}, Yoga Style: {self.yoga_style}")


# Create objects
emp = Employee("Asha", "Manager")
trainer = Trainer("Rahul", "Trainer", "Strength Training")
yoga = YogaInstructor("Neha", "Yoga Instructor", "Hatha Yoga")
multi = MultiTrainer("Vikram", "Multi Trainer", "Cardio", "Vinyasa")

# Display details
emp.display()
trainer.display()
yoga.display()
multi.display()