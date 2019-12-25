import os
import sys
import random

test_file = open("test.txt", "wb")
print("mode:", test_file.mode)
print(test_file.name)
test_file.write(bytes("writing data to file\n", "UTF-8"))
test_file.close()
test_file=open("test.txt","r+")
print(test_file.read())

#os module
os.remove("test.txt")