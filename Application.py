from ProjectPython import Emarket
class Application:
    def __init__(self):
        self.__emarket = Emarket()

    def help(self):
        print("Commands: ")
        print("0 Exit")
        print("1 Check the Store")

    def check_the_store(self):
        self.__emarket.display_products()
    