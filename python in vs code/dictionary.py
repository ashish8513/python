def insert(dict,i):
    dict.update({i:input("enter subject name")})
    return
def delete(dict):
    i=int(input("Which particular subject you want to delete Enter its Key"))
    del dict[i]
    return
def update(dict):
    index=int(input("which particular Key you want to Update"))
    dict.update({index:input("enter subject name")})
    return
dict={}
n=int(input("how many practical subjects you have"))
for i in range(n):
    dict.update({i:input("enter subject name")})
k=1
while(1==1):
    print("press 1 for insertion /n press 2 for deletion /n press 3 for updation /n press 4 for exit /n 5 for display")
    ch=int(input("enter your choice"))
    if(ch==1):
        k+=1
        insert(dict,k)
    elif(ch==2):
        delete(dict)
    elif(ch==3):
        update(dict)
    elif(ch==5):
        print(dict)
    elif(ch==4):
        break
    else:
        print("you have entered a wrong value")
        