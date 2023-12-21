class Employee:
    # self = for which emplopyee object
    def __init__(self, name, email, phone, salary=0) -> None:
        print('inint called')
        self.name = name
        self.email = email
        self.phone = phone
        self.salary = salary
    def setSalary(self, salary):
        self.salary = salary
    def __str__(self) -> str:
        return self.name+' '+self.email+' '+ self.phone+' '+str(self.salary)

e1 = Employee('shalini','shal;ni@gmail.com','123123')
print(e1.name,e1.phone,e1.email)
e2 = Employee('ajay','ajay@gmail.com','123123')
print(e2.name,e2.phone,e2.email)
print(e1) # string representation of employee e1
e1.setSalary(121212)
print(e1)
        