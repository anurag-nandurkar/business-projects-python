import csv

# Product Class
class Product:
    def __init__(self, sku, name, quantity, price):
        """
        Initialize a Product instance.

        :param sku: Stock Keeping Unit (unique identifier for the product)
        :param name: Name of the product
        :param quantity: Quantity in stock
        :param price: Price per unit
        """
        self.sku = sku
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        
    def __str__(self):
        return f"SKU: {self.sku}, Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}"

# Inventory Manager Class
class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def update_product(self, sku, quantity):
        for product in self.inventory:
            if product.sku == sku:
                product.update_quantity(quantity)
                print(f"Updated quantity for SKU {sku}: {quantity}")
                return
        print(f"Product with SKU {sku} not found.")

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            print("------------------")
            for product in self.inventory:
                print(product)

    def search_product(self, search_term):
        """Search for a product by name or SKU."""
        results = [p for p in self.inventory if search_term.lower() in p.name.lower() or search_term.lower() in p.sku.lower()]
        if results:
            print("\nSearch Results:")
            for product in results:
                print(product)
        else:
            print(f"No products found for search term: {search_term}")
            
    def export_to_csv(self, filename="inventory.csv"):
        """Export the inventory to a CSV file."""
        with open(filename, mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["SKU", "Name", "Quantity", "Price"])
            for product in self.inventory:
                writer.writerow([product.sku, product.name, product.quantity, product.price])
        print(f"Inventory exported to {filename}.")

# Main Function
def main():
    inventory_manager = InventoryManager()

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add New Product")
        print("2. Update Product Quantity")
        print("3. Display Inventory")
        print("4. Search Product")
        print("5. Export Inventory to CSV")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sku = input("Enter SKU: ")
            name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            product = Product(sku, name, quantity, price)
            inventory_manager.add_product(product)
            print(f"Product '{name}' added successfully.")

        elif choice == "2":
            sku = input("Enter SKU to update: ")
            quantity = int(input("Enter new quantity: "))
            inventory_manager.update_product(sku, quantity)

        elif choice == "3":
            inventory_manager.display_inventory()

        elif choice == "4":
            search_term = input("Enter product name or SKU to search: ")
            inventory_manager.search_product(search_term)

        elif choice == "5":
            inventory_manager.export_to_csv()

        elif choice == "6":
            print("Exiting the Inventory Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
