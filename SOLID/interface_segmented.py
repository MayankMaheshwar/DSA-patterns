"client should not implement interface they don't need to use" - "in this case Waiter"
from abc import ABC , abstractmethod

class RestaurantEmployee(ABC):

    @abstractmethod
    def cookFood(self):
        pass

    @abstractmethod
    def takeOrder(self):
        pass

    @abstractmethod
    def washUtensils(self):
        pass


class Waiter(RestaurantEmployee):
    def takeOrder(self):
        print("take orders")


" SOLUTION "


class WaiterInterface(ABC):
    @abstractmethod
    def takeOrder(self):
        pass

    @abstractmethod
    def serveOrder(self):
        pass


class CorrectWaiter(WaiterInterface):
    
    def takeOrder(self):
        return super().takeOrder()
    
    def serveOrder(self):
        return super().serveOrder()