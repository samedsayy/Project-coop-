#Order class
import datetime
from Shopping_cart import Shopping_cart
class Order():
    order_count = 0

    def __init__(self, user_id,items):
        #public attr
        if len(items) > 0:
            self.items = items
        else:
            self.items = []
        #protect attr
        self._user_id = user_id 
        #private attr
        self.__order_id = Order.order_count + 1
        
        
        #date
        self.add_data = datetime.datetime.now()
        #count
        Order.order_count += 1
        self.status = "processing"

        #list
        self.status_list = ["processing", "delivered", "canceled"]

    def __str__(self):
        return f"{self._user_id},{self.__order_id},{self.status}"
    
    
    @staticmethod
    def new_order(user_id,shopping_cart):
        new_order = Order(user_id, [])

        for n,m in shopping_cart.item.items():

            new_order.add_item(n, m["price"],  m["amount"])

        return new_order
    
    def add_item(self,name,price,amount):
        new_items = {

            "product" : name,
            "price" : price,
            "amount" : amount
        }
          
        self.items.append(new_items)
        

    def total_price(self):
        sum = 0
        for i in self.items:
            sum += i["price"] * i["amount"]

        return sum
    
    def new_status(self,new_status):

        if new_status in self.status_list:
            old_status = self.status
            self.status = new_status

        else:
            print("Invalid Status")
            return False
        
    def delivered_check(self):
        if self.status == "delivered":
            return True
        else :
            return self.status



if __name__ == "__main__":
    
    order1 = Order(1,[])

    order1.add_item("Apple Mac Pro",999.999,1)

    for i in order1.items:
        print(i['product'])
        print(i['price'])
        print(i['amount'])

    
    #order1.add_item("Apple Mac Pro",999.999,1)
    total = order1.total_price()

    print(total)

    print(order1.status)
    order1.new_status("delivered")
    print(order1.status)
    order1.new_status("RandomText")

    print(order1.delivered_check())

    cart = Shopping_cart(1)
    cart.add_item("Apple Mac Pro",999.999,1)
    new_order = Order.new_order(1,cart)


    print(new_order)

    for m in new_order.items:
        print(m['product'])
        print(m['price'])
        print(m['amount'])

    print(new_order.total_price())

