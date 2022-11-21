import couriers_funct
import mainproject

def enumerate_order(order_list):
    for i, x in enumerate(order_list):
        print(f"Order number: {i}, {x}")


def add_order(order_list):
    c_name = input("Please enter your name: ")
    c_address = input("Please enter your address: ")
    c_phone_number = int(input("Please enter your phone number: "))
    enumerate_courier(courier_list)
    courier = input("Please enter the name of a courier for the delivery: ")
    new_order = {
        "customer_name": c_name,
        "customer_address": c_address,
        "customer_phone_number": c_phone_number,
        "courier": courier,
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
        print("Please ensure that the index is inn range of th options.")


def update_order(order_list):
    try:
        index = int(input("Please enter the index of the order you'd like to ammend: "))
    except ValueError as VE:
        print("You can only input an integer!")
    except IndexError as IE:
        print("Please ensure that the index is inn range of th options.")
    else:
        item_to_update = order_list[index]
        keys = [
            "customer_name",
            "customer_address",
            "customer_phone_number",
            "courier",
            "Status",
        ]
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


def update_order_status(order_list):
    order_statuses = ["Preparing...", "Dispatched", "Delivered", "Cancelled"]
    updatedstatus = int(input("Select the order you'd like to update: "))
    for i, x in enumerate(order_statuses):
        print(f"{i}, {x}")
    new_status = int(input("Please enter the index of the new status: "))
    order_list[updatedstatus]["Status"] = order_statuses[new_status]
