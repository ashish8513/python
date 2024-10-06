#Print Geometric and Harmonic means of a series input by the user.
a=int(input("enter first term of gp:"))
r=int(input("enter common ratio:"))
n=int(input("number of terms:"))
print("geometric progrseesion:")
for i in range(0,n):
    term=a*pow(r,i)
    print(term,end=",")
PRO=1
for i in range(0,n):
    PRO=PRO*a
    a=a*r
print("\n Product:",PRO)
GM=pow(PRO,(1/n))
GM=round(GM,3)
print("Geomentric meana:",GM)