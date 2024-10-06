def fact(num):
    if(num==1):
        return 1
    else:
        return num*fact(num-1)
num=int(input("enter a num to find a factorial"))
print("factorial of the num ",fact(num))