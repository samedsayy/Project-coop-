import os 

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def load_phones(self):
        """Load products from the file and return them as a dictionary."""
        products = {}
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, price, amount = line.strip().split(", ")
                    products[name] = {'price': float(price), 'amount': int(amount)}
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
            print(f"Current working directory: {os.getcwd()}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return products


class Emarket:
    def __init__(self):
        self.__my_products = {}

    def add_product(self,name,info):
        self.__my_products[name] = info

    def get_products(self):
        return self.__my_products


class Emarketapplication:
    def __init__(self):
        self.__emarket = Emarket()
        self.__filehandler = FileHandler("list.txt")

        products = self.__filehandler.load_phones()
        for name, info in products.items():
            self.__emarket.add_product(name,info)



    def help(self):
        print("Commands: ")
        print("0 Exit")
        print("1 Show products")


    def display_products(self):
        #Display all products
        for name, info in self.__emarket.get_products().items():
            print(f"Product: {name}, Price: {info['price']}, Amount: {info['amount']}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("Command: ")
            if command == "0":
                break
            elif command =="1":
                self.display_products()




app = Emarketapplication()
app.execute()