# from unittest import mock

# import pytest

# import csv

# def load_list_file(file_name):
#     list = []
#     with open(file_name, "r") as file:
#         csv_file = csv.DictReader(file)
#         for row in csv_file:
#             list.append(row)
#         return list


# @pytest.fixture
# def product_list_with_no_products():
#     return []

# def test_product_file_repository_save():
#     # Setup
#     headers = ["Product", "Price"]
#     products = Products(Product("Fanta"), Product("Pepsi"))
#     file_path = "Miniproject/tests/mock_file.csv"
#     product_file_repository = ProductFileRepository(file_path)

#     # Assertions
#     read_product_lines = read_repository_save(file_path)
#     assert read_product_lines == []

#     product_file_repository.save(products)

#     read_product_lines = read_repository_save(file_path)
#     assert read_product_lines == ["Product(Fanta)", "Product(Pepsi)"]

#     # Teardown
#     open(file_path, "w").close() # <- Flushing the contents of the file

# from io import StringIO
# from csv import reader  

# in_mem_csv = StringIO("""\
# Product,Price
# Coke,3
# Pepsi,5
# Fanta,7""")  
# test_reader = reader(in_mem_csv, delimiter=',', quotechar='|')
# for line in test_reader:
#     print(line)