inventory = [
    {"title": "book 1", "price": 10.0, "quantity": 100},
    {"title": "book 2", "price": 15.0, "quantity": 50},
    {"title": "book 3", "price": 20.0, "quantity": 30},
    {"title": "book 4", "price": 25.0, "quantity": 10},
    {"title": "book 5", "price": 30.0, "quantity": 5}
]

def existing_book():
    while True:
        book = input("Please indicate the name of the book: ").lower()
        found = False
        for i in inventory:
            if i["title"] == book:
                found = True
                print(f"the {book} already exists so we are unable to add it, however you can edit the quantity")
                return found
        if not found:
            return book
        
def request_price():
    while True:
        try: 
            price = float(input("Please type the price of the book: "))
            if price > 0:
                return price
            else:
                print("The price must be a positive number higher than zero, please try again\n")
        except ValueError:
            print("--\033[31mERROR\033[0m-- The value is incorrect, please type a valid number.\n")
            
def request_quantity():
    while True:
        try: 
            quantity = int(input("Please type the quantity of the book: "))
            if quantity >= 0:
                return quantity
            else:
                print("The quantity must be a positive number higher than zero, please try again\n")
        except ValueError:
            print("--\033[31mERROR\033[0m-- The value is incorrect, please type a valid number.\n")
            
def add_book(new_book, price, quantity):
    inventory.append({"title":new_book,"price":price,"quantity":quantity})
    
def find_book(book):
    found = False
    for i in inventory:
        if i["title"] == book:
            found = True
            print(f"the {book} was found an here is the information\n{i["title"]} | {i["price"]} | {i["quantity"]}")
    if not found:
        print(f"The book you're trying to find doesn't exist at the moment\n")

def update_price(book, price):
    found = False    
    for i in inventory:
        if i["title"] == book:
            found = True
            i["price"] = price
            print(f"the {book} was found an here is the information\n{i["title"]} | {i["price"]} | {i["quantity"]}")
    if not found:
        print(f"The book you're trying to edit doesn't exist\n")    

def delete_book(book):
    found = False    
    for i in inventory:
        if i["title"] == book:
            found = True
            inventory.remove(i)
            return
    if not found:
        print(f"The book you're trying to delete doesn't exist in the invetory\n")        

def total_amount():
    sum = 0
    for i in inventory:
        print(f"{i["title"]} | {i["price"]} | {i["quantity"]}")
        product = i["price"]*i["quantity"]
        sum = sum + product
    print(f"\n\033[32mTOTAL\033[0m:  {sum:.2f}")
    
while True:
        #Menu interactivo principal
        print("""
            -----\033[33mLIBRERY\033[0m-----\n
        1. Add new book to the inventary
        2. Consult book
        3. Update the price of the book
        4. Delete book
        5. Total inventory
        6. Close application\n""")
        option = input("Choose an option: ")
        match option:
            case "1":
                new_book = existing_book()
                if new_book != True:
                    price = request_price()
                    quantity = request_quantity()
                    add_book(new_book, price, quantity)
            case "2":
                book = input("Type the name of the book you are looking for: ").lower()
                find_book(book)
            case "3":
                book = input("Type the name of the book you want to update: ").lower()
                price = request_price()
                update_price(book, price)
            case "4":
                book = input("Type the book you want to delete: ").lower()
                delete_book(book)
            case "5":
                total_amount()
            case "6":
                print("\033[35mClosing...\033[0m")
                break
            case _:
                print("The option is not eligible or doesn't exist, please try again\n")          