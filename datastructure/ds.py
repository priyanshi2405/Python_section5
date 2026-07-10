# question 1 
# fruits = ["apple", "banana" , "cherry"]
# print(fruits[0])
# fruits[1] = "orange"
# print(fruits)
# print(len(fruits))

# create a list of numbers 1 t0 10 and perform slicing

# li = []
# for i in range(1,11):
#     li.append(i)

# print(li)
# print(li[ : 3])
# print(li[-3:])

# list methods

# numbers = [5,2,9,1,7]
# numbers.sort()
# print(numbers)
# numbers.append(10)
# print(numbers)
# numbers.remove(2)
# print(numbers)


# q3 create a list and use insert method to insert a name

# li = ["alice", "bob" , "charli"]
# li.insert(1, "david")
# print(li)


# q4 tuples

# cordinates = (10 , 20)
# print(cordinates)
# print(cordinates[0],cordinates[1]) 
# cordinates[0] = 50
# print(cordinates)


# q5 convert tuple into list and back list to tuple

# cordinates = (10 , 20)
# corlist = list(cordinates)
# corlist[0] = 50
# print(corlist)
# cordinates = tuple(corlist)
# print(cordinates)


# q6 sets

# my_set = {1,2,3,3,4}
# print(my_set)
# my_set.add(5)
# print(my_set)
# my_set.remove(2)
# print(my_set)
# # is 2 in my_set

# Q7 tell the union interaction and difference of two sets 

# a = {1,2,3,4,5}
# b = {4,5,6}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))


# Q8 dictionary and its methods 

# student = {"name" : "jhon" , "age" : 21 , "grade" : "A"}
# print(student['name'])
# student["grade"] = "A+"
# print(student)
# print(student["city"])


# Q9 create a dictionary of 3 friendsand there phone numbers 
# use keys values and items 

# friends = {"raj":9090909090,"ram":909090909,"prem":8796546777}

# print(friends.keys())
# print(friends.values())
# for keys,  values in friends.items():
#     print(keys,values)

# Q10 create a list and remove all the dublicates usein sets 
# number = [1,2,3,3,4,5,6,6]
# uniqueList = list(set(number))
# print(number)
# print(uniqueList)


# Q11 give the dictionary of the product and find the product with the heighest price 

# 
# products = {"pen":20 , "pencil":10 , "book": 200 , "eraser":5}
# high = 0
# heightest_price = " "
# for pro in products:
#     if products[pro] > high:
#         heightest_price = products[pro]
#         high = pro

# print(products)
# print(high)
# print(heightest_price)

# products = {
#     "Laptop": 75000,
#     "Phone": 50000,
#     "Tablet": 30000,
#     "Monitor": 20000
# }

# highest_product = ""
# highest_price = 0

# for product in products:
#     if products[product] > highest_price:
#         highest_price = products[product]
#         highest_product = product

# print("Products:", products)
# print("Product with highest price:", highest_product)
# print("Price:", highest_price)


# Write a program that merges two dictionaries into one.

# dict1 = {
#     "a": 1,
#     "b": 2
# }

# dict2 = {
#     "c": 3,
#     "d": 4
# }

# merged_dict = dict1 | dict2

# print("Dictionary 1:", dict1)
# print("Dictionary 2:", dict2)
# print("Merged Dictionary:", merged_dict)

