n=int(input("enter the range"))
for i in range(0,n):
    if(i==0 or i==1 or i==2):
        print(i)
    else:
        num=i
        for j in range(2,(num/2)):
            if(num/j==0):
                break
            if(j==(num/2)):
                print(num)
        

