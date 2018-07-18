#Example for Tuple (NOT MUTABLE)
print ("Below are Example for Tuple (NOT MUTABLE)")
t = ()
print (type(t))

t = (1,2,3)
print (t)

t = (1, 'AcadView', 1.2, 'Dehradun')
print(t)

t = (1, 2, 3)
print(t[-1])
# Slicing
print(t[1:3])

t = (1, 2, 3, (4, 5), [6, 7, 8])
t[4][0] = 'hi'
print(t)

# Convert a list to tuple
l = [0, 1, 2]
print(tuple(l))
print(tuple('python'))

#Example for Sets
print ("\n")
print ("Below are Example for SET")
s = set()
print(type(s))

s = {1, 2, 3}
print(s)
print(type(s))

s = set ([4,5,6])
print(s)
print(type(s))

#Duplicates Removed
li = [1, 2, 3, 4, 1 , 5, 2]
s = set(li)
print(s)

# Set Operations
print ("\n")
print ("SET OPERATIONS")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)
print(set1.union(set2))
print(set1 & set2)
print(set1.intersection(set2))
print(set1 - set2)
print(set1.difference(set2))
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
