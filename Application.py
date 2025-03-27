from ProjectPython import Emarket

class Application:
    def __init__(self):
        self.__emarket = Emarket()

    def help(self):
        print("Commands:")
        print("0: Exit")
        print("1: Check the Store")
        print("2: Search for a Product")
        print("3: Sort Products by Price")
        print("4: Update Product Quantity (Manager)")
        print("5: Add New Product (Manager)")
        print("6: Apply Discount (Manager)")

    def check_the_store(self):
        self.__emarket.display_products()

    def search_product(self):
        keyword = input("Enter keyword to search for: ")
        results = self.__emarket.search_products(keyword)
        if results:
            print("Search results:")
            for name, product in results.items():
                print(product)
        else:
            print("No product found with that keyword.")

    def sort_products(self):
        sorted_products = self.__emarket.sort_products_by_price()
        print("Products sorted by price (ascending):")
        for name, product in sorted_products:
            print(product)

    def update_product(self):
        product_name = input("Enter product name to update: ")
        try:
            quantity_change = int(input("Enter quantity change (use negative to reduce): "))
            self.__emarket.update_product_quantity(product_name, quantity_change)
        except ValueError:
            print("Invalid input. Please enter a valid number for quantity change.")

    def add_product(self):
        product_name = input("Enter new product name: ")
        try:
            price = float(input("Enter product price: "))
            amount = int(input("Enter product amount: "))
            self.__emarket.add_product(product_name, price, amount)
        except ValueError:
            print("Invalid input. Please ensure price is a number and amount is an integer.")

    def apply_discount(self):
        product_name = input("Enter product name to apply discount to: ")
        try:
            discount_input = float(input("Enter discount percentage (e.g., 15 for 15% off): "))
            discount = discount_input / 100  # Convert percentage to decimal
            self.__emarket.apply_discount(product_name, discount)
        except ValueError:
            print("Invalid input. Please enter a valid discount percentage.")

    def run(self):
        while True:
            self.help()
            choice = input("Enter your choice: ")
            if choice == "0":
                print("Exiting application. Goodbye!")
                break
            elif choice == "1":
                self.check_the_store()
            elif choice == "2":
                self.search_product()
            elif choice == "3":
                self.sort_products()
            elif choice == "4":
                self.update_product()
            elif choice == "5":
                self.add_product()
            elif choice == "6":
                self.apply_discount()
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = Application()
    app.run()
