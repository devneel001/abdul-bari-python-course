import math
print("put 1,-5 and 6 ploease")
a=int(input("enter value of a "))
b=int(input("enter value of b "))
c=int(input("enter value of c "))

r1=(-b+math.sqrt( b**2 - 4*a*c ))/(2*a)
r2=(-b-math.sqrt( b**2 - 4*a*c ))/(2*a)

print("roots are ",r1,r2)