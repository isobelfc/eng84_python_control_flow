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

age = int(input("Please enter your age "))
print(f"You are {age} years old")

ratings = {
    "Finding Nemo": 0,
    "Jurassic Park": 0,
    "Return of the King": 12,
    "Blade Runner": 15,
    "Trainspotting": 18
}

film = input("Which film do you want to see? Currently playing: Finding Nemo, Jurassic Park, Return of the King, Blade Runner, Trainspotting ")

minimum_age = ratings[film]

if age >= minimum_age:
    print("Thank you, please proceed")
elif age < minimum_age:
    print("Sorry, you are too young to watch this film")
else:
    print("Sorry, something went wrong, please try again")
