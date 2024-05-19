a=1

print(a.__sizeof__())       #int has nop fixed size in python

b=1234343434343454565465675677667677687879786756
print(b)
print(b.__sizeof__())

# lets say the variable a points to a memory location "1234" where 1 is stored. if I were to
#change the value of a in another line to 2 then the variable a would point to a separate location "1235" lets say
#this shows immutability of a value