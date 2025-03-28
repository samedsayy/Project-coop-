from ProjectPython import Emarket
from User import User, SpecialUser
from Shopping_cart import Shopping_cart
from Order import Order

class MergedApplication:
    def __init__(self):
        self.emarket = Emarket()  # Product/store management system
        self.current_user = None  # The logged-in User object
        self.cart = None          # Shopping_cart for the current user
        self.order = None         # Latest Order

    # Product management sub-menu
    def manage_products(self):
        while True:
            print("\nProduct Management Menu:")
            print("1: Check the Store")
            print("2: Search for a Product")
            print("3: Sort Products by Price")
            print("4: Apply Discount")
            print("0: Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.emarket.display_products()
            elif choice == "2":
                keyword = input("Enter keyword to search for: ")
                results = self.emarket.search_products(keyword)
                if results:
                    print("Search results:")
                    for name, product in results.items():
                        print(product)
                else:
                    print("No product found with that keyword.")
            elif choice == "3":
                sorted_products = self.emarket.sort_products_by_price()
                print("Products sorted by price (ascending):")
                for name, product in sorted_products:
                    print(product)
            elif choice == "4":
                product_name = input("Enter product name to apply discount: ")
                try:
                    discount_input = float(input("Enter discount percentage (e.g., 15 for 15% off): "))
                    discount = discount_input / 100  # Convert percentage to decimal
                    self.emarket.apply_discount(product_name, discount)
                except ValueError:
                    print("Invalid discount input.")
            elif choice == "0":
                break
            else:
                print("Invalid option. Please try again.")

    # User management menu
    def user_menu(self):
        print("\nUser Menu:")
        print("1: Create User")
        print("2: Login as User")
        print("0: Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.create_user()
        elif choice == "2":
            self.login_user()
        elif choice == "0":
            return
        else:
            print("Invalid choice.")

    def create_user(self):
        user_name = input("Enter your name: ")
        user_mail = input("Enter your email: ")
        user_phone = input("Enter your phone: ")
        
        self.current_user = User(user_name, user_mail, user_phone)
        print("User created successfully!")
        self.post_user_login()

    def login_user(self):
        # In a full system, you'd search for a user; here we assume one exists.
        if self.current_user is None:
            print("No user exists. Please create a user first.")
        else:
            print("Logged in as:", self.current_user)
            self.post_user_login()

    def post_user_login(self):
        # Create a shopping cart for the logged-in user
        self.cart = Shopping_cart(self.current_user.user_id)
        print("Shopping cart created for user.")

    # Shopping cart management menu
    def manage_cart(self):
        if self.cart is None:
            print("Please login or create a user first.")
            return
        while True:
            print("\nShopping Cart Menu:")
            print("1: Add product to cart")
            print("2: Remove product from cart")
            print("3: View cart items")
            print("4: View total cart price")
            print("0: Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.emarket.display_products()
                product_name = input("Enter product name to add: ")
                try:
                    amount = int(input("Enter amount: "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                product_info = self.emarket.get_product_info(product_name)
                if product_info:
                    self.cart.add_item(product_name, product_info.price , amount)
                    print("Item added to cart.")
                else:
                    print("Product not found.")
            elif choice == "2":
                product_name = input("Enter product name to remove: ")
                try:
                    amount = int(input("Enter amount to remove: "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                self.cart.remove_item(product_name, amount)
                print("Item updated in cart.")
            elif choice == "3":
                print("Cart contents:")
                for name, details in self.cart.item.items():
                    print(f"{name}: Price: ${details['price']} | Amount: {details['amount']}")
            elif choice == "4":
                total = self.cart.total_price()
                print(f"Total cart price: ${total:.2f}")
            elif choice == "0":
                break
            else:
                print("Invalid option.")

    # Order management: Create an order from the shopping cart
    def place_order(self):
        if self.cart is None:
            print("No shopping cart found. Please manage your cart first.")
            return
        self.order = Order.new_order(self.current_user.user_id, self.cart)
        print("\nOrder placed successfully!")
        print("Order details:")
        print(self.order)
        print(f"Total Order Price: ${self.order.total_price():.2f}")

    # View purchase history from the user object
    def view_purchase_history(self):
        if self.current_user is None:
            print("No user logged in.")
            return
        print("\nUser Purchase History:")
        history = self.current_user.check_purchase_history()
        if isinstance(history, list):
            for record in history:
                print(record)
        else:
            # For SpecialUser, it might return a dictionary summary
            print(history)

    # Main menu integrating all functions
    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1: Manage Products")
            print("2: User Management")
            print("3: Manage Shopping Cart")
            print("4: Place Order")
            print("5: View Purchase History")
            print("0: Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.manage_products()
            elif choice == "2":
                self.user_menu()
            elif choice == "3":
                self.manage_cart()
            elif choice == "4":
                self.place_order()
            elif choice == "5":
                self.view_purchase_history()
            elif choice == "0":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def run(self):
        self.main_menu()


if __name__ == "__main__":
    app = MergedApplication()
    app.run()
