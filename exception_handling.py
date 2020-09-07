# EXCEPTION HANDLING
#
# def division(a,b):
#     try:
#         print(a / b)
#     except ZeroDivisionError as zerodv:
#         print("you can not divide by Zero ")
#         print("Error: ", zerodv)
#     except (NameError, TypeError) as err:
#         print("please check your input !")
#         raise err # this will raise regular error message and stop your executionK
#     finally: # always executed either try block or except block executed
#         print("finally block is executed.")
#
# division(45,15)
# division(45,0) # exception handling expected
# division(45,10)
# division(45, 'hello')
# division(100,15)
#
#
#
# filename = 'dat/inputData.txt'
# try:
#     with open(filename) as input_data:
#         print('2). reading the whole content and assigning to a variable')
#         contents = input_data.read()
#     print(contents)
# except FileNotFoundError as err:
#     print(err)
#
# print("Reading file is completed !")

from selenium import webdriver
driver = webdriver.Chrome
