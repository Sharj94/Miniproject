# Miniproject

## Project Background
The client required an app that they could utilise to complete all the business requirements behind the scenes of a pop-up coffee shop. We were drip fed the evolving requirements for the CLI application in python by the client over the course of 6 weeks which were implemented as required. 

## Client requirements
  
Here are the requirements set out by the client.
  
###  Week 1
The client's initial requirements included creating a product, adding, deleting and updating the product in a list. Additionally, the requirements included the ability to view all products in the list.

In order to fulfill these requirements, a simple list of strings for the products was created. Likewise, a simple function was made to ask for user input to populate the list. There was no data persistence at this point which is why the edits made to the list were only temporary in the working memory. It was very straightforward to implement these requirements due to their simple logic. It, however, did not demonstarte a working business application of an application.

###  Week 2
The client's requirements evolved and they wanted the app to be able to create, view and edit orders in addition to the products. Likewise, the product should be in the form of a string and, if many, a list of strings. The orders, on the other hand, needed to be a list of dictionaries.

In order to achieve all the functions the requirements set out, the code had to be refactored. To create dictionaries for the orders, key-value pairs were made and utilised. The data was still not being persisted which allowed more flexibility with the functions.
  
###  Week 3
This week, the client stated that they needed to persist the data for orders and products in the form of .txt files. They needed to be able to update the status of orders. They needed to be able to load the data when starting the application and save it when closing the application. 

Here we were instroduced to data persistence for orders and products to a .txt file. In order to achiveve this, new functions were added that allowed for the file to be opened, saved and closed with the new data. The code had to be refactored again to ensure functionality. 

###  Week 4
The client now needed the data to be persisted in .csv form for all three components of the app: couriers, orders and products. The client also wanted all data to be in dictionary form and be persisted as a list of dictionaries. In addition, the client specified that unit tests should be implemented in the programme.

In order to achieve the requirements for week 4, we were tasked with transferring our data from .txt files to .csv files for all three componenets (Products, orders and couriers). This meant that the code had to be rewritten to allow for the data to be loaded into lists before being manipulated by the user of the app. This threw a new challenge as up until this point the user was able to complete all the actions it needed inside the .txt file without having to transcribe it.
  
###  Week 5 and 6 (tbc):
The client now requires the application to utilise databases and sort orders by couriers and items.

These requirements are yet to be implemented in the near future. 

## How did your design go about meeting the project's requirements?

```
.
├── Makefile
├── data
│   ├── couriers.csv
│   ├── orders.csv
│   └── products.csv
├── functions
│   ├── couriers_funct.py
│   ├── file_functions.py
│   ├── orders_funct.py
│   └── products_funct.py
├── mainproject.py
├── requirements.txt
└── tests
    ├── test_file_persistence.py
    └── test_functions.py
```

In order to ensure that the requirements of the project were fully met, I matched the specified requirements with the client's needs while ensuring the functionality of the app. The importance of sticking to the given requirements became apparent in the first few weeks of the project, as the client's requirements did not allow for any additional functionality created by us. This allowed for less technical debt to be built up over the course of the project, which had to be refactored/rewritten. Through this project it became clear how important it is to stick exactly to the client's requirements as any other work may not be needed by the client and cause further delays.

### Demo order update function

```Python
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
```

### Demo - test of a function

```Python
def test_order_change():
    mock_index = 0
    mock_n_customer = "J Watson"
    mock_n_address = "221b Baker Street"
    mock_n_phone = 20875358
    mock_products = "1,2"
    mock_n_courier = "Moriarty"

    mock_list = [
        {
            "customer_name": "Tobias Kempe",
            "customer_address": "13 Bond Stree, SW1X3CE, London",
            "customer_phone_number": 7398485932,
            "courier": "Bob the builder",
            "products": "1,2",
            "Status": "Preparing...",
        }
    ]

    expected_outcome = [
        {
            "customer_name": "J Watson",
            "customer_address": "221b Baker Street",
            "customer_phone_number": 20875358,
            "courier": "Moriarty",
            "products": "1,2",
            "Status": "Preparing...",
        }
    ]

    mock_args = [
        mock_index,
        mock_n_customer,
        mock_n_address,
        mock_n_phone,
        mock_products,
        mock_n_courier,
    ]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        update_order(mock_list)
        assert mock_list == expected_outcome
```

## How did you guarantee the project's requirements?

Flexibility was crucial to ensure that the specified requirements were met. As the client's needs and requirements changed, the code also had to be adapted to these new requirements. Refactoring the code, rewriting functions and looking for new ways to meet the requirements were essential for this and were pursued consistently. The requirements of the project were then ensured through the use of unit tests for the core functions of the application. This ensured that the clients got what they required and were able to familiarise themselves with their new application. This would also help with future troubleshooting of the application should any problems arise.

## If you had more time, what is one thing you would improve upon?

One factor that became indispensable once added into the requirements, and which would have reduced the technical debt built up was continues testing. The ideal way of doing so would have been test-driven development (TDD). Towards the end of the project, it became clear that writing tests for the code after the fact was very time consuming and required a lot of extra time and effort. This is something that, in the long run, can lead to difficulties in refactoring the code and making it easier for new members of a team who are not previously familiar with the project and the code. Similarly, I would have liked to have more tests built into my code that focus on different paths and analyse different scenarios that the code might face after implementation.

Similarly, I would have liked to work more on creating pure functions and combining them with OOP. This would allow me to further deepen my understanding of these two types of programming approaches, which would also translate into more robust code. Similarly, I would have liked to implement databases using SQL. I would also have liked to use various other tools such as Docker to upload my code and make it available to others as well.

The use of repositories is something that would be quite useful in this project, if given more time, this would be something that would have been explored further. This would allow for more testing as well - through the use of mock repositories. However, it does come with its disadvantages, mainly adding another layer of complexity that would mean more difficulty for a reader in understanding the code.

## What did you most enjoy implementing?

One aspect I particularly enjoyed was adding encapsulation layers to the programme. Also, troubleshooting the app and working together to find a solution to these problems made the work an enjoyable experience. It was fun to learn how to write a programme that meets the given specifications and to see how it runs when you have no prior knowledge of the field.
