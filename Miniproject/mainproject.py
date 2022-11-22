import time
import sys


from functions.file_functions import load_list_file, save_to_file

from functions.products_funct import (
    enumerate_product,
    add_product,
    update_product,
    delete_product,
)
from functions.orders_funct import (
    enumerate_order,
    add_order,
    update_order,
    update_order_status,
    delete_order,
)
from functions.couriers_funct import (
    enumerate_courier,
    add_courier,
    delete_courier,
    update_courier,
)


product_list = load_list_file('data/products.csv')
order_list = load_list_file('data/orders.csv')
courier_list = load_list_file('data/couriers.csv')


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

        try:
            product_option = int(input('Please select an option: '))
        except ValueError as VE:
            print('You can only input integers!')
        else:
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
                time.sleep(1)
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

        try:
            order_option = int(input('Please select an option: '))
        except ValueError as VE:
            print('You can only input integers!')
        else:
            if order_option == 0:
                menu()

            elif order_option == 1:
                enumerate_order(order_list)
                time.sleep(3)
                order_menu()

            elif order_option == 2:
                enumerate_courier(courier_list)
                enumerate_product(product_list)
                add_order(order_list)
                time.sleep(3)
                order_menu()

            elif order_option == 3:
                enumerate_order(order_list)
                enumerate_courier(courier_list)
                update_order(order_list)
                enumerate_order(order_list)
                time.sleep(3)
                order_menu()

            elif order_option == 4:
                enumerate_order(order_list)
                delete_order(order_list)
                enumerate_order(order_list)
                time.sleep(3)
                order_menu()

            elif order_option == 5:
                enumerate_order(order_list)
                update_order_status(order_list)
                enumerate_order(order_list)
                time.sleep(3)
                order_menu()

            else:
                print(
                    """Uh-oh Invalid option
        Please try again!"""
                )
                time.sleep(1)
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

        try:
            courier_option = int(input('Please select your option: '))
        except ValueError as VE:
            print('You can only input integers!')
        else:

            if courier_option == 0:
                menu()

            if courier_option == 1:
                enumerate_courier(courier_list)
                time.sleep(3)
                courier_menu()

            if courier_option == 2:
                add_courier(courier_list)
                time.sleep(3)
                courier_menu()

            if courier_option == 3:
                enumerate_courier(courier_list)
                delete_courier(courier_list)
                time.sleep(3)
                courier_menu()

            if courier_option == 4:
                enumerate_courier(courier_list)
                update_courier(courier_list)
                enumerate_courier(courier_list)
                time.sleep(3)
                courier_menu()

            else:
                print(
                    """Uh-oh Invalid option
        Please try again!"""
                )
                time.sleep(1)
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

    while True:
        try:
            main_option = int(input('Choice: '))
        except ValueError as VE:
            print('You can only input an integer!')
        else:
            if main_option == 0:
                print('Saving files...')
                time.sleep(3)
                save_to_file('data/products.csv', product_list)
                save_to_file('data/orders.csv', order_list)
                save_to_file('data/couriers.csv', courier_list)
                print('Miss you already!')
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
                time.sleep(1)
                menu()


menu()
