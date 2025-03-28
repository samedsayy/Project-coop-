class Product:
    def __init__(self, name: str, price: float, amount:int):
        self.name = name
        self.__price = price
        self.__amount = amount
    @property

    def name(self):
        return self.name
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value)>0:
            self.name = value
        else:
            raise ValueError("Name must not be empty")

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
    
    def __sub__(self,other):
        if isinstance(other,Product) and self.name == other.name:
            new_amount = self.amount - other.amount
            if new_amount < 0:
                new_amount = 0
            return Product(self.name, self.price, new_amount)
        raise ValueError("You can only use sub for proucts having same name")
    
    def __eq__(self,other):
        if isinstance(other, Product):
            return(self.name == other.name)
        return False
    
    def get_final_price(self):
        return self.__price
    
    @staticmethod
    def is_valid_product(name):
        return isinstance(name, str) and len(name) > 0
    


class DiscountedProduct(Product):
    def __init__(self, name: str, price: float, amount: int, discount: float):
        super().__init__(name, price, amount)
        self.discount = discount  

    def get_final_price(self):
        return self.price * (1 - self.discount)

    def __str__(self):
        return (f"{self.name}: Original Price: ${self.price:.2f}, "
                f"Discounted Price: ${self.get_final_price():.2f}, "
                f"Available: {self.amount}")
