import csv


def load_list_file(file_name):
    list = []
    with open(file_name, "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            list.append(row)
        return list


def save_to_file(file_name, list):
    if file_name == "data/products.csv":
        headers = ["Product", "Price"]
        with open(file_name, "w", newline="") as f:
            w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in list:
                w.writerow(x)
        print("Products list save complete!")

    elif file_name == "data/orders.csv":
        headers = [
            "customer_name",
            "customer_address",
            "customer_phone_number",
            "courier",
            "products",
            "Status",
        ]
        with open(file_name, "w", newline="") as f:
            w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in list:
                w.writerow(x)
        print("Orders list save complete!")

    elif file_name == "data/couriers.csv":
        headers = ["Courier", "Number"]
        with open(file_name, "w", newline="") as f:
            w = csv.DictWriter(f, headers, quoting=csv.QUOTE_MINIMAL)
            w.writeheader()
            for x in list:
                w.writerow(x)
        print("Couriers list save complete!")
