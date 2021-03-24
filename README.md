# Control Flow
- Conditional statements are used to control the flow of our program

## If, elif, else
- `if` checks whether a condition is met, and executes a block of code if it is met
- If the first conditional statement is not met, `elif` checks whether another condition is met, and executes if it is
- Multiple `elif`s may be present, and each one is checked in order until one is met and executes
- If none of the conditions are met, the `else` block is executed

## Loops

- Loops allow an action to be repeated multiple times - they iterate through the data
- They can be used with all kinds of data collections
- We use them to reduce the amount of duplicate code written, which saves time and reduces mistakes
- In addition, the number of repeats may not be a set number, e.g. dependent on the length of a list, or a certain condition being met
- Loops allow the number of repeats to be flexible
- `break` is a key word that will end the loop

### For loops
- We used a `for` loop to iterate through a list, and compared it to the process of manually repeating the line
```python
shopping_list = ["bread", "eggs", "milk", "oranges"]

print(shopping_list)
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])

# Let's use a for loop to iterate through our list
for items in shopping_list:
    print(items)
```
- We used a `for` loop to iterate through letters
```python
for letter in "fruits":
    print(letter)
```
- We used the key word `break` to end the loop when the condition was true
```python
shopping_list = ["bread", "eggs", "milk", "oranges"]
for items in shopping_list:
    print(items)
    if items == "milk":
        break
        # at this point when milk is found when iterating the loop will stop
```
- We used a `for` loop with a dictionary to print name and bill amount for each person
```python
food_bill = {1: {"name": "James", "bill": "£1"}, 2: {"name": "Bond", "bill": "£2"}, 3: {"name": "Shah", "bill": "£3"}}

# Print the names and the bill amount for each person
for items in food_bill.values():
    print(items["name"] + ": " + items["bill"])
```

### While loops