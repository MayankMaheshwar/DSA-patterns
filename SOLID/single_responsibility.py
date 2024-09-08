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
        return self.quantity * self.marker.price
    
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
        print("printing invoice", self.invoice.total())
        pass


class invoiceDao:

    def __init__(self, invoice):
        self.invoice = invoice

    def saveToDatabase(self):
        print("saving to db")
        pass


if __name__ == "__main__":
    marker_obj = Marker("red", 5, 100)
    invoice_obj = Invoice(marker_obj, 5)
    invoicePrinter_obj = invoicePrinter(invoice_obj)
    invoiceDao_obj = invoiceDao(invoice_obj)

    invoicePrinter_obj.printInvoice()
    invoiceDao_obj.saveToDatabase()
