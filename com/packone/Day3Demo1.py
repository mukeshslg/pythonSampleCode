from functools import reduce

# def sum(a, b):
#     return a + b
#
#
# print(sum(1, 2))
#
#
# # multiple arguments
# def get_sum2(*args):
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum
#
#
# print(get_sum2(1, 2, 3, 4, 5, 5))
#
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


'''**********************'''

'''*****************Lambda*********************'''


# Function without name: Sounds interesting ?
# -->also called as 'Lambda'
# example:
# def power(x, y):
#     print(x ** y)
#
#
# power(4, 2)


# **-->functions are Object in python
# can we pass functions inside function in python?? Yes!/No!
# writing function name ,u feel waste of time in some instance when u are using it only once?


# lambda example/lambda expression in python:
# lambda a:a**a <-- here function accepts arg a and returns a to power a. Just add lambda to work as function.


# f = lambda a, b: a ** b
# result = f(4, 2)
# print("result:", result)
#
# f = lambda a, b: a + b
# print("result:", f(2, 55))
#
# print("result:", (lambda a, b: a + b)(2, 55))


# # Realtime use with- Filter, Map , Reduce:
def check_iseven(n):
    return n % 2 == 0


def check_iseven2(n, m):
    return max(n, m)


def check_iseven3(a,b):
    return a+b


nums = [56, 23, 4, 2, 9, 5, 77, 234]
evens = list(filter(check_iseven, [56, 23, 4, 2, 9, 5, 77, 234]))
print(evens)
print("filter:", filter(check_iseven, nums))
print("Map:", list(map(check_iseven2, [32, 34], [64, 56])))
'''
map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :
map(fun, iter)
param:
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Returns :
Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 
'''
print("reduce2: ", reduce(check_iseven3, [4, 4, 5]))  # reduce stores prev value

'''
Working : 
At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
print("not filter:")'''

# # for above example , lambda is best fit.
check_iseven_lambda = lambda n: n % 2 == 0

nums2 = [561, 232, 41, 22, 91, 52, 771, 234, 44]
nums3 = [561, 232, 41, 22, "", None, 91, 52, 771, 2342, ""]
evens = list(filter(check_iseven_lambda, nums2))
print("with lambda and filter:", evens)
# false value in pytho {empty dict},(empty tuple),[],None,
print("filter data numb3:", list(filter(None, nums3)))

# Team-Task: Write a lambda expression with list and filter to check max of 2 number.
# print  result list.

# Question: what if u have  been given chunk of data and ask to filter, apply sm operation and reduce it.
# # ????

dbl = list(map(lambda a: a + 2, evens))
print("with lambda and map:", dbl)
#
# # Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print("Map example add 2 list:", list(result))

# reduce:
sum = reduce(lambda a, b: a + b, dbl)
print("with reduce:", sum)

# reduce example:
print("very simple in python:", reduce(lambda x, y: x + y, range(1, 10)))

print(filter())
