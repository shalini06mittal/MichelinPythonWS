#provides access to functions and variables used to manipulate python runtime env
import sys
# arguments passed while executing a .py file
# ex: python sysdemo.py hello 1 2
print('argv',sys.argv)
#sys.exit()
print(sys.path) #python path
print(sys.version)
print(sys.platform)