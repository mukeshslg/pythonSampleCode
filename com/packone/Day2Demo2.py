import sys
import random
import os
from functools import reduce

import math

'''
Basic data types:
integer,String,float,complex numbers,booleans
'''

# print(type(10))
# print(type(10.5))
# print("integer max size:", sys.maxsize)
# print(sys.float_info.max)
#
# # real + imaginory
# f=9+4j #legal in python
# print(f)

# #cast
# print("cast:", type(int(23.99)))
# print("cast:", type(str(23)))
# print("cast:", type(chr(29)))

# #math function
# print("pow:", pow(2, 3))
# print("round:", round(4.6))
# print("sqrt:", math.sqrt(4))
# print("tan:", math.tan(2))
# print("sin:", math.sin(2))

# print("random:", random.randint(1, 20))
# num=0
# while num != 19:
#     print(random.randint(1, 20))
#     num = random.randint(1, 20)

# list
# ls1 = ["jack", True, 3345, 'superuser']
# print("List data:", ls1[0:2])
# ls1[0:2] = ['rayan', False]  # n-1 always
# print(ls1)
# ls1.remove(3345)
# print("after remove:", ls1)

# min in list
# print(min(['xolo', 'samson', 'Nokia', 'sony']))
phone_ls = ['xolo', 'samson', 'Nokia', 'sony', 'mi']
# print("actual list:", phone_ls)
# print(" ", phone_ls[1:-3])
# # reverse, etc
# print(phone_ls.reverse(), 'reersed list:', phone_ls)
# print(phone_ls[0:2])
# print("every other:", phone_ls[0::2])
# print("reverse list:", phone_ls[::-1])  # other way to reverse


# iter
# itr = iter(phone_ls)
# print(next(itr))
# print(next(itr))
# print(next(itr))

# range, print reverse
# print(list(range(1,10)))
# print(list(range(1, 10, 3)))

# for e in range(1, 10, 2):
#     print(e, ' ', end='')

# Set in python:unordered,unique value
# s1 = set(['xolo', 5])
# s2 = {'samson', 876, 5}
# print(type(s1))
# print("Length:", len(s2))
# s3 = s1 | s2
# s3.add(876)  # not allow dublicate value in set
# print("s3:", s3)
# s3.discard(5)
# print("s3:", s3)
# print("Random bacause  set is unordered list:", s3.pop())
# #******
# print(s3)
# print(s2)
# s3 |= s2
# print("s3|s2=", s3)
#
# # intersection: common in both set
# print(s1.intersection(s2))
# # difference
# print(s1.difference(s2))
# # clear
# s3.clear()
# print("s3:", s3)
# # frozenset is a set that cannot be changed in any way
# s3 = frozenset({'fixed', 'me', 'here', 7})

'''*************Functions in Python*****************'''


# def get_sum(num1: int = 1, num2: int = 1):
#     return num1 + num2
#
#
# print(get_sum(3,4))


# public static void fun(int ... a)
# {
#    // method body
# }

# multiple arguments
# def get_sum2(*args):
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum
#
#
# print(get_sum2(1, 2, 3, 4, 5, 34, 34))

#
# # return types:
# def work_nextgen(shifttiming):
#     return shifttiming + 1, shifttiming + 6
#
#
# s1, s2 = work_nextgen(9)
# print(s1, s2)
#
#
# # complex functions:
#
# def mult_fun(lists, func):
#     for x in lists:
#         print(func(x))
#
#
# mult_fun([9, 3, 9], work_nextgen)

'''*****************Lambda*********************'''
# Function without name: Sounds interesting ?
# -->also called as 'Lambda'
# example:
# def power(x, y):
#     print(x ** y)
#
#
# power(4, 2)
# # **-->functions are Object in python
# # can we pass functions inside function in python?? Yes!/No!
# # writing function name is u feel waste of time in some instance when u are using in only once?


# # lambda example/lambda expression in python:
# # lambda a:a**a <-- here function accepts arg a and returns a to power a. Just add lambda to work as function.
#
#
# f = lambda a, b: a ** b
# result = f(4, 2)
# print("result:", result)
#
#
# # Realtime use with- Filter, Map , Reduce:
# def check_iseven(n):
#     return n % 2 == 0
#
#
# nums = [56, 23, 4, 2, 9, 5, 77, 234]
# evens = list(filter(check_iseven, nums))
# print(evens)

# # for above example , lambda is best fit.
# check_iseven_lambda = lambda n: n % 2 == 0
#
# nums2 = [561, 232, 41, 22, 91, 52, 771, 234, 44]
# nums3 = [561, 232, 41, 22, "", None, 91, 52, 771, 2342, ""]
# evens = list(filter(check_iseven_lambda, nums2))
# print("with lambda and filter:", evens)
# # false value in pytho {empty dict},(empty tuple),[],None,
# print("filter data numb3:", list(filter(None, nums3)))
#
# # Team-Task: Write a lambda expression with list and filter to check max of 2 number.
# # print  result list.
#
# # Question: what if u have  been given chunk of data and ask to filter, apply sm operation and reduce it.
# # ????
#
# dbl = list(map(lambda a: a + 2, evens))
# print("with lambda and map:", dbl)
#
# # # Add two lists using map and lambda
# # numbers1 = [1, 2, 3]
# # numbers2 = [4, 5, 6]
# #
# # result = map(lambda x, y: x + y, numbers1, numbers2)
# # print(list(result))
#
# # reduce:
# sum = reduce(lambda a, b: a + b, dbl)
# print("with reduce:", sum)

# #reduce example:
# print("very simple in python:", reduce(lambda x, y: x + y, range(1, 10)))
