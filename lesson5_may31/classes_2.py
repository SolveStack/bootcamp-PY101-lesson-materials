class Car:
    def __init__(self, make: str, model: str, year: int, tow_required=False) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.tow_required = tow_required
        self.location = "shop" # always starts at the shop
        self.symptoms = []
        self.assignee = None
    
    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def add_symptom(self, symptom: str):
        self.symptoms.append(symptom)

# my_car = Car("Jeep", "Wrangler", 2015)
# print(my_car)

# my_mentors_old_car = Car("Hyundai", "Elantra", 2013)
# print(my_mentors_old_car)

# Customer 1 things
customer_1_car = Car("Dodge", "Neon", 2005, tow_required=True)
print(customer_1_car)

print("Previous symptoms:")
print(customer_1_car.symptoms)

customer_1_car.add_symptom("won't start")
customer_1_car.add_symptom("smoke")
customer_1_car.add_symptom("overheating")
customer_1_car.add_symptom("engine knocking")

customer_1_car.assignee = "Jerry"
print(f"Assigned: {customer_1_car.assignee}")

print("Entered symptoms:")
print(customer_1_car.symptoms)


# Customer 2 things
customer_2_car = Car("Ford", "Focus", 2009, tow_required=False)
print(customer_2_car)

customer_2_car.add_symptom("leaking fluid")

