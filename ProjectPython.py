from file_handler import FileHandler
from product import Product

class Emarket:
    def __init__(self, product_file = "list.txt"):
        self.__file_handler = FileHandler(product_file)
        self.__products = {}
        raw_data = self.__file_handler.load_phones()
        for name,details in raw_data.items():
                self.__products[name] = Product(name, details["price"], details["amount"])

    def display_products(self):
        print("Products available in the Market:")
        for product in self.__products.values():
            print(product)

    def get_product_info(self,product_name):
        """Return the product object if it exists, otherwise return None"""
        return self.__products.get(product_name, None)
    
    def update_product_quantity(self,product_name,quantity_change):
        product = self.get_product_info(product_name)
        if product:
            new_amount = product.amount + quantity_change
            if new_amount < 0:
                print("Not enough stock.")
                return
            product.amount = new_amount
            self.__save_data()
        else:
            print(f"Product {product_name} not found")


    def add_product(self,product_name, price, amount):
        if product_name in self.__products:
            print(f"Product {product_name} already exist")
        else:
            new_product = Product(product_name, price, amount)
            self.__products[product_name] = new_product
            self.__save_data()

    def search_products(self,keyword):
        """Search for products that contain the given keyword in their name. Returns a dictionary of matching products"""
        results = {}
        for name, product in self.__products.items():
            if keyword.lower() in name.lower():
                results[name] = product
        return results

    def sort_products_by_price(self):
        """Return a list of products sorted by price in ascending order """
        return sorted(self.__products.items(), key=lambda item: item[1].price)

    def apply_discount(self, product_name, discount):
        product = self.get_product_info(product_name)
        if product:
            new_price = product.price * (1-discount)
            product.price = new_price
            self.__save_data()
            print(f"Discount of {discount*100}% applied to '{product_name}'.")
            print(f"New final price: ${product.price:.2f}")
        else:
            print(f"{product_name} not found !")


    def __save_data(self):
        data_to_save = {p.name: {"price": p.price, "amount": p.amount} for p in self.__products.values()}
        self.__file_handler.save_phones(data_to_save)