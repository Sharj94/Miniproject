def add_product(product_list):
    product = input("New product name: ")
    price = float(input("New product price: "))
    new_product = {"Product": product, "Price": price}
    product_list.append(new_product)