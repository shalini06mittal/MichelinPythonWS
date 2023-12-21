'''
Python look up as follows:
1. In the current directory i.e other
2. Pyhton environment
'''

# import sys
# print(sys.path)
# sys.path.insert(0, '/Users/Shalini/Desktop/Edforce_MichelinWS/BasicPythonWS')
#LINUX : export PYTHONPATH='/Users/Shalini/Desktop/Edforce_MichelinWS/BasicPythonWS'
# WINDOWS : set PYTHONPATH='/Users/Shalini/Desktop/Edforce_MichelinWS/BasicPythonWS'
# from modules import module1

# print(module1.add(10,20))

from packagedemo.sample import messages
messages.welcome('hey')