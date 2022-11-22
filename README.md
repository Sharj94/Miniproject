# Miniproject

## Project Background
The client required an app that they could utilise to complete all the business requirements behind the scenes of a pop-up coffee shop. We were drip fed the evolving requirements for the CLI application in python by the client over the course of 6 weeks which were implemented as required. 

## Client requirements
  
Here are the requirements set out by the client.
  
###  Week 1
  The initial requirements that were given by the client included creating a product, adding, deleting, and updating the product in a list. Additionally, the requirements inncluded the ability to view all the products that belonged to the list.
  
###  Week 2
  The client needs evolved and they now required the app to be able to create, view, and manipulate orders in addition to the product. Additionally the product was to be in the form strings and list of strings. The orders, on the other hand, were required to be a list of dictionaries. 
  
###  Week 3
  During this week the client specified that they needed to persist the data for orders and products in .txt form. They needed to be able to update the status of orders. They needed to be able to load the data when the application was started and saved at the closing of it. 
  
###  Week 4
  The client now needed the data to be persisted in .csv form for all three components of the app; couriers, orders and products. The client also needed for all of the data to be in the form of a dictionary and be persisted as a list of dictionaries. Furthermore, the client set out their needs of unit testing to be implemented in the programme.
  
###  Week 5 and 6 (tbc):
  The client now requires the application to utilise databases and sort orders by couriers and items.
  
## How did your design go about meeting the project's requirements?

In order to ensure that the requirements of the projects were fully met, I checked off the provided requirements to the needs of the client whilst ensuring functionality of the app. The importance of following the set requirements became evident during the first couple of weeks of the project as the client requirements didn't allow for other functionaility to be added. This allowed for less tech debt to buid up over the course of the project which had to be refactored/rewritten. Due to this, the project made the importance of following client requirements closely explicit. 

## How did you guarantee the project's requirements?

Flexibility was crucial in order to gurantee the fulfilment of the set requirements. As the needs and requirements of the client changed, the code had to adjust to those new requirements as well. For this to happen, refactoring the code, rewriting functions and exploring new ways of fulfilling the needs was essential and something that was followed throughout. The projects requirements were then guranteed through the use of unit testing throughout the core functionality of the application. This was done to ensure that the client received what they asked for and could also familiarise themselves with their new application. This would also help in future troubleshooting of the application should any problems arise.

## If you had more time, what is one thing you would improve upon?

One factor that became essential once introduced in the requirements and that would have reduced the built up technical debt was test driven development (TDD). Towards the end of the project it became evident that retrospectively writing tests for code is very time consuming and requires a lot of added time and effort. This is something that in the long term can lead to difficulties in refactoring the code and in simplifying it for new members of a team, that aren't familiar with the project and code thus far.

Likewise, I would have liked to work more on creating pure functions and combining thses with OOP. This would allow me to further strengthen my understadning of these two types of programming approaches and would also reflect in a more robust code. Likewise, I would like to have implemented databases and utilised SQL to do so. I would like to have also used various other tools such as Docker to upload my code and allow others to use as well.

## What did you most enjoy implementing?
