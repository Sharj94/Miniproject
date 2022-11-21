def enumerate_product(product_list):
    for i, x in enumerate(product_list):
        print(f"Number: {i}, {x}")


def add_product(product_list):
    product = input("New product name: ")
    price = float(input("New product price: "))
    new_product = {"Product": product, "Price": price}
    product_list.append(new_product)


def delete_product(product_list):
    try:
        del product_list[
            int(input("Please enter the number of the item you'd like to delete: "))
        ]
    except ValueError as VE:
        print("You can only input an integer!")
    except IndexError as IE:
        print("Please ensure that the index is in range of th options.")


def update_product(product_list):
    try:
        index = int(
            input("Please enter the index of the product you'd like to ammend: ")
        )
    except ValueError as VE:
        print("You can only input an integer!")
    except IndexError as IE:
        print("Please ensure that the index is inn range of th options.")
    else:
        item_to_update = product_list[index]
        keys = ["Product", "Price"]
        for key in keys:
            input_by_user = input(f"New {key}: ")
            if input_by_user == "":
                return
            if key == "Product":
                item_to_update["Product"] = input_by_user
            elif key == "Price":
                item_to_update["Price"] = float(input_by_user)
            else:
                print("Please try again!")
                continue
