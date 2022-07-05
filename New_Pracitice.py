class Vehicle:
    def __init__(self, name, mileage, speed, color, rent):
        self.name = name
        self.mileage = mileage
        self.speed = speed
        self.color = color
        self.rent = rent

    def new_speed(self):
        return "Vehicle speed: {}".format(self.speed)

    def vehicle_name(self):
        print("Name of Vehicle: {}".format(self.name))

    def all_details(self):
        print("Vehicle name :{}, Mileage :{}, Speed : {}, Color : {}, Rent : {} ".
              format(self.name, self.mileage, self.speed, self.color, self.rent))


class Bus(Vehicle):
    def __init__(self, name, mileage, speed, color, rent=1000):
        super().__init__(name, mileage, speed, color, rent)


class Car(Vehicle):
    def __init__(self, name, mileage, speed, color, rent):
        super().__init__(name, mileage, speed, color, rent)


b = Bus("Volvo", 100, 150, "Red")
b.all_details()


c = Car("BMW", 100, 300, "Black", 5000)
c.all_details()
