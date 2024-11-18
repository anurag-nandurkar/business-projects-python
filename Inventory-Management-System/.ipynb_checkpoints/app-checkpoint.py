#lets create product class to product info
class Product:
    def __init__(self,sku,name,quantity,price):
        """
        Initialize a Product instance.

        :param sku: Stock Keeping Unit (unique identifier for the product)
        :param name: Name of the product
        :param quantity: Quantity in stock
        :param price: Price per unit
        """
        self.sku = sku
        self.name = name
        self.quanty =quantity
        self.price = price
        
    def update_quantity(self,new_quantity):
        self.quantity = new_quantity
    def __str__(self):
         return f"SKU: {self.sku}, Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}"
        
        