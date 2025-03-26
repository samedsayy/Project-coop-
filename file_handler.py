import os 
class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def load_phones(self):
        products = {}
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, price, amount = line.strip().split(", ")
                    products[name] = {"price":float(price), "amount": int(amount)}
        except FileNotFoundError:
            print(f"Error: The file {self.filename}")
            print(f"Current working directorty: {os.getcwd()}")

        except Exception as e:
            print(f"An error occured while reading the file: {e}")

        return products
    
    def save_phones(self, products):
        """Save the products dictionary back to the file"""
        try:
            with open(self.filename, "w") as file:
                for name, info in products.items():
                    file.write(f"{name}, {info["price"]}, {info["amount"]}\n")
        except Exception as e:
            print(f"An error occured while saving the file: {e}")



