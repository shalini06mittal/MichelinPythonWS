import module1
# from module1 import add, sub
print(module1.add(2,3))
print(module1.x)
#__name__ => __main__ for the current module in execution
print(__name__)

import module1 as m1
print(m1.sub(10,9))