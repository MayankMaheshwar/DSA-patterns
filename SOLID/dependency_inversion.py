# class should depends on interface not on concrete classes

from abc import ABC, abstractmethod

# Abstraction (Interface)
class MouseInterface(ABC):
    @abstractmethod
    def click(self):
        pass

# Concrete Implementations
class WiredMouse(MouseInterface):
    def __init__(self, name):
        print("wired mouse")
        self.name = name
    
    def click(self):
        print("wired mouse click")

class BluetoothMouse(MouseInterface):
    def __init__(self, name):
        print("bluetooth mouse")
        self.name = name
    
    def click(self):
        print("bluetooth mouse click")


# Abstraction (Interface)
class KeyboardInterface(ABC):
    @abstractmethod
    def type(self):
        pass

# Concrete Implementations
class BluetoothKeyboard(KeyboardInterface):
    def __init__(self, name):
        print("bluetooth keyboard")
        self.name = name
    
    def type(self):
        print("bluetooth keyboard type")

class WiredKeyboard(KeyboardInterface):
    def __init__(self, name):
        print("wired keyboard")
        self.name = name
    
    def type(self):
        print("wired keyboard type")


# High-level module
class MacBook:
    def __init__(self, mouse: MouseInterface, keyboard: KeyboardInterface):
        self.mouse = mouse
        self.keyboard = keyboard
        print("macbook")


# Dependency Injection
mouse = WiredMouse("Wired Mouse")
keyboard = WiredKeyboard("Wired Keyboard")
macbook = MacBook(mouse, keyboard)
macbook.mouse.click()
macbook.keyboard.type()
