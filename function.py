# Built in functions/standard-library functions

y = max(45,89,75,44,41,4,84,81,12,1)
print(y,"is the maximum value")
x=min(12,1,4,8,55,88,59,9,6,4444,4464,11555)
print(x,"is the minimum value")


#User defined functions
def school():
    print( "eMobilis")

school()

def add():
    num1=5
    num2=4
    print(num1+num2)
add()
#parameters/variable and argument/value

def multiply(a,b):
    print(a*b)


multiply(7,9)
multiply(45,7)

def employee(name,age,gender,salary,position):
    print(name,age,gender, salary ,position)

employee("Maureen","24", "female",10000000,"Ceo")
employee("Julius","24", "male",100000,"Coo")
employee("Kevin","24", "female",10000,"Cool")
employee("Big Boss","24", "male",10000000,"marine")
employee("Fushiguro","24", "male",10000,"Data Analsyst")
employee("Nobara","24", "female",1000,"Secretary")
employee("Sukuna","24", "female",10000000,"watchdog")
employee("Gojo","24", "male",10000000,"teacher")
employee("Gheto","24", "male",10000000,"assistant")



def patient(fullname, gender, age,disease):
    print(fullname,gender,age,disease)

patient("Charles Owuor", "male","45","Lung Cancer")
patient("Julius Oloo", "male","12","Brain Tumor")
patient("Hulio Kabete", "male","48","HIV")
patient("Janet Wawili", "female","34","Gingivitis")
patient("Jane Doe", "female","24","Halitosis")
patient("Betty Chang", "female","84"," Eye Cataract")




