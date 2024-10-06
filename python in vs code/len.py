upr=lwr=spl=0
str=input("Enter a string")
n=len(str)
i=0
while(i<n):
    if(str[i]>='a'and str[i]<='z'):
        lwr+=1
    elif (str[i]>='a' and str[i]<='z'):
        upr+=1
    else:
        spl+=1
    i+=1
print("total upper case =",upr)
print("total lower case =",lwr)
print("total special case =",spl)
