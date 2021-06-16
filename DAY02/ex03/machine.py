import random
from beverages import *

class CoffeeMachine:
    def __init__(self):
        self.nbr = 0
    class EmptyCup(HotBeverages):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
        def description(self):
            return "An empty cup?! Gimme my money back!"
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    def repair(self):
        self.nbr = 0
    def serve(self, hot):
        if self.nbr >= 10:
            raise self.BrokenMachineException()
        self.nbr += 1
        x = random.randint(0, 1)
        if x == 1:
            hot = hot
        else:
            hot = self.EmptyCup()
        return hot
    
if __name__ == '__main__':
    machine = CoffeeMachine()
    hot = HotBeverages()
    cup = machine.serve(hot)
    print(cup)
    coffee = Coffee()
    cup2 = machine.serve(coffee)
    print(cup2)
    tea = Tea()
    cup3 = machine.serve(tea)
    print(cup3)
    for i in range(13):
        try:
            cup = machine.serve(hot)
        except Exception as error:
            print(error)
    print(machine.nbr)
    machine.repair()
    print(machine.nbr)
    for i in range(13):
        try:
            cup = machine.serve(hot)
        except Exception as error:
            print(error)
    print(cup)

