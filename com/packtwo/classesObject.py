'''class and object in python:'''

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)
#
#
# # basically model object with real world object by defining capabilities and attributes
#
# class Squares:
#
#     def __init__(self, bmi=0, weight=0):  # calls when inst is created of class square
#         self.bmi = bmi
#         self.weight = weight
#
#     # self: refer to object u are working with
#
#     # @property
#     def getWeight(self):
#         return self.weight
#
#     def getBmi(self):
#         return self.bmi
#
#     # @weight.setter
#     def set_weight(self, val):
#         # if val
#         self.weight = val
#
#     # else:
#     #     print("please enter digit.")
#     #
#
#     def set_BMI(self, value):
#         # if
#         self.bmi = value
#         # else:
#         #     print("please enter digit.")
#
#
# ob1 = Squares(1, 2)  # object created
#
# print(ob1.weight)
# ob1.set_weight(60)
# print("getWeight:", ob1.getWeight())
# ob1.set_BMI(554)
# print("getBMI", ob1.getBmi())
#
# '''*******************Inheritance in python********'''
#
# '''
# Types:
# 1.single ton
# 2.multiple
# 3.multilevel
# '''
#
#
# class A:
#     def feature1(self):
#         print("Feature 1 working")
#
#     def feature2(self):
#         print("Feature 2 working")
#
#     def featureUnknown(self):
#         print("Feature unk working A")
#
#
# class B:
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#
#     def featureUnknown(self):
#         print("Feature unk working B")
#
#
# class C(A, B):
#     def feature5(self):
#         print("Feature 5 working")
#
#
# a1 = A()
#
# a1.feature1()
# a1.feature2()
#
# b1 = B()
#
# c1 = C()
# c1.featureUnknown()
#
# '''*******Constructor in Inheritance:'''
#
# print("#####constructor inheritance demo:#####")
#
#
# class AA:
#
#     def __init__(self):
#         print("A class constructor")
#
#     def feature1(self):
#         print("Feature 1 working")
#
#     def feature2(self):
#         print("Feature 2 working")
#
#     def featureUnknown(self):
#         print("Feature unk working A")
#
#
# class BB(AA):
#     def __init__(self):
#         print("b class constructor")
#
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#
#     def featureUnknown(self):
#         print("Feature unk working B")
#
#
# a1 = AA()
#
# b1 = BB()
#
# # what super().__init__() does?
#
# '''*******************Multilevel*****************'''
# print("#######Multilevel#########")
#
#
# class AAA:
#
#     def __init__(self):
#         print("AAA class constructor")
#
#     def feature1(self):
#         print("Feature 1 working")
#
#     def feature2(self):
#         print("Feature 2 working")
#
#     def featureUnknown(self):
#         print("Feature unk working AAA")
#
#
# class BBB:
#     def __init__(self):
#         print("BBB class constructor")
#
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#
#     def featureUnknown(self):
#         print("Feature unk working BBB")
#
#
# class CCC(AAA, BBB):
#
#     def dummyc(self):
#         print("dummy c")
#
#     def __init__(self):
#         super().__init__()
#         print("CCC class constructor")
#
#
# a2 = AAA()
#
# b2 = BBB()
#
# c2 = CCC()
#
# '''*******MRO: Method resolution order:'''
# # 1. order starts from left to right
# # 2. eg: class CCC(AAA, BBB):<----left to right always
# # 3. for methods same rule is applicable in python.super().baseMethod()
#
#
# ''' ***************PolyMorphism**********************'''
# # --->Many forms
# print("#######PolyMorphism#########")
# x = "Mukesh"
# x = 777
#
#
# # Dynamic typing in python:
# # -->above type is change from string to integer
# # -->here x is just variable which holds data somewhere in memory, variable is name for that allocated memory
# class Intellij:
#     def compile(self):
#         print("compile and check syntax")
#         print("generate .class file")
#         print("ready to execute")
#
#
# class Windows:
#     def win10(self, java):
#         java.compile()
#
#     def winVista(self, version):
#         if version >= 12:
#             print("supports intellij")
#         else:
#             print("oops-does-not support IntellijIdea")
#
#
# # type defined by user here
# intellij = Intellij()
# win = Windows()
# win.win10(intellij)
# win.winVista(11)

# #TEAM-Task: write a class to check pycharm supports in 3 major version of linux


'''**************************operator overloading****************'''

#


# ********************************
# class Student:
#     def __init__(self, m01, m02):
#         self.m01 = m01
#         self.m02 = m02
#
#
# s01 = Student(76, 66)
# s02 = Student(88, 87)
#
# s03 = s01 + s02  # will get error:unsupported operand type


# ********************************


# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     # overloading here:
#     def __add__(self, other):
#         m1 = self.m1 + self.m2
#         m2 = other.m1 + other.m2
#         s3 = Student(m1, m2)  # calling
#         return s3
#
#     def __gt__(self, other):
#         if self.m1 + other.m2 > self.m1 + other.m2:
#             return True
#         else:
#             return False
#
#     # def __str__(self):
#     #     print(self.m1, self.m2)
#
#
# s1 = Student(66, 55)
# s2 = Student(88, 81)
#
# s3 = s1 + s2
#
# print("m1:", s3.m1)
# print("m2:", s3.m2)
# # #** comparing two instance with > or _gt_ ,with overloading
# res = s1 > s2
# if s1 > s2:
#     print("s1 win")
# else:
#     print("s2 wins")
#
# print(s3)

# # Note: any operation we perform it calls its inbuilt method


'''********* Note:method overloading is not der in python.Cannot create 2 methods with same name.****'''

# -->how do we do it in python?

# Python is cool believe me.

# method overloading:
# class Employee:
#     def detail(self, name, phno, email, linked_in_Id):
#         print("Employee detail:", name, ",", phno, ",", email, "linkedin-ID:", linked_in_Id)
#
#
# e1 = Employee()
# e1.detail("john", 909098998, "john@yahoo.com","JOh@lnk.co")

'''***********Method Overriding***********'''

class Phone:
    def key(self, qwerty):
        print("phone has got ", qwerty, " Key")


class Samson(Phone):
    def key(self, qwerty, touchScreen=None):
        print("phone has got ", qwerty, " Key")
        print("with latest touchscreen ", touchScreen, "version")


s1 = Samson()
s1.key("qwerty1.1")


# # Team-Task: Design a class with covers inheritance between department and employee and also include
# concept of overloading(in department class) and overriding.

'''********Iterator*****'''
# num = [4, 6, 7, 3, 43, 4545]
# it=iter(num)
# print(it.__next__())
# print(it.__next__())


'''###############COMPLEX ONE IS EASY ################'''

# def div(a, b):
#     print(a - b)
#
#
# def calc_method(func):
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)
#
#     return inner
#
#
# calc_method(div)
#
# r1(3, 5)


# #Team-Task: Design functions and separate it as module.eg: calculator.
'''
Hint:
import Util
from Util import *
from Util import ArrayList

'''

# class myclass:
#     def __init__(self):
#         print("Dcon")
#
#     def mydisplayfun(self, arg1):
#         print("mydisplayfun", arg1)
#
#
# ob = myclass()

print(list(map((lambda ls1, ls2: max(ls1, ls2)), [2, 4, 6, 77, 89], [2, 5, 454, 45445])))

ini_dict = {'a': 1, 'b': -2, 'c': -3, 'd': 7, 'e': 0}

# printing initial dictionary
print("initial lists", str(ini_dict))

# filter dictionary such that no value is greater than 0
result = dict(filter(lambda x: x[1] >= 0.0, ini_dict.items()))
result = dict(result)

print("resultant dictionary : ", str(result))

# more lambda example:
print((lambda x, y: x if x > y else y)(3,5))
