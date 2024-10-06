n=(input("enter the range"))
num=1
while(num<=n):
    if(num==1 or num==2 or num==3):
        print(num)
else:
    i=2
    while(i<=num-1):
        if(num%i==0):
            break
        i=i+1
        if i==num:
            print(num)
            num=num+1