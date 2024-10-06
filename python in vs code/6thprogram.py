'''Write a program to determine whether a triangle is isosceles or not?'''
a=int(input("length first side of the triangle"))
b=int(input("length second side of the triangle"))
c=int(input("length third side of the triangle"))
print("first side =",a,"cm")
print("second side =",b,"cm")
print("third side =",c,"cm")
if a==b==c or a==b!=c or a==c!=b or b==c!=a:
    print("Traingle is isoceles")
else:
    print("Triangle is not isoceles")
