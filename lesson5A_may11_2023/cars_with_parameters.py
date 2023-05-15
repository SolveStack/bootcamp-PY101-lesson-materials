class Car():
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

mothers_day_car = Car("Range Rover", "Sport", 2023)

# these are the same now!
print(f"Mom's new car is a {mothers_day_car}")
print(f"Mom's new car is a {mothers_day_car.year} {mothers_day_car.make} {mothers_day_car.model}")