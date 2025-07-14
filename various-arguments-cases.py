import re
# if we are not sure no. of arguments while calling printAllNames() method

# def printAllNames(*args):
#     print(args);
#
#
# printAllNames('s','g','f')
# def play():
#     print("hello world")
#     print("hello world 2")
#     print("hello world 3")
#
# sushi = lambda a,b: a+b
#
# print(sushi(2,3))
#
# for i in range(0, 10, 2):
#     if(i==4):
#         pass
#     print(i)
#create list of odd numbers
# oddNumbers = [x for x in range(10) if x%2!=0]
# #create list of prime numbers
# primeNumbers = [x for x in range(10) if x%2==1]
# print(primeNumbers)

# #iterate list
# listNums = [1, 3, 5, 9, 3, 0]
# for x in listNums:
#     print(x)


def customExcep():
    try:
        a = 2/0
        print(a)
    except ZeroDivisionError:
        print("division  by zero exception")


customExcep()