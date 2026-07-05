# def greet():
#     print("hello, Python learner!")

# greet()



# def square(num):
#     s = num*num 
#     return s 

# a = int(input("enter a number:"))
# print("the square of the number is :" , square(a))


# def full_name(first,last):
#     # name = first+" "+last 
#     # return name 

#     return f"{first} {last}"

# print(full_name("priyanshi","shah"))



# def calculate_area(length, width=10):
#     return length * width 

# print(f"area of the rectangle is {calculate_area(10,20)} cm")
# print(f"area of the rectangle is {calculate_area(5)} cm")


# sum = lambda a , b : a + b 
# print(f"sum of the given number is = {sum(10,20)}")



# Q5 create a list[1,2,3,4,5] and use map() with lambda function to get there square;

# square = lambda a : a*a 
# list1 = [1,2,3,4,5]

# print(list(map(square,list1)))

# Q6 factorial of a number 

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return fact(n-1) *n
    
# print(fact(5))

# # def fact(n):
#     for i in range(1,n):
#         f = f*i 
#         return f

# print(fact(5))


# Q7write a recursive function sum_of _digits(n) that returns the sum of  all digits of a given number 


# def sum_of_digits(n):
    
# #     # base case of recurssion
#     if n == 0:
#         return 0
#     sum = 0
#     for i in str(n):
#         sum = sum + int(i)
#     return sum

   

# print(sum_of_digits(555))


# num = 1234
# sum = 0
# for i in str(num):
#     sum = sum + int(i)

#     print(sum)




# Q8 import the math module and use it to find the 

# square of 144 & sin(90)

# import math

# a = math.sqrt(144)
# b = math.sin(math.radians(90))

# print(a,b)



# Q9 install and import the request module and use it to fetch data from github


# import requests
# a = request.get("https://api.github.com/")

# print(a.json)


# Q10) write a function increment() that has a local variable counter initialixe to zero and increments it by 1 every time its called observe the vale persists across the finction call 

# def increment():
#     counter = 0
#     counter = counter + 1
#     print(counter) 

# increment()
# increment()
# increment()
# increment()


# write a function multiply(a,b) that has a proper docstring explaination what it does. than use help(multiply) to disply the doc string  


# def multiply(a,b):
#     '''doc sring to explain the multiplication problem
#     input a = 1st number
#     input b  =  2nd number
#     result = a*b
#     return value of result
#      '''
#     return a*b

# print(multiply(2,4))
# help(multiply)

# print(multiply.__doc__)


# Q11 fibonaccis series 


# def fibonacci(n):
#     '''print 1st n fibonacci number'''
#     def fibo(k):
#         if k<=1:
#             return k
#         return fibo(k-2) + fibo(k-1)
    
#     for i in range(n):
#         print(fibo(i) , end = " ")

# fibonacci(5)


# def safe_div(a,b):
#     if b == 0:
#         print("invalid deniminator")
#         return
#     d = a / b
#     return d

# print(safe_div(5,0))

# main.py

from my_utils import is_even

# Example usage
print(is_even(4))   # True
print(is_even(7))   # False
