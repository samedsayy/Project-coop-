from Application import Application

def main():
    print("Commands: ")
    print("0: Exit")
    print("1: Check the Store")
    print("2: Search for a Product")
    print("3: Sort Products by Price")
    print("4: Update Product Quantity (Manager)")
    print("5: Add New Product (Manager)")
    print("6: Apply Discount (Manager)")
    
    app = Application()
    app.run()

if __name__ == "__main__":
    main()
