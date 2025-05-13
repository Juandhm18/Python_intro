#List of  products with basic information: name, price and quantity
inventory = [
    {"product": "apple", "price": 10.0, "quantity": 25},
    {"product": "coconout", "price": 15.0, "quantity": 15},
    {"product": "mango", "price": 10.0, "quantity": 35},
    {"product": "tomato", "price": 5.0, "quantity": 50},
    {"product": "carrot", "price": 5.0, "quantity": 50}
]
#function that validates if a new product is already in the inventory and returns True or False
def existing_product(product):
    while True:
        found = False
        for i in inventory:
            if i['product'] == product:
                found = True
                print(f"the {product} already exists so we are unable to add it.")
                print("However you can edit the quantity\n")
                return found
        if not found:
            return found
#Requests and validates that the price is a valid floating point number.
def request_price():
    while True:
        try:
            price = float(input("Type the price of the product: "))
            if price > 0:
                return price
            else:
                print("The price must be a positive number higher than zero, try again\n")
        except ValueError:
            print("--\033[31mERROR\033[0m-- The value is incorrect, please type a valid number.\n")
#Requests and validates that the price is a valid number.
def request_quantity():
    while True:
        #Requests and validates that the amount is a valid integer.
        try:
            quantity = int(input("Please type the quantity of the product: "))
            if quantity >= 0:
                return quantity
            else:
                print("The quantity must be a positive number, please try again\n")
        except ValueError:
            print("--\033[31mERROR\033[0m-- The value is incorrect, please type a valid number.\n")
#Function to add a new product to the inventory
def add_product(new_product, price, quantity):
    inventory.append({"product":new_product,"price":price,"quantity":quantity})
    print("Product succesfully added...")
#Function that only shows the list of available products with price
def show_products():
    print("\n|     Market      |")
    for i in inventory:
        print(f"{i['product']} | ${i['price']}")
# Function to search for a product in the inventory
def find_product(product):
    found = False
    for i in inventory:
        if i['product'] == product:
            found = True
            print(f"""the {product} was found and here is the information
        PRODUCT     |    PRICE    |    QUANTITY\n
                {i['product']} | ${i['price']} | {i['quantity']}""")
    # If the product is not on the list, the user is informed
    if not found:
        print(f"\nWe don't have that product available")
# Function to update the price of an existing product
def update_price(product, price):
    found = False
    for i in inventory:
        if i['product'] == product:
            print(f"        {i['product']} | ${i['price']}")
            found = True
            i['price'] = price
            print(f"""the {product} was succesfully edited
        {i['product']} | ${i['price']}""")
    if not found:
        print(f"The product you're trying to edit is not available\n")
# Function to update the quantity of an existing product
def update_quantity(product, quantity):
    found = False
    for i in inventory:
        if i['product'] == product:
            print(f"        {i['product']} | {i['quantity']}")
            found = True
            i['quantity'] = quantity
            print(f"""the {product} was succesfully edited
        {i['product']} | {i['quantity']}""")
    if not found:
        print(f"The product you're trying to edit is not available\n")
# Function to remove a product from inventory
def delete_product(product):
    found = False
    for i in inventory:
        if i['product'] == product:
            found = True
            sure = input("Are you sure you want to remove this product? Y/N: ").upper()
            if sure == "Y":
                inventory.remove(i) # Use remove() to remove the correct dictionary
                print("This product was removed succesfully...\n")
                return
            else:
                print("Don't worry the product is still in your inventory...\n")
                return
    if not found:
        print(f"The product you're trying to delete doesn't exist in the invetory\n")
# Function that displays inventory and calculates total value
def total_amount():
    if not inventory:
        print("The inventory is empty.")
        return# Check if the list is empty
    mult = 0
    # Calculate the total value of the inventory by multiplying price * quantity
    for i in inventory:
        print(f"{i['product']} | {i['price']} | {i['quantity']}")
        product = i['price']*i['quantity']
        mult = mult + product
    print(f"\n\033[32mTOTAL\033[0m:  ${mult:.2f}")

while True:
        #Main interactive menu
        print("""
            -----\033[33mMARKET\033[0m-----\n
        1. Add new product to the inventary
        2. Show available products
        3. Consult product
        4. Update the price of the product
        5. Delete product
        6. Total inventory
        7. Close application\n""")
        option = input("Choose an option: ")
        match option:
            case "1":
                product = input("Please indicate the product name: ").lower()
                new_product = existing_product(product)
                #line to validate if a new product is already in the inventory
                if new_product != True: #If the item does not exist, it will be added
                    price = request_price()
                    quantity = request_quantity()
                    add_product(product, price, quantity)
                else:
                    edit = input(f"Do you want to edit the quantity of the product? yes/no: ").upper()
                    if edit == "YES":
                        quantity = request_quantity()
                        update_quantity(product, quantity)
                    else:
                        print("Redirecting to main menu...\n")
            case "2":
                show_products()
            case "3":
                product = input("Type the name of the product you are looking for: ").lower()
                find_product(product)
            case "4":
                product = input("Type the name of the product you want to update: ").lower()
                price = request_price()
                update_price(product, price)
            case "5":
                product = input("Type the product you want to delete: ").lower()
                delete_product(product)
            case "6":
                total_amount()
            case "7":
                print("\033[35mClosing...\033[0m")
                break
            case _:
                print("The option is not eligible or doesn't exist, please try again\n")

            ####README####
# This project aims to manage a store's inventory interface more dynamically, thereby better tracking available products, their quantity and price, and calculating their total value in the system.

# The system allows you to add products to the inventory, display the list of available products, consult a product by its name in the inventory, update the price of a product as well as the quantity, also allows you to delete a product and calculate the total value of the inventory.

# The code structure initially defines a dictionary list with the data for five products already registered in the inventory.
# This is followed by the functions used to validate the functionality, and finally, the interactive menu with the options the system can display and what the user can select as needed.

# To run this program, you need to have the most updated version of Python along with a debugger. You must also run the program to start the interactive menu. You can use "F5" or press play with the arrow at the top right of the screen.

#         1. Add new product to the inventary
#         2. Show available products
#         3. Consult product
#         4. Update the price of the product
#         5. Delete product
#         6. Total inventory
#         7. Close application

# This is the main menu, which has 7 options, if the user enters

# option #1 the system will allow them to add a new product, validating that both the quantity and the price are valid positive numbers, so if they enter a piece of information other than a positive number it will let the user know,
# this option also validates whether a product already exists or not, and if it already exists, it gives you the option to modify the quantity.
# Example: if the user add candy, the price is $8.0 and the quantity is 60 the system will show this message "Product succesfully added..."
                # Choose an option: 1
                # Please indicate the product name: corn
                # Type the price of the product: 8
                # Please type the quantity of the product: 60
                # Product succesfully added...

# Option #2 shows the list of products available in the inventory with their name and unit price.
# Example: the user will see this, |     Market      |
                                    # apple | $10.0
                                    # coconout | $15.0
                                    # mango | $10.0
                                    # tomato | $5.0
                                    # carrot | $5.0

# Option #3 specifically shows a single product according to its name. This validates that the product is in the inventory.
# Example: mango
                        # PRODUCT     |    PRICE    |    QUANTITY
                        #         mango | $10.0 | 35

# If you enter something that does not exist in the inventory, you will be duly notified by means of a message.
                    #We don't have that product available

# Option #4 allows you to update the unit price of a product. It also validates that the price is a valid positive number and lets you know when it is not.
#Example: apple, new price will be $8.0
                            #         apple | $10.0
                            # the apple was succesfully edited
                            #         apple | $8.0
# Option #5 allows you to delete a product, first validating its existence and, if so, displaying a message when the product does not exist.
# It also confirms whether you want to delete the product as a final validation method.
#Example: tomato
            #Type the product you want to delete: tomato
            #Are you sure you want to remove this product? Y/N: Y
            #This product was removed succesfully...

# Option #6 calculates the total value of all entered products based on their quantity and unit price, and then displays it on the screen.
                            # apple | 8.0 | 25
                            # coconout | 15.0 | 15
                            # mango | 10.0 | 35
                            # carrot | 5.0 | 50

                            # TOTAL:  $1025.00

# Option #7 ends the menu execution, displaying a completion message.
                            # Choose an option: 7
                            # Closing...
# If you do not enter a valid option or a different one than those mentioned above, the system will notify you and ask for another option until you enter a valid one.
#Example: 34
# Choose an option: 34
# The option is not eligible or doesn't exist, please try again

#             -----MARKET-----

#         1. Add new product to the inventary
#         2. Show available products
#         3. Consult product
#         4. Update the price of the product
#         5. Delete product
#         6. Total inventory
#         7. Close application
