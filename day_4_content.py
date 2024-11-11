### Day 4 Content
# tomato_dict = {"mane": "tomato", "cost": 2.25, "amount": 20, "backup": "canned tomato", "available": True}
# tomato_dict["available"] = False

# # if tomato_dict["available"] == False

# if tomato_dict["amount"] < 5 and not tomato_dict["available"]:
#     select_item = "cherry tomatoes"
#     select_amount = 1
# elif tomato_dict["amount"] >= 5 and not tomato_dict["available"]:
#     select_item = tomato_dict["backup"]
#     select_amount = 1
    
#     if tomato_dict["amount"] > 5:
#         select_amount = tomato_dict["amount"] /5
# else:
#     select_item = tomato_dict["mane"]
#     select_amount = tomato_dict["amount"]

# print(f"Let's buy {select_amount} {select_item}")

# if, elif, else
# if first_condition:
#     # Code to execute if first condition is true
# elif second_condition:
#     # Code to execute if first_condition is false but   
#       second_condition is true
# elif third_condition:
#     # Code to execute if first_condition and second_condition 
#       are false but third_condition is true
# else:
#     # Code to execute if none of the conditions are true

# price = 50
# if price < 30:
#     print("This is affordable")
# elif price < 40:
#     print("This is a bit expensive")
# else:
#     print("This is too expensive")

# a conditional placed inside another conditional, enabling complex,
# layered decision-making based on multiple criteria.
# every nested conditional should be indented to separate it from other conditionals. 
# weather = "sunny"
# temperature = 75
# # conditional 1: Check if the weathe is sunny or not
# if weather == "sunny":
#     # conditional 2: if sunny, check if temperature is above 70
#     if temperature > 70:
#         print("Wear sunglasses and a t-shirt.")
#     else: # matching else statment for conditonal 2
#         print("Wear sunglasses and a light jacket.")
# else: # matching else statment for conditional 1
#     print("Bring an umbrella.")

# Practice Exercises
# 1. Basic IF-Else to check if number is even or odd
# number = int(input("Give me a number: "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# 2. IF-ELIF-ELSE Chain: Check if temperature is Cold, Warm, Hot
# temperature = int(input("What is the temperature outside? "))
# if temperature <= 14:
#     print("It is Cold outside")
# elif 15 <= temperature <= 25:
#     print("It is Warm outside today!")
# else: 
#     temperature >= 26
#     print(" It is so Hot outside!")

# 3. Nested Conditionals

# age = int(input("Enter your age. "))
# citizenship = input("Are you a citizen (yes/no)").lower()
# if age >= 18:
#     if citizenship == "yes":
#         print("You are eligible to vote!")
#     else:
#         print("You are not eligible to vote")
# else:
#     print("Not eligible to vote: Must be 18 or older.")

# LOOPS
# grocery_list = [
# {"name": "milk", "amount": 2, "cost": 2.5, "store": "Walmart",
#  },
# {"name": "bread", "amount": 1, "cost": 1.5, "store": "Target",
#  },
# {"name": "eggs", "amount": 12, "cost": 3, "store": "Costco",
#  },
# ]
# for item in grocery_list:
#     print(f"{item['name']} - {item['amount']} - {item['cost']} - from {item['store']}")

# While Loop: Keeps running until condition changes

# grocery_list = [
# {"name": "milk", "amount": 2, "cost": 2.5, "store": "Walmart",
#  },
# {"name": "bread", "amount": 1, "cost": 1.5, "store": "Target",
#  },
# {"name": "eggs", "amount": 12, "cost": 3, "store": "Costco",
#  },
# ]

# while True:
#      command = input("Type a command add or done: ")
#      if command == "done":
#          break

#      name = input("Enter item name: ")
#      amount = int(input("Enter amount: "))
#      cost = float(input("Enter cost: "))
#      store = input("Enter store: ")

#      new_item_dict = {"name": name, "amount": amount, "cost": cost, "store": store}
#      grocery_list.append(new_item_dict)

# print(f"{name} was added to grocery list")

# for item in grocery_list:
#      print(item)

# Nested Loop:
# shape_list = ["circle", "square", "triangle"]
# color_list = ["red", "yellow", "green"]
# for shape in shape_list:
#     for color in color_list:
#         print(f"{shape} is {color}")

# Break
#grocery_list = ["milk", "bread", "eggs", "cheese", "apples", "bananas"]
# item_to_find = "cheese"

# for item in grocery_list:
#     if item == item_to_find:
#         print(f"found {item_to_find}")
#         break
# else:
#     print(f"{item_to_find} not dound in the grocery list")

# number_of_items = 0

# while number_of_items < 5:
#     print("adding items to the list")
#     number_of_items += 1

# for item in grocery_list:
#     if item in fruits:
#         continue
#     print(f"Non-fruit item: {item}")

# Exercise 1: Grocery item categorization using Conditional Statements

# food_items = ["apple", "bread", "milk"]
# household_itmes = ["soap", "detergent", "paper towels"]
# # Ask user to input a grocery item
# item = input("Enter a grocery item: ").lower()
# # Use Conditional statements to categorize the item
# if item in food_items:
#     print(f"{item.upper()} is a food item.")
# elif item in household_itmes:
#     print(f"{item.upper()} is a household item.")
# else:
#     print("unknown item")

#Exercise 2 Make a Burger with a While Loop

items_list = [
    {"name": "spaghetti", "cost": 3.00, "amount": 1},
    {"name": "ground beef", "cost": 10.00, "amount": 1},
    {"name": "tomato sauce", "cost": 4.00, "amount": 1},
    {"name": "parmesan cheese", "cost": 5.00, "amount": 1},
    {"name": "garlic", "cost": 2.00, "amount": 1},
    {"name": "olive oil", "cost": 3.50, "amount": 1},
    
]
# Create Variables
shopping_list = []
budget = 27.50
total_cost = 0
index = 0
# Create while loop to add items to shopping list within budget
while total_cost <= budget and index < len(items_list):
    item = items_list[index]
    item_total_cost = item["cost"] * item["amount"]

    if total_cost + item_total_cost > budget:
        break

    shopping_list.append(item["name"])
    total_cost += item_total_cost
# Exercise 5 Error Handling with try-except
    #index += "1"
    index += 1

# Exercise 3 Extending Logic with Nesting
    # Print each item in the shopping list
    for item in shopping_list:
        print(item)
    print("-----------")
# Exercise 4 Breaking the Loop
    if "spaghetti" in shopping_list and "ground beef" in shopping_list and "tomato sauce" in shopping_list:
        print(f"We can make pasta with tomato sauce and meatballs for {total_cost}!") 
    # Print shopping list
    print(shopping_list)











    


