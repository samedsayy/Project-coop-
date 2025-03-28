
import os
from file_handler import FileHandler

class User:

    user_count = 0

    def __init__(self, user_name, user_mail, user_phone):
        
        #public attr
        self.user_mail = user_mail
        self.user_phone = user_phone
        #protect attr 
        self._username = user_name
        #private attr
        self.__user_id =  User.user_count + 1
        #count
        User.user_count += 1
        #history for purchase
        self.history = []


    def __str__(self):
     return f"{self._username},{self.__user_id}"


    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def username(self):
        return self._username
    
    
    #User name must be more than 1 character.
    @username.setter
    def username(self,new_name):
        if len(new_name) >= 1:
            self._username = new_name
            return True
        
        else :
            return False
        
    
    @staticmethod
    def phone_checker(phone):
        if len(phone) >= 9:
            return True
        else :
            return False
        
    @staticmethod
    def mail_checker(email):
        if "@" in email and "." in email:
            return True
        
        elif "@" not in email or "." not in email:
            return False
        

    def purchase_history(self,name,price,amount):
        purchase_dict = {
            "product" : name,

            "amount" : amount,

            "total" : price * amount

        }

        self.history.append(purchase_dict)

        return purchase_dict
    
    def check_purchase_history(self):
        return self.history
    
    #Check user id is same
    def __eq__(self, another):

        if not isinstance(another,User):
            return False
        
        if self.__user_id == another.__user_id:
            return True
        else:
            return False

#Subclass
class SpecialUser(User):
    def __init__(self, user_name, user_mail, user_phone,user_rank=0):

        super().__init__(user_name, user_mail, user_phone)
        self.points = 0
        self.user_rank = user_rank

    def __str__(self):
        origin_str = super().__str__()
        return f"{origin_str},{self.points}"
    
    def discount(self,name,price,amount):
        discount_price = price * 0.97

        purchase = super().purchase_history(name,discount_price,amount)

        self.add_points(round(purchase["total"] * 0.01))

        return purchase
    
    def check_bonus(self,name,price,amount):

        purchase = super().purchase_history(name, price, amount)

        if price > 100:
            self.user_rank += 1

        if self.user_rank > 10:
            self.add_points(round(purchase["total"] * 0.03))

        return purchase

        


    def add_points(self,new_points):
        self.points += new_points
        return self.points
    
    def use_points(self,points):
        if self.points >= points:
            self.points -= points
        else:
            return False
    


if __name__ == "__main__":
    
    user1 = User("Taro", "kinoshita@sample.com","000000000")

    print(user1)
    print(user1.username)
    print(user1.user_id)

    mail_check = User.mail_checker("kinoshita@sample.com")
    print(mail_check)
    mail_check = User.mail_checker("kinoshita|sample.com")
    print(mail_check)

    phone_check = User.phone_checker("000000000")
    print(phone_check)
    phone_check = User.phone_checker("123")
    print(phone_check)

    user1.purchase_history("Apple Mac Pro",999.999,1)

    hist = user1.check_purchase_history()
    for i in hist :
        print(i["product"])
        print(i["total"])

    user2 = User("Samed", "Say@sample.com","111111111")

    print(user1 == user2)
    print(user1 == user1)


