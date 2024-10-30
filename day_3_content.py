# day 3 content
# list examples
# my_list = [1, 2, "apple", 4.3, "tomato", 75]
# my_list.append("banana")
# my_list.remove(4.3)
# get_item = my_list[: : -1]
# print(get_item)

#tuple examples, list that should not change
# my_tuple = (10, 20, 30)
# print(my_tuple[0:2])

# dictionaries, personal cabinet
# dict_a = {"name":"milk", "cost": 6.50, "store": "Save-On", "amount": 2}
# dict_a["buy"] = True
# dict_a.pop("amount")
# print(dict_a)

#Sets, manage collection of unique values, no duplicates
# my_set = {"apple", "banaan", "chocolate", "kombuchua"}
# my_set.remove("banaan")
# print(my_set)
# set_1 = {"cheese", "bread", "deli meat"}
# set_2 = {"milk", "eggs", "bread"}
# diff_set = set_2.difference(set_1)
# print(diff_set)

#Exercise 1
# define tuples
# orange_tuple = ("oranges", 10.50, 7)
# banana_tuple = ("bananas", 5.50, 5)
# peach_tuple = ("peaches", 6.75, 6)
# # empty grocery list
# grocery_list = []
# # add tuples to grocery list
# grocery_list.append(orange_tuple)
# grocery_list.append(banana_tuple)
# grocery_list.append(peach_tuple)
# # print each item in grocery list, individually,using indexing
# print(grocery_list[0])
# print(grocery_list[1])
# print(grocery_list[2])
# # Calculate Total_cost using price * quantity
# oranges_total_cost = grocery_list[0][1] * grocery_list[0][2]
# bananas_total_cost = grocery_list[1][1] * grocery_list[1][2]
# peaches_total_cost = grocery_list[2][1] * grocery_list[2][2]
# # Print each item's name and total cost
# print(f"Total cost of {grocery_list[0][0]}: ${oranges_total_cost:.2}")
# print(f"Total cost of {grocery_list[1][0]}: ${bananas_total_cost:.2}")
# print(f"Total cost of {grocery_list[2][0]}: ${peaches_total_cost:.2}")

# Exercise 2
# Create three dictionaries containing grocery items
# apple_dict = {"name": "apple", "price": 0.50, "quantity": 5}
# banana_dict = {"name": "banana", "price": 0.30, "quantity": 7}
# orange_dict = {"name": "orange", "price": 0.70, "quantity": 3}
            
# # Calculate total cost of each , use the round()
# apple_dict["total_cost"] = round(apple_dict["price"] * apple_dict["quantity"], 2)
# banana_dict["total_cost"] = round(banana_dict["price"] * banana_dict["quantity"], 2)
# orange_dict["total_cost"] = round(orange_dict["price"] * orange_dict["quantity"], 2)

# # Total cost of each item
# print(f"Total cost of {apple_dict['name']}: ${apple_dict['total_cost']:.2}")
# print(f"Total cost of {banana_dict['name']}: ${banana_dict['total_cost']:.2}")
# print(f"Total cost of {orange_dict['name']}: ${orange_dict['total_cost']:.2}")

# Exercise 3
# Slicing and Sorting a List
# Slice and print: Everything from the second index onward.
# Slice and print: Everything up to (but not including) the fourth index.
# Use a negative index to get and print the third-to-last item in the list.
# num_list = [16, 47, 1, 3, 5, 9, 15, 2]
# print(num_list[2:])
# print(num_list[ :4])
# print(num_list[-3: ])
# # Sort list in descending order
# sorted_list = sorted(num_list, reverse=True)
# print(sorted_list)
# # Find and print length of num_list
# print(len(num_list))

# Exercise 4
# Create two sets that contain the following:
# dairy_set = {"milk", "butter", "cream", "yogurt", "cheese"}
# dessert_set = {"jello", "chocolate", "candy", "cookies", "muffins"}
# # Add the shared item, "ice_cream" to both sets that qualifies as both dairy and 
# dairy_set.add("ice_cream")
# dessert_set.add("ice_cream")
# # Remove item from each set that is not "ice_cream"
# dairy_set.remove("milk")
# dessert_set.remove("jello")
# # Find and Print intersection of the two sets
# common_items = dairy_set.intersection(dessert_set)
# print(common_items)

# Exercise 5: Update Changelog
# Exercise 6: Upload to GitHub


