from ProjectPython import Emarket
class Application:
    def __init__(self):
        self.__emarket = Emarket()

    def check_the_store(self):
        self.__emarket.display_products()

    def search_product(self):
        keyword = input("Enter keyword to search for: ")
        results = self.__emarket.search_products(keyword)
        if results:
            print("Search results: ")
            for name, details in results.items():
                print(f"{name} - Price: ${details['price']} | Available: {details['amount']}")
        else:
            print(f"No item found with that keyword")


    def sort_products(self):
        sorted_products = self.__emarket.sort_products_by_price()
        print("Products sorted by price (ascending): ")
        for name, details in sorted_products:
            print(f"{name} - Price: ${details['price']} | Available: {details['amount']}")
    