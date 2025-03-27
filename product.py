class Product:
    def __init__(self, name: str, price: float, amount:int):
        self.name = name
        self.__price = price
        self.__amount = amount

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value >=0:
            self.__price = value
        else:
            raise ValueError("Price must be positive")
    @property
    def amount(self):
        return self.__amount 
    
    @amount.setter
    def amount(self,value):
        if value >=0:
            self.__amount = value
        else:
            raise ValueError("amount must be positive")

    def __str__(self):
        return f"{self.name}: ${self.__price:.2f}, Available: {self.__amount}"
    
    def __add__(self,other):
        if isinstance(other,Product) and self.name ==other.name:
            return Product(self.name, self.__price, self.__amount + other.__amount)
        raise ValueError("You can only add products with the same name")
    
    def get_final_price(self):
        return self.__price
    
    @staticmethod
    def is_valid_product(name):
        return isinstance(name, str) and len(name) > 0
    

class DiscountedProduct(Product):
    def __init__(self, name:str, price: float, amount: int ,discount: float):
        super().__init__(name,price,amount)
        self.discount =discount

    def get_final_price(self):
        return super().get_final_price() * (1-self.discount)
    
    def apply_discount(self):
        final_price = self.get_final_price()
        print(f"The discounted price for{self.name} is: ${final_price:.2f}")
    
    def __str__(self):
        # Override to display both original and discounted price
        return (f"{self.name}: Original Price: ${super().price:.2f}, "
                f"Discounted Price: ${self.get_final_price():.2f}, "
                f"Available: {self.amount}")