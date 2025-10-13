from base import Vehicle

class Bicyle(Vehicle):
    def __init__(self):
        super().__init__()
        self.engine=False
        self.wheels=2
    def get_fuel(self):
        return "None"
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.engine=True
        self.wheels=4
    def get_fuel(self):
        return super().get_fuel()

if __name__=="__main__":
    cycle=Bicyle()
    print("cycle wheels",cycle.wheels)
    car=Car()
    print("car wheels",car.wheels)
    base=Vehicle()
    print("base wheels",base.wheels)

