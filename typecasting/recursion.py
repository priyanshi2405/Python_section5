# def fibo(n):
#     if n==0 or n==1:
#         return n
#     else:

#         return fibo(n-2) + fibo(n-1)


# for i in range(0,6):

# print("the fibonaccis series is" , fibo(5))


def fact(n):
    if n == 1:
        return n          

    else:

        f = n*fact(n-1)
        return f


# print(fact(5))