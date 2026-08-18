class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'Car("{self.make}", "{self.model}")'

my_car = Car("Ford", "Mustang")
print(repr(my_car))
# Output: Car("Ford", "Mustang")

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

my_car = Car("Ford", "Mustang")
print(my_car)
# Output: Ford Mustang