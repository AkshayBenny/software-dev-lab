class ElectricCar:
    # Class attribute
    car_name = 'Tesla Model X'

    # Initialization
    def __init__(self, speed, x, y, electric_charge, max_charge):
        self.speed = speed
        self.x = x
        self.y = y
        self.electric_charge = electric_charge
        self.max_charge = max_charge

    def description(self):
        return f"The percentage of electric charge is {(self.electric_charge/self.max_charge)* 100}% "


my_car = ElectricCar("40km/h", 233, 44, 50, 100)

print(my_car.description())
