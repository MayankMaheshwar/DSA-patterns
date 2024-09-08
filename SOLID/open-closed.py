from abc import ABC, abstractmethod
from single_responsibility import Invoice
class InvoiceDao(ABC):

    @abstractmethod
    def save(self):
        print("Saving")
        pass


class DatabaseInvoiceDao(InvoiceDao):

    def __init__(self, invoice):
        self.invoice = invoice

    def save(self):
        print("Saving to database")
        pass


class FileInvoiceDao(InvoiceDao):

    def __init__(self, invoice):
        self.invoice = invoice

    def save(self):
        print("Saving to file")
        pass




invoice_obj = Invoice(5, 100)
DatabaseInvoiceDao_obj = DatabaseInvoiceDao(invoice_obj)
FileInvoiceDao_obj = FileInvoiceDao(invoice_obj)

DatabaseInvoiceDao_obj.save()
FileInvoiceDao_obj.save()



