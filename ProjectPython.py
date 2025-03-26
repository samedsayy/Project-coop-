from file_handler import FileHandler
class Emarket:
    def __init__(self, product_file = "list.txt"):
        self.__file_handler = FileHandler(product_file)
        self.__products = self.__file_handler.load_phones()

    def display_products(self):
        """Print all available products in the market"""
        print("Products available in the Market")
        for name, details in self.__products.items():
            print(f"{name} - Price: ${details["price"]} | Available: {details["amount"]}")

    def get_product_info(self,product_name):
        """Return the product object if it exists, otherwise return None"""
        return self.__products.get(product_name, None)
    
    def sort_products_by_price(self):
        """Return a list of products sorted by price in ascending order"""
        return sorted(self.__products.items(), key=lambda item: item[1]['price'])
