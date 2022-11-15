import csv

# def open_file():
#     with open(filename) as file:
#         lines = csv.reader(file)


# filename = []

# def write_file():
#     with open(filename) as file:
#         fieldnames = ["Product", "Price"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     prod_name = input("Whats the name of the new product? ")
#     prod_price = input("Whats the price of the product?: ")
#     writer.writerow({"Product": prod_name, "Price": prod_price})


def load_list_from_file(file_name):
    list=[]
    with open(file_name, "r") as file: 
        csv_file = csv.DictReader(file)
        for row in csv_file: 
            list.append(row)
        return list


def save_to_file(file_name,list):
    headers = ["name","price"]
    with open(file_name, 'w',newline='') as f:  
        w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for x in list:
            w.writerow(x)


product_list = load_list_from_file("products.csv")

def add_product():
    name = input("Product name: ")
    price = int(input("Product price: "))
    new_product = {
        "name": name,
        "price": price 
    }
    product_list.append(new_product)

def update_product():
    print("Updating product....")
    index = int(input("index u want to delete: "))
    item_to_update = product_list[index]
    keys = ["name", "price"]
    for key in keys: 
        input_by_user = input(f"new {key}: ")
        if input_by_user != "":
            if key == "name":
                item_to_update["name"] = input_by_user
            elif key == "price":
                item_to_update["price"] = input_by_user

def delete_product():
    index = int(input("Please enter the number of the item you'd like to delete: "))
    item_to_delete = product_list[index]
    item_to_delete.remove()
    enumerate_prod()

def app():
    while True: 
        selected_option = int(input("""
         Select 0 to save to file and exit
         Select 1 to add product 
         Select 2 to update product
         Select 3 to delete product
         """))
        if selected_option == 0: 
            save_to_file("fakeproduct.csv", product_list)
        elif selected_option==1: 
            print("Calling the add_product function")
            add_product()
        elif selected_option==2:
            update_product()

app()