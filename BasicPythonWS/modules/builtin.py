# import math

# print(math.sqrt(10))
# print(math.pow(2,5))
# print(math.factorial(5))

# from math import *

# print(sqrt(89))
# print(sin(1))

# from random import shuffle
# shuffle([])

# print(help('modules'))

# import http

# tasks of OS
import os
# /Users/Shalini/Desktop/Edforce_MichelinWS/BasicPythonWS/modules
# print(os.path.dirname(__file__))

# print(__file__) #/Users/Shalini/Desktop/Edforce_MichelinWS/BasicPythonWS/modules/builtin.py
# print(os.getcwd()) #/Users/Shalini/Desktop/Edforce_MichelinWS/BasicPythonWS
# print(os.path.isfile(__file__))
# print(os.path.isdir(__file__))
# # os.mkdir('dir1')
# # os.rmdir('dir1')
# os.chdir('/Users/Shalini/Desktop/Akhilesh')
# print(os.getcwd())

# print(os.listdir(os.getcwd()))
# os.mkdir('dir2')

import statistics

# print(statistics.mean([1,3,4,8,10]))

# print(statistics.median([1,3,4,8,10]))
# print(statistics.mode([1,3,4,8,10,3,3,2,1,4,5,3,5]))

import time

time.sleep(2)
print(time.time())
print(time.gmtime())
ob = time.strftime('%a %d %b %Y %H:%M:%S')


data = 'Tue, 01 Aug 2020 09:10:10'
obj = time.strptime(data,'%a, %d %b %Y %H:%M:%S')

print(type(obj))

