# TODO Function Defintion

# def add(a,b):
#     c=a+b
#     print (c)
#     return
# ?recursive Function
# def fac(n):
#     if(n==1):
#         return 1
#     else:
#         return n*fac(n-1)
#!Function with no argument
# def display():
#     print("ashish")
#     return
# display()
# !Function with required  argument
# def add(a,b):
#     c=a+b
#     print(c)
# add(5,3)
#! Function with arbitary length argument
# def add(*n):
#     sum=0
#     for i in  n:
#         sum=sum+i
#         return sum
# print(add(1,6,7,8,9))
# print("sum is :-",add)
def add(*n):
   sum = 0
   for num in n:
      sum += num
   return sum
result = add(1, 2, 3)
print("sum is :-",result)
#!Function keyword based argument 
# def sum(a,b):
#     c=a+b
#     print("sum is =",c)
# x=int(input("enter a num1:-"))
# y=int(input("enter a num2:-"))
# sum(a=23,b=59) or
# sum(a=x,b=y)