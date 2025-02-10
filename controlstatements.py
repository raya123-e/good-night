#A python programme that checks for room temperature
temperature=float(input("Enter temperature"))
if temperature >25:
    print("It is too hot")
else:
    print("It is too cold")


#A program that returns the largest number.
first= int(input("Enter first number:"))
second= int(input("Enter second number:"))
third= int(input("Enter third number:"))



if first > second and first>third:
    print(first, "is the largest number")
elif second>first and second>third:
    print(second,"is the largest number")

else:
    print("third is the largest number")
    #Program to check the number and differentiate whether number is even or not
number=15

if number==0:
    print(number,"is a neutral number")
elif number %2==0:
    print( number," is an even number")
else :
    print( number," is an odd number")

