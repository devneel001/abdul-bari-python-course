import math
u=1
v=1
z=1

velocity=(v**2-u**2)/z


#area of rectangle

l = int(input("Type the length"))
b = int(input("Enter the breadth"))
area = l*b
print("area is",area)

#convert km to miles   1km=0.621371 miles
kilo=float(input("enter the km value "))
mile=kilo*0.621371

print("the mile value of ",kilo,"is",mile)

radius=float(input("enter the float value of the radius of your damn circle "))
area=math.pi*radius**2

print("area of circle is ",area)

