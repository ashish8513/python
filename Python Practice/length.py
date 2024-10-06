# def add_num(*args):
#    sum = 0
#    for num in args:
#       sum += num
#    return sum
# result = add_num(1, 2, 3)
# print('Sum is', result)

# result = add_num(10, 20, 30, 40)
# print('Sum is', result)
# result = add_num(5, 6, 7, 8, 9)
# print('Sum is', result)
def add(*n):
    sum=0
    for  i in  n:
        sum+=i
    return sum
result=add(1,2,3)
print("sum is :-",result)
        