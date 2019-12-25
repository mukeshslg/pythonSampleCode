'''
Exception handling:
Compile time: eg: syntactical error
logical eg:2+2=5
RunTime Error: Arithmetic exc 2/0
'''

# try:
#     print(2 / 0)
# except ArithmeticError as e:
#     print(e)
#     print("exception occured")
# except Exception as e:
#     print(e)
#     print("its exception")
# finally:
#     print("i will be executed Always....")


# Exception demo:
# try:
#     f = open("/Users/mukeshsah/Downloads/sample/sample.rtf")
# except FileNotFoundError as e:
#     print(e, " This is exception due to file not found")
# except Exception as e:
#     print(e, " some other exception")
# finally:
#     print("finally block")
# print("COntent text file", f.read())
# f.close()

# Exception demo2:
try:
    f = open("/Users/mukeshsah/Downloads/sample/sample.rtf")
    print(f.name)
    if f.name == '/Users/mukeshsah/Downloads/sample/sample.rtf':
        raise FileExistsError
except FileNotFoundError as e:
    print(e, " This is exception due to file not found")
except FileExistsError as e:
    print(e ," this is FileNotFoundError")
except Exception as e:
    print(e, " some other exception")
finally:
    print("finally block")
print("COntent text file", f.read())
f.close()

# Exception demo3:
# try:
#     f = open("/Users/mukeshsah/Downloads/sample/sample.rtf")
#     print(f.name)
#     if f.name == '/Users/mukeshsah/Downloads/sample/sample.rtf':
#         raise FileExistsError
# except FileNotFoundError as e:
#     print(e, " This is exception due to file not found")
# except FileExistsError as e:
#     print(e, " this is FileNotFoundError")
# except Exception as e:
#     print(e, " some other exception")
# finally:
#     print("finally block")
# print("COntent text file", f.read())
# f.close()
