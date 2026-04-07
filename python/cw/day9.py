# Base class
class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id   # protected attribute
        self._base_rate = base_rate     # protected attribute

    def display_details(self):
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate}"

    def rental_charge(self):
        return 0.0   # placeholder (to be overridden)


# Subclass Car
class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self):
        return self._base_rate * self.num_seats


# Subclass Bike
class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        return self._base_rate * 0.5


# Polymorphism function
def calculate_rental(vehicle):
    return vehicle.rental_charge()


# Create objects
car = Car("CAR001", 100.0, 4)
bike = Bike("BIKE001", 80.0, "Scooter")

# Display details
print(car.display_details())
print("Car Rental Charge:", calculate_rental(car))

print(bike.display_details())
print("Bike Rental Charge:", calculate_rental(bike))