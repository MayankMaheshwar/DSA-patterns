class Marker:
    def __init__(self, color, thickness, price):
        self.price = price
        self.color = color
        self.thickness = thickness

    def draw(self):
        pass


class Invoice:

    def __init__(self, marker, quantity):
        self.quantity = quantity
        self.marker = marker

    def total(self):
        return self.quantity * self.price
    
    " 2nd reason to change the class "
    def printInvoice(self):
        pass

    " 3rd reason to change the class "
    def saveToDatabase(self):
        pass


class invoicePrinter:

    def __init__(self, invoice):
        self.invoice = invoice

    def printInvoice(self):
        pass


class invoiceDatabase:

    def __init__(self, invoice):
        self.invoice = invoice

    def saveToDatabase(self):
        pass