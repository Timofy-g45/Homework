class Car:
    def __init__(self, model, fuel):
        self.model = model
        self.fuel = fuel

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 15
            print(f"{self.model} їде за кермом Залишилось палива {self.fuel}")

class FuelStation:
    def refuel(self, car, amount):
        car.fuel += amount
        print(f"Заправлений {amount} літрів для {car.model}.")

car = Car("Toyota", 53)
station = FuelStation()

car.drive()
car.drive()
station.refuel(car, 55)
car.drive()