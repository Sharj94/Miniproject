def enumerate_order(order_list):
    for i, x in enumerate(order_list):
        print(f"Order number: {i}, {x}")


def add_order(order_list):
    courier = input("Please enter the name of a courier for the delivery: ")
    c_name = input("Please enter your name: ")
    c_address = input("Please enter your address: ")
    products = input("Please enter the index of the products you'd like to add: ")
    try:
        c_phone_number = int(input("Please enter your phone number: "))
    except ValueError as VE:
        print("You can only input a number!")
    else:
        new_order = {
            "customer_name": c_name,
            "customer_address": c_address,
            "customer_phone_number": c_phone_number,
            "courier": courier,
            "products": products,
            "Status": "Preparing...",
        }
        order_list.append(new_order)
        print("Order update is complete!")


def delete_order(order_list):
    try:
        del order_list[
            int(input("Please enter the number of the order you'd like to delete: "))
        ]
    except ValueError as VE:
        print("You can only input an integer!")
    except IndexError as IE:
        print("Please ensure that the index is in range of the options.")


def update_order(order_list):
    try:
        index = int(input("Please enter the index of the order you'd like to ammend: "))
    except ValueError as VE:
        print("You can only input an integer!")
    except IndexError as IE:
        print("Please ensure that the index is in range of the options.")
    else:
        item_to_update = order_list[index]
        keys = [
            "customer_name",
            "customer_address",
            "customer_phone_number",
            "products",
            "courier",
        ]
        for key in keys:
            input_by_user = input(f"new {key}: ")
            if input_by_user == "":
                return
            if key == "customer_name":
                item_to_update["customer_name"] = input_by_user
            elif key == "customer_address":
                item_to_update["customer_address"] = input_by_user
            elif key == "customer_phone_number":
                item_to_update["customer_phone_number"] = int(input_by_user)
            elif key == "products":
                item_to_update["products"] = input_by_user              
            elif key == "courier":
                item_to_update["courier"] = input_by_user


def update_order_status(order_list):
    order_statuses = ["Preparing...", "Dispatched", "Delivered", "Cancelled"]
    try:
        updatedstatus = int(input("Select the order you'd like to update: "))
    except ValueError as VE:
        print("You can only input an integer!")
    except IndexError as IE:
        print("Please ensure that the index is in range of the options.")
    else:
        for i, x in enumerate(order_statuses):
            print(f"{i}, {x}")
        new_status = int(input("Please enter the index of the new status: "))
        order_list[updatedstatus]["Status"] = order_statuses[new_status]
