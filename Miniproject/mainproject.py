import time
import csv
import sys

from products_funct import enumerate_product,add_product,update_product,delete_product
from orders_funct import enumerate_order,add_order,update_order,update_order_status,delete_order
from couriers_funct import enumerate_courier,add_courier,delete_courier,update_courier


def load_list_file(file_name):
    list = []
    with open(file_name, "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            list.append(row)
        return list


def save_to_file(file_name, list):
    if file_name == "products.csv":
        headers = ["Product", "Price"]
        with open(file_name, "w", newline="") as f:
            w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in list:
                w.writerow(x)
        print("Products list save complete!")

    elif file_name == "orders.csv":
        headers = [
            "customer_name",
            "customer_address",
            "customer_phone_number",
            "courier",
            "Status",
        ]
        with open(file_name, "w", newline="") as f:
            w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in list:
                w.writerow(x)
        print("Orders list save complete!")

    elif file_name == "couriers.csv":
        headers = ["Courier", "Number"]
        with open(file_name, "w", newline="") as f:
            w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in list:
                w.writerow(x)
        print("Couriers list save complete!")


product_list = load_list_file("products.csv")
order_list = load_list_file("orders.csv")
courier_list = load_list_file("couriers.csv")


def product_menu():
    print(
        """
    Product menu
    -0- Back to Main Menu
    -1- Show Products
    -2- Add products
    -3- Delete products
    -4- Change products

    What would you like to do?
    
    """
    )

    while True:

        product_option = int(input("Please select an option: "))

        if product_option == 0:
            menu()

        elif product_option == 1:
            enumerate_product(product_list)
            time.sleep(3)
            product_menu()

        elif product_option == 2:
            add_product(product_list)
            enumerate_product(product_list)
            time.sleep(3)
            product_menu()

        elif product_option == 3:
            enumerate_product(product_list)
            delete_product(product_list)
            enumerate_product(product_list)
            time.sleep(3)
            product_menu()

        elif product_option == 4:
            enumerate_product(product_list)
            update_product(product_list)
            enumerate_product(product_list)
            time.sleep(3)
            product_menu()

        else:
            print(
                """Uh-oh Invalid option
    Please try again!"""
            )
            product_menu()


def order_menu():
    print(
        """
    Order menu
    -0- Back to Main Menu
    -1- Show orders
    -2- Add new order
    -3- Change order
    -4- Delete order
    -5- Update order status

    What would you like to do?
    
    """
    )

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
            print(
                """Uh-oh Invalid option
    Please try again!"""
            )
            order_menu()


def courier_menu():
    print(
        """
    Order menu
    -0- Back to Main Menu
    -1- Show couriers
    -2- Add couriers
    -3- Delete couriers
    -4- Change couriers

    What would you like to do?
    
    """
    )

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
            print(
                """Uh-oh Invalid option
    Please try again!"""
            )
            order_menu()


def menu():
    print(
        """
    Welcome to Sajid's Delivery Service!
    
    Please choose one of the following options:
    -0- Exit the delivery service
    -1- Product menu
    -2- Order menu
    -3- Courier menu
    
    """
    )
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
            print(
                """Uh oh, invalid option
            Please choose one of the following:"""
            )
            menu()

menu()
