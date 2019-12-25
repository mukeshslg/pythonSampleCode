import random

print("Hello python!!!")
# this is comment
'''
Muktiline comment in python
'''
var = 99
print("I got good marks in maths", var)

print("\nHello" * 5)

print("Python is awesome ", end="")
print(" Its best programming", end="")
print("language")

# + - / * %
# *->exponential calculation
# //->perform division and descard
print("5//2=", 5 // 2, "5**2=", 5 ** 2)

'''***************Data Type*************'''
# 5 main python data types:
# Number, String, List, Tuples, Dictionaries
print("List:")
my_list = ['nisha', 'sandeep', 'dr.sandeep', 'sathya', 'laxman']
my_list.append('shendil')
print(my_list)
del my_list[3]
print(my_list)

planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'second last? Neptune']
orginal_planet_list = [planet_list]
print(planet_list[0])
print(len(planet_list))
planet_list[0] = 'firstplanet'
print(planet_list[0])
print(planet_list[0:3])
planet_list2 = ['pluto', 'other']
total_planet_list = [planet_list, planet_list2]
print(total_planet_list)
print("\n" * 5)
print(total_planet_list[1][1])
# append
total_planet_list.append('some more planets')
print(total_planet_list)
# insert
planet_list.insert(1, 'i am new')
print("planet_list:", planet_list)
# short,reverse
print("planet_list sorted:", planet_list.sort(), planet_list)
print("reverse:", planet_list.reverse(), "\n reversed list:", planet_list)
print("\n" * 5)

print("orginal:", planet_list)
# len,max,min
print("\nlength:", len(planet_list), " Max/min:", max(planet_list), ":", min(planet_list))
'''******************Tuples*****************
# data cannot be changed, to modify need to convert to list
# '''
tuple_var = (4, 6, 9, 4, 1)
print("Tuple:", tuple_var)
new_list = list(tuple_var)
new_list[0] = 99
print(new_list)
# len(),max(),min()<--works for tuple
print(tuple(new_list))
print(len(tuple_var))

'''****************Dictionary*****************'''
mysampleDict = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4}
print(mysampleDict.get('apr'))
print("Keys:", mysampleDict.keys(), "values:", mysampleDict.values())
my_dict = {'name': 'john', 'age': 29, 'sex': 'Male', 'e-mail': 'john@yahoo.com'}
print("age:", my_dict.get('age'))
my_dict.__setitem__('age', 99)
print(my_dict)
# del to delete
del my_dict['age']
print("age:", my_dict.get('age'))

my_dict['age'] = 31
print("item:", my_dict.items())
# len, Keys
my_dict.get('e-mail').__len__()
print("Keys:", my_dict.keys(), " \nvalues:", my_dict.values())
my_dict2 = {'e-mail': ['john007@gmail.com', 'john@yahoo.com']}
# # update
my_dict.update(my_dict2)
print(my_dict)
'''**********conditional statement '''
# age = int(input("Enter your age:"))
# if age >= 18 and age <= 80:
#     print("you are eligible to drive")
#      print("you are eligible to drive")
# elif age < 18:
#     print("You are not eligible")
# else:
#     print("Invalid age")
# for

# javacode:
# for(i=0;i<=5;i++){
#     Syso("jhdjhsd");
# }

# in python
for x in range(0, 5):
    print(x)

print("printing list item:")
for p in planet_list:
    print(p, ':', end="")

print("\n", planet_list)

food_list = {'matar paneer', 'sahi paneer', 'grill paneer', 'chicken lollipop', 'noodles', 'mashroom pulao'}
print("\n________food list:____________")
for item in food_list:
    print(item, end='')
print("\n")
for x in [2, 4, 6, 9, 10]:
    print(':', x, '', end='')
numb_list = [[2, 4, 6, 8], [99, 3, 45, 21, 11], [13, 16, 61, 1]]
# 2D array using for loop
print('\nnumlist:')

for x in range(0, len(numb_list)):  # n-1
    for y in range(0, 4):
        print("", numb_list[x][y], end="")

# while Loop: when u have no idea how many times u need to loop
# print("\n"*3, " Random no with while loop:")
# num_random = random.randrange(0, 3)
# i = 0
# while (num_random != 1):
#     print("trying to print random nop")
#     print(num_random, ':', end='')
#     num_random = random.randrange(0, 20)


print("\n#######while data:######")
# ------------------------------
i = 0
while i <= 20:
    if i % 2 == 0:
        print(i, '', end='')
    elif i == 19:
        break
    else:
        i += 1
        continue
    i += 1
