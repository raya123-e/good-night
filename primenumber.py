# input, check whether number is a primenumber or not
num= int(input("Enter number:"))
if  num<=1:
    print("Value is not a prime number")
elif num>1:
    for x in range(2,num):
        if(num %x)==0:
            print(num,"Is not a prime number")
            print(x,"times",num//x,"is",num)
            break
    else:
        print(num,"Is a prime number")
else:
    print(num,"Is not a prime number")
