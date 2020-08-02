##!/usr/bin/env python3

class Automobile:

    def __init__(self, make, engine):
        self.make = make
        self.engine = engine
        self.wheels = 0

    def printDetails(self):
        print(f"Type {self.wheels} wheeler")
        print(f"Make: {self.make}")
        print(f"Engine: {self.engine} CC")

# Has additional attributes and property
class Car(Automobile):

    def __init__(self):
        super().__init__('Tata', '1600')
        self.wheels = 4
    
    def printDetails(self):
        super().printDetails()

        print(f"Is reverse: {self.isReverse()}")
    
    def isReverse(self):
        return "Not"

# Main class methods and properties are sufficient
class Scooter(Automobile):

    def __init__(self):
        super().__init__('Bajaj', '140')
        self.wheels = 2


#Use the classes

vehicle = Car()
vehicle.printDetails()

print("========================================")

vehicle1 = Scooter()
vehicle1.printDetails()