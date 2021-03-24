# Control Flow
# Conditional statements are used to control the flow of our program

# age = 15
# # If the user is above the age of 15 allow them to buy a ticket
# if age >= 15:  # if this condition is met/true the print statement will execute
#     print("Thank you, please proceed to your purchase")
# # If the user is under 15 years old do not allow them to buy a ticket
# elif age < 15:
#     print("Sorry, you are under age to watch this film")
# # else block gets executed if none of the above conditions are met
# else:
#     print("Oops, something went wrong, please try later")

# Exercise - as a user I would like to sell tickets according to the age of the user and category of the film
# age = U, PG, 12A, 15, 18
# user input to let us know the age
# casting implemented - age as integer
# display the age back to the user with appropriate message

# age = int(input("Please enter your age "))
# print(f"You are {age} years old")
#
# ratings = {
#     "Finding Nemo": 0,
#     "Jurassic Park": 0,
#     "Return of the King": 12,
#     "Blade Runner": 15,
#     "Trainspotting": 18
# }
#
# film = input("Which film do you want to see? Currently playing: Finding Nemo, Jurassic Park, Return of the King, Blade Runner, Trainspotting ")
#
# minimum_age = ratings[film]
#
# if age >= minimum_age:
#     print("Thank you, please proceed")
# elif age < minimum_age:
#     print("Sorry, you are too young to watch this film")
# else:
#     print("Sorry, something went wrong, please try again")

# Loops
# Syntax to create a loop
# for is python keyword variable then data_collection

# shopping_list = ["bread", "eggs", "milk", "oranges"]
#
# print(shopping_list)
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])
#
# # Let's use a for loop to iterate through our list
# for items in shopping_list:
#     print(items)

# Let's iterate through letters in a word
# for letter in "fruits":
#     print(letter)

# shopping_list = ["bread", "eggs", "milk", "oranges"]
# for items in shopping_list:
#     print(items)
#     if items == "milk":
#         # break is a key word
#         break  # at this point when milk is found when iterating the loop will stop

# Let's create a dictionary of our food bill so we can iterate through it
food_bill = {1: {"name": "James", "bill": "£1"}, 2: {"name": "Bond", "bill": "£2"}, 3: {"name": "Shah", "bill": "£3"}}

# # Print the names and the bill amount for each person
# for items in food_bill.values():
#     print(items["name"] + ": " + items["bill"])

# # Nested loops to iterate through the nested dictionary
# for item in food_bill.values():
#     for name_bill in item.values():
#         print(name_bill)

# Syntax while condition value:
# num = 0
# while num < 10:  # while True continue, if False stop
#     print(f"it's working -> {num}")
#     num += 1

# Added in more complexity
# num = 0
# while num < 10:  # while True continue, if False stop
#     print(f"it's working -> {num}")
#     if num == 4:  # if True the loop ends
#         break
#     num += 1

# Use case
user_prompt = True
while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit():  # isdigit() ensures the user input is in digits
        user_prompt = False
    else:
        print("Please enter your age in digits")
print(f"Your age is {age}")  # this line of code is only executed if the user enters age in digits

# Ensure the loop conditions are in your control to avoid going into an infinite loop
