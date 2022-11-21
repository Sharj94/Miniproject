def enumerate_courier(courier_list):
    for i, x in enumerate(courier_list):
        print(f"Index: {i}, {x}")


def add_courier(courier_list):
    Courier = input("New courier name: ")
    Number = int(input("New courier number: "))
    new_courier = {"Courier": Courier, "Number": Number}
    courier_list.append(new_courier)


def delete_courier(courier_list):
    try:
        del courier_list[
            int(input("Please enter the number of the courier you'd like to delete: "))
        ]
    except ValueError as VE:
        print("You can only input an integer!")
    except IndexError as IE:
        print("Please ensure that the index is inn range of th options.")


def update_courier(courier_list):
    try:
        index = int(
            input("Please enter the index of the courier you'd like to ammend: ")
        )
    except ValueError as VE:
        print("You can only input an integer!")
    except IndexError as IE:
        print("Please ensure that the index is inn range of th options.")
    else:
        courier_to_update = courier_list[index]
        keys = ["Courier", "Number"]
        for key in keys:
            input_by_user = input(f"new {key}: ")
            if input_by_user == "":
                return
            if key == "Courier":
                courier_to_update["Courier"] = input_by_user
            elif key == "Number":
                courier_to_update["Number"] = int(input_by_user)
