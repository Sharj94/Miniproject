# Miniproject

## Project Background
The client required an app that they could utilise to complete all the business requirements behind the scenes of a pop-up coffee shop. We were drip fed the evolving requirements for the CLI application in python by the client over the course of 6 weeks which were implemented as required. 

## Client requirements
  
Here are the requirements set out by the client.
  
###  Week 1
The client's initial requirements included creating a product, adding, deleting and updating the product in a list. Additionally, the requirements included the ability to view all products in the list.

###  Week 2
The client's requirements evolved and they wanted the app to be able to create, view and edit orders in addition to the products. Likewise, the product should be in the form of a string and, if many, a list of strings. The orders, on the other hand, needed to be a list of dictionaries.
  
###  Week 3
This week, the client stated that they needed to persist the data for orders and products in the form of .txt files. They needed to be able to update the status of orders. They needed to be able to load the data when starting the application and save it when closing the application. 
  
###  Week 4
The client now needed the data to be persisted in .csv form for all three components of the app: couriers, orders and products. The client also wanted all data to be in dictionary form and be persisted as a list of dictionaries. In addition, the client specified that unit tests should be implemented in the programme.
  
###  Week 5 and 6 (tbc):
  The client now requires the application to utilise databases and sort orders by couriers and items.
  
## How did your design go about meeting the project's requirements?

In order to ensure that the requirements of the project were fully met, I matched the specified requirements with the client's needs while ensuring the functionality of the app. The importance of sticking to the given requirements became apparent in the first few weeks of the project, as the client's requirements did not allow for any additional functionality created by us. This allowed for less technical debt to be built up over the course of the project, which had to be refactored/rewritten. Through this project it became clear how important it is to stick exactly to the client's requirements as any other work may not be needed by the client and cause further delays.

## How did you guarantee the project's requirements?

Flexibility was crucial to ensure that the specified requirements were met. As the client's needs and requirements changed, the code also had to be adapted to these new requirements. Refactoring the code, rewriting functions and looking for new ways to meet the requirements were essential for this and were pursued consistently. The requirements of the project were then ensured through the use of unit tests for the core functions of the application. This ensured that the clients got what they required and were able to familiarise themselves with their new application. This would also help with future troubleshooting of the application should any problems arise.

## If you had more time, what is one thing you would improve upon?

One factor that became indispensable once added into the requirements, and which would have reduced the technical debt built up was continues testing. The ideal way of doing so would have been test-driven development (TDD). Towards the end of the project, it became clear that writing tests for the code after the fact was very time consuming and required a lot of extra time and effort. This is something that, in the long run, can lead to difficulties in refactoring the code and making it easier for new members of a team who are not previously familiar with the project and the code. Similarly, I would have liked to have more tests built into my code that focus on different paths and analyse different scenarios that the code might face after implementation.

Similarly, I would have liked to work more on creating pure functions and combining them with OOP. This would allow me to further deepen my understanding of these two types of programming approaches, which would also translate into more robust code. Similarly, I would have liked to implement databases using SQL. I would also have liked to use various other tools such as Docker to upload my code and make it available to others as well.

## What did you most enjoy implementing?

One aspect I particularly enjoyed was adding encapsulation layers to the programme. Also, troubleshooting the app and working together to find a solution to these problems made the work an enjoyable experience. It was fun to learn how to write a programme that meets the given specifications and to see how it runs when you have no prior knowledge of the field.
