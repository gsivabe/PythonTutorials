#Example for Data Type
a = 5
print (type(a))
print (type(5.0))
print (isinstance(a, int))
print("\n")

b = 10.34
print (type(b))
print("\n")

c = 1.2e-37
# f= 1.23e34 and f= 1.23e+34 are equivalent
print(c)
print (type(c))
print("\n")

d = 10+20J
print(type(d))
print(d + 5)
print(isinstance(c, complex))

a = 10
print (id(a))

myStr = 'hi'
print(id(myStr))
