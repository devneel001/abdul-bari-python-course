a=5
b=12
if a<b:
    z=True
else:
    z=False

print(z)
print(type(z))     #prints type of variable 



#for complex numbers j is used "a+ij" where j=sq.rt-1
#we can also use function complex


x=3.5j
print(type(x))
print(x)

y=complex(12,9)
print(y)

# when we assign a value to a variable directly in the code, its called a literal
i=123_456       #we use _ to separate numbers for ease of use(doesnt work if not between numbers)
print(i)

#bool is a predefined literal

f=12_2.3_33
print(f)

#using different number systems for representaion of integers 

decimal=10
binary=0b1010
octal=0o12
hexadecimal=0xA

print(decimal)
print(binary)
print(octal)
print(hexadecimal)

#only deciaml numbers are allowed for float

imag=0b101+12j        #other no systems can only be used in the real part of the complex no

print("imag")
print(imag)

price=input("type something")
print(price)