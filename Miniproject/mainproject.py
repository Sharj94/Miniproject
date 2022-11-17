import time
import csv
import sys

def load_list_file(file_name):
    list = []
    with open(file_name, "r") as file: 
        csv_file = csv.DictReader(file)
        for row in csv_file: 
            list.append(row)
        return list

def save_to_file(file_name,list):
    if file_name == "products.csv":
        headers = ["Product","Price"]
        with open(file_name, 'w',newline='') as f:  
            w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in list:
                w.writerow(x)
        print("Products list save complete!")

    elif file_name == "orders.csv":
        headers = ["customer_name","customer_address","customer_phone_number","courier","Status"]
        with open(file_name, 'w',newline='') as f:  
            w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in list:
                w.writerow(x)
        print("Orders list save complete!")

    elif file_name == "couriers.csv":
        headers = ["Courier","Number"]
        with open(file_name, 'w',newline='') as f:  
            w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in list:
                w.writerow(x)
        print("Couriers list save complete!")

product_list = load_list_file("products.csv")
order_list = load_list_file("orders.csv")
courier_list = load_list_file("couriers.csv")

def enumerate_product():
    for i,x in enumerate(product_list):
        print(f"Number: {i}, {x}")

def add_product():
    Product = input("New product name: ")
    Price = float(input("New product price: "))
    new_product = {
        "Product": Product,
        "Price": Price 
    }
    product_list.append(new_product)

def delete_product():
    del product_list[int(input("Please enter the number of the item you'd like to delete: "))]

def update_product():
    try:
        index = int(input("Please enter the index of the product you'd like to ammend: "))
    except ValueError as VE:
        print("You can only input an integer!")
    except IndexError as IE:
        print("Please ensure that the index is inn range of th options.")
    else:
        item_to_update = product_list[index]
        keys = ["Product", "Price"]
        for key in keys: 
            input_by_user = input(f"New {key}: ")
            if input_by_user != "":
                if key == "Product":
                    item_to_update["Product"] = input_by_user
                elif key == "Price":
                    item_to_update["Price"] = float(input_by_user)
                else:
                    print("Please try again!")
                    continue
            else:
                menu()

def enumerate_order():
    for i,x in enumerate(order_list):
        print(f"Order number: {i}, {x}")

def add_order():
    c_name = input("Please enter your name: ")
    c_address = input("Please enter your address: ")
    c_phone_number = int(input("Please enter your phone number: "))
    enumerate_courier()
    courier = input("Please enter the name of a courier for the delivery: ")
    new_order = {
    "customer_name": c_name,
    "customer_address": c_address,
    "customer_phone_number": c_phone_number,
    "courier": courier,
    "Status": "Preparing..."
    }
    order_list.append(new_order)
    print("Order update is complete!")

def delete_order():
    del order_list[int(input("Please enter the number of the order you'd like to delete: "))]

def update_order():
    index = int(input("Please enter the index of the order you'd like to ammend: "))
    item_to_update = order_list[index]
    keys = ["customer_name", "customer_address", "customer_phone_number", "courier", "Status"]
    for key in keys: 
        input_by_user = input(f"new {key}: ")
        if input_by_user != "":
            if key == "customer_name":
                item_to_update["customer_name"] = input_by_user
            elif key == "customer_address":
                item_to_update["customer_address"] = input_by_user
            elif key == "customer_phonne_number":
                item_to_update["customer_phone_number"] = input_by_user
            elif key == "courier":
                enumerate_courier
                item_to_update["courier"] = input_by_user

def update_order_status():
    order_statuses = ["Preparing...", "Dispatched", "Delivered", "Cancelled"]
    updatedstatus = int(input("Select the order you'd like to update: "))
    for i,x in enumerate(order_statuses):
        print(f"{i}, {x}")
    new_status = int(input("Please enter the index of the new status: "))
    order_list[updatedstatus]["Status"] = order_statuses[new_status]

def enumerate_courier():
    for i,x in enumerate(courier_list):
        print(f"Index: {i}, {x}")

def add_courier():
    Courier = input("New courier name: ")
    Number = int(input("New courier number: "))
    new_courier = {
        "Courier": Courier,
        "Number": Number 
    }
    courier_list.append(new_courier)

def delete_courier():
    del courier_list[int(input("Please enter the number of the courier you'd like to delete: "))]

def update_courier():
    index = int(input("Please enter the index of the courier you'd like to ammend: "))
    courier_to_update = product_list[index]
    keys = ["Courier", "Number"]
    for key in keys: 
        input_by_user = input(f"new {key}: ")
        if input_by_user != "":
            if key == "Courier":
                courier_to_update["Courier"] = input_by_user
            elif key == "Number":
                courier_to_update["Number"] = int(input_by_user)

def product_menu():
    print( """
    Product menu
    -0- Back to Main Menu
    -1- Show Products
    -2- Add products
    -3- Delete products
    -4- Change products

    What would you like to do?
    
    """ )

    while True:

        product_option = int(input("Please select an option: "))

        if product_option == 0:
            menu()

        elif product_option == 1:
            enumerate_product()
            time.sleep(3)
            product_menu()

        elif product_option == 2:
            add_product()
            enumerate_product()
            time.sleep(3)
            product_menu()

        elif product_option == 3:
            enumerate_product()
            delete_product()
            enumerate_product()
            time.sleep(3)
            product_menu()

        elif product_option == 4:
            enumerate_product()
            update_product()
            enumerate_product()
            time.sleep(3)
            product_menu()

        else:
            print("""Uh-oh Invalid option
    Please try again!""")  
            product_menu()

def order_menu():
    print( """
    Order menu
    -0- Back to Main Menu
    -1- Show orders
    -2- Add new order
    -3- Change order
    -4- Delete order
    -5- Update order status

    What would you like to do?
    
    """ )

    while True:

        order_option = int(input("Please select an option: "))
    
        if order_option == 0:
            menu()

        elif order_option == 1:
            enumerate_order()
            time.sleep(3)
            order_menu()

        elif order_option == 2:
            add_order()
            time.sleep(3)
            order_menu()

        elif order_option == 3:
            enumerate_order()
            update_order()
            enumerate_order()
            time.sleep(3)
            order_menu()

        elif order_option == 4:
            enumerate_order()
            delete_order()
            enumerate_order()
            time.sleep(3)
            order_menu()

        elif order_option == 5:
            enumerate_order()
            update_order_status()
            time.sleep(3)
            order_menu()

        else:
            print("""Uh-oh Invalid option
    Please try again!""")  
            order_menu()


def courier_menu():
    print( """
    Order menu
    -0- Back to Main Menu
    -1- Show couriers
    -2- Add couriers
    -3- Delete couriers
    -4- Change couriers

    What would you like to do?
    
    """ )

    while True:

        courier_option = int(input("Please slect your option: "))

        if courier_option == 0:
            menu()

        if courier_option == 1:
            enumerate_courier()
            time.sleep(3)
            courier_menu()
        
        if courier_option == 2:
            add_courier()
            time.sleep(3)
            courier_menu()

        if courier_option == 3:
            enumerate_courier()
            delete_courier()
            time.sleep(3)
            courier_menu()

        if courier_option == 4:
            enumerate_courier()
            update_courier()
            enumerate_courier()
            time.sleep(3)
            courier_menu()

        else:
            print("""Uh-oh Invalid option
    Please try again!""")  
            order_menu()


def menu():
    print( """
    Welcome to Sajid's Delivery Service!
    
    Please choose one of the following options:
    -0- Exit the delivery service
    -1- Product menu
    -2- Order menu
    -3- Courier menu
    
    """ )
    main_option = int(input("Choice: "))

    while True:
        if main_option == 0:
            print("Saving files...")
            time.sleep(3)
            save_to_file("products.csv", product_list)
            save_to_file("orders.csv", order_list)
            save_to_file("couriers.csv", courier_list)
            print("Miss you already!")
            sys.exit()

        elif main_option == 1:
            product_menu()
    
        elif main_option == 2:
            order_menu()

        elif main_option == 3:
            courier_menu()

        else:
            print("""Uh oh, invalid option
            Please choose one of the following:""")
            menu()

menu()