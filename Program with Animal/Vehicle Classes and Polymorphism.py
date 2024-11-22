# Base class representing a general Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Car class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Animal class as another example of polymorphism
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Dog class inherits from Animal
class Dog(
