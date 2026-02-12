from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

class BMW(Car):
    def start(self):
        print("BMW started with push button")

class Audi(Car):
    def start(self):
        print("Audi started with key")

car1 = BMW()
car1.start()

car2 = Audi()
car2.start()
