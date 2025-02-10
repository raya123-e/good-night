# firstnumber, operator,second number(+ - / *)


first=int(input("Enter First number:"))
op=input("enter operator:")
exp= int(input("Enter second number:"))

if op=="+":
    print(first+exp)
elif op=="/":
    print(first/exp)

elif op=="-":
    print(first-exp)

elif op=="*":
    print(first*exp)

else:print("invalid operator")


