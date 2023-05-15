class Car:
    def __init__(self) -> None:
        self.make = ""
        self.model = ""
        self.year = 0
        return


my_car = Car()
print("My car before:")
print(my_car.__dict__)

my_car.make = "Nissan"
my_car.model = "Versa"
my_car.year = 2014


print("My car after:")
print(my_car.__dict__)

print(f"namespace of this file: {__name__}")