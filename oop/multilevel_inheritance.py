#A child class inherits from a parent class, which itself inherits from another parent class.

class Vehicle:
    def __init__(self, model, make, horse_power):
        pass
    
    def move(self):
        print("Moving....")

class Car(Vehicle):
    def __init__(self, model, make, horse_power, type):
        super().__init__(model, make, horse_power)
        pass
    
class ElectricCar(Car):
    def __init__(self, model, make, horse_power, type):
        super().__init__(model, make, horse_power, type)
        
        pass
    def charge(self):
        print("Charging.......")

tesla = ElectricCar(make= 'xyz', model= 'abc', horse_power= 500, type= 'wxc')
tesla.move()
tesla.charge()


