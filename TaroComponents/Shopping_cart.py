#User shopping basket function. My task is....
#Shoppig Cart manager
#Add or Remove product
#Sum total price
#Show the content of cart

import os
from file_handler import FileHandler


class Shopping_cart():
    """The class manage shopping cart itself"""

    cart_count  = 0

    def __init__(self,user_id, cart_count=None):
        #public attr
        self.item = {}
        #protect attr
        self._user_id = user_id
        #private attr
        if cart_count is None:
            self.__cart_id = Shopping_cart.cart_count + 1
        else:
            self.__cart_id = cart_count + 1

        #count
        Shopping_cart.cart_count += 1
    
    def __str__(self):
        
        return f"{self.__cart_id},{self._user_id},{Shopping_cart.cart_count} "
    
    #decorators
    @property
    def user_id(self):
        
        return self._user_id
    #decorators
    @classmethod
    def cart_numbers(num):
        return num.cart_count

    def add_item(self,name ,price, amount):
        if name in self.item:
            self.item[name]['amount'] += amount

        else:
            self.item[name] = {'price': price, 'amount': amount}

    def total_price(self):
        sum = 0
        for i,o in self.item.items():
            #print(i)
            #print(o)
            sum += o['price'] * o['amount']

        return sum
    
    #Comparison of two carts(greater).
    def __gt__(self,another_cart):
        result =  self.total_price() > another_cart.total_price()
        return result

    #Comparison of two carts(smaller).
    def __lt__(self,another_cart):

        result =  self.total_price() < another_cart.total_price()
        return result
    
    #Marge two cart
    def __add__(self,another_cart):
        new_cart = Shopping_cart(self._user_id)

        for n,m in self.item.items():
            #print(n)
            #print(m)

            new_cart.add_item(n, m['price'],m['amount'])

        for j,k in another_cart.item.items():
            #print(j)
            #print(k)

            new_cart.add_item(j, k['price'],k['amount'])


        return new_cart

     
    def remove_item(self,name,remove_amount):
        
        if name in self.item:
            pass
        else:
            return False
        
        if remove_amount <= 0:
            raise ValueError("input positive interger")
        
        if self.item[name]['amount'] <= remove_amount:
            self.item.pop(name)
        else:
            self.item[name]['amount'] -= remove_amount
        
        

if __name__ == "__main__":

    current_direct = os.path.dirname(__file__)
    file_path = os.path.join(current_direct, "list.txt")
    handler = FileHandler(file_path)
    products = handler.load_phones()

    #print(products)
    #print(list(products.keys())[0])
    sample_product = list(products.keys())[0]
    #print(products["Apple Mac Pro"]["price"])
    sample_price = products["Apple Mac Pro"]["price"]
    #print(products["Apple Mac Pro"]["amount"])
    sample_amount = 1
   
    #Add item into the cart
    sample_id = 1
    cart1 = Shopping_cart(sample_id)
    cart1.add_item(sample_product ,sample_price , sample_amount)
    
    for n,m in cart1.item.items():
        print(n)
        print(m['price'])
        print(m['amount'])

    cart1.add_item(sample_product ,sample_price , sample_amount)
    total1 = cart1.total_price()
    print(total1)

    sample_id2 = 2
    cart2 = Shopping_cart(sample_id)
    cart2.add_item("Apple Wireless Keyboard",69.99 , sample_amount)
    total2 = cart2.total_price()

    print(cart1 > cart2)
    print(cart1 < cart2)

    mix_cart = cart1 + cart2

    for j,k in mix_cart.item.items():
        print(j)
        print(k['price'])
        print(k['amount'])

    cart1.add_item(sample_product ,sample_price , sample_amount)

    for e,r in cart1.item.items():
        print(e)
        print(r['price'])
        print(r['amount'])

    print("Removed")
    cart1.remove_item(sample_product,1)

    for a,b in cart1.item.items():
        print(a)
        print(b['price'])
        print(b['amount'])


