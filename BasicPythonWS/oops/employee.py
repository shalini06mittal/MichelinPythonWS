class Employee:
    # self = for which emplopyee object
    # def __new__(cls,  name, email, phone, salary=0) :
    #     print('new called')
    #     obj = super().__new__(cls)
    #     return obj
    def __init__(self, name, email, phone, salary=0) -> None:
        print('inint called')
        self.__name = name
        self.email = email
        self.phone = phone
        self.salary = salary

    def setSalary(self, salary, commision=0):
        def f1():
            print('f1 called', salary)
        self.salary = salary +commision
        return f1
    # method overloading
    # def setSalary(self, salary, commision):
    #     def f1():
    #         print('f1 called', salary)
    #     self.salary = salary + commision
    #     return f1
    
    
    def __str__(self) -> str:
        return self.__name+' '+self.email+' '+ self.phone+' '+str(self.salary)

e1 = Employee('shalini','shal;ni@gmail.com','123123')
# print(e1.__name,e1.phone,e1.email)
# e2 = Employee('ajay','ajay@gmail.com','123123')
# print(e2.name,e2.phone,e2.email)
print(e1) # string representation of employee e1
# func = e1.setSalary(109080)
# print(e1)
# func()
e1.setSalary(1000, 100)
print(e1)
        