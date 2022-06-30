class Car(object):
    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = 0

my_car = Car()
print(my_car.__dict__) # returns attributes and functions
print(my_car)

my_car.make = "Hyundai"
my_car.model = "Elantra"
my_car.year = 2013
print(my_car.__dict__)

print(f"My car is a {my_car.year} {my_car.make} {my_car.model}")