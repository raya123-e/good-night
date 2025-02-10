


class employee:
    def __init__ (self,name,position,salary):
     self.name = name
     self.position = position
     self.salary=salary


              def info(self):
       print(self.position,"is earning",self.salary)

employee1= employee("John","CEO",50000)
print(employee1.name,employee1.position,employee1.salary)
employee1.info()
employee2=employee("June","Secretary",4500)
print(employee2.name,employee2.position,employee2.salary)
employee2.info()
employee3=employee("Jane","Auditor",4000)
print(employee3.name,employee3.position,employee3.salary)
employee3.info()
employee4=employee("Regan","Teacher",400)
print(employee4.name,employee4.position,employee4.salary)
employee4.info()
employee5=employee("Cornie","Tout",450)
print(employee5.name,employee5.position,employee5.salary)
employee5.info()




