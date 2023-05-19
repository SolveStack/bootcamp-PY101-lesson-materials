class Car(object):
    def __init__(self, make: str, model: str, year: int, tow_required: bool = False) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.tow_required = tow_required
    
    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"
    
# Without providing tow_required:
my_car = Car("Jeep", "Wrangler", 2023)
print(f"My car is {my_car}")