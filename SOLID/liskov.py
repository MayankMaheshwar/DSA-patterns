"subclass should extend the capability of parent not narrow it down"

from abc import ABC, abstractmethod

class Bike(ABC):
    @abstractmethod
    def turnOnEngine(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Motorcycle(Bike):
    def turnOnEngine(self):
        print("Unicycle started")

    def stop(self):
        print("Unicycle stopped")
    

class Bicycle(Bike):
    " don't narrow down the capability of parent"
    def turnOnEngine(self):
        raise Exception("Bicycle cannot start")

    def stop(self):
        print("Bicycle stopped")


Bicycle_obj = Bicycle()
Bicycle_obj.turnOnEngine()