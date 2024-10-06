"""2nd Program """
# '''Compute area of following shapes: circle, rectangle, triangle, square, trapezoid and parallelogram.'''
            #1st method
     # Area of the circle
# r=int(input("enter radius of the circle"))
# circle=3.14 * r * r
# print("area of the circle=",round(circle,2))

#     #Area of the rectangle
# a=int(input("enter radius of the rectangle"))
# rectangle=l*b
# print("area of the rectangle=",round(rectangle,2))

            #2nd method 
import math
PI = math.pi
print("List of shapes")
print("1.Circle")
print("2.Rectangle")
print("3.Triangle")
print("4.Square")
print("5.Trapezoid")
print("6.Parallelogram")
n = int(input("enter your choice :-"))
print("whose you are want to calculate ")
if n == 1:
    r = int(input("enter radius"))
    A1 = PI * r * r
    print("area of the circle", round(A1, 2))
elif n == 2:
    s1 = int(input("enter length of the rectangle"))
    s2 = int(input("enter breadth of the circle"))
    r = s1 * s2
    print("area of the rectangle", round(r, 2))
elif n == 3:
    a = int(input("enter 1st side of the traingle"))
    b = int(input("enter 2nd side of the traingle"))
    c = int(input("enter 3rd side of the traingle"))
    d = (a + b + c) / 2
    print("area of the triangle:-", round(d, 2))
elif n == 4:
    side = int(input("enter side of the sqaure"))
    a4 = side * side
    print("area of the sqaure of the square", round(a4, 2))
elif n == 5:
    p1 = int(input("enter 1st parallel side of the trapozoid"))
    p2 = int(input("enter 2nd parallel side of the trapozoid"))
    d = int(input("enter distance of the || trapozoid "))
    a5 = 0.5 + (p1 + p2) * d
    print("area of the trapozoid", a5)
elif n == 6:
    base = int(input("enter base of the parallelogram"))
    height = int(input("enter height of the parallelogram"))
    a6 = base * height
    print("area of the parallelogram", a6)
else:
    print("you are enter wrong vlaue ")
