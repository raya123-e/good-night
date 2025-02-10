class student:
     def __init__(self,name,age,gender):
       self.name = name
       self.gender = gender
       self.age =age

     def study(self):
          print(self.name,"is studying")

stud1=student("Innocent","male",34)
stud2=student("Clarence","male",34)
stud3=student("Ann","female",34)
stud4=student("Jane","female",34)
stud5=student("Abigael","female",22)

print(stud1.name,stud1.gender,stud1.age)


