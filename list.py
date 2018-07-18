#List is Mutable
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
print("Length of array %d" %(len(mylist)))
print(mylist[0])
print("for loop starts")
# prints out 1,2,3
for x in mylist:
    print(x)
	
#Slicing 
print ("\n")
print("BELLOW ARE EXAMPLE FOR SILICING")
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
print(my_list[2:5])
print(my_list[:-5])
print(my_list[-5:])
print(my_list[5:])
print(my_list[:])
print(my_list[-4:-2])
print(my_list[-3:])

s = "Hey there! what should this string be?"
#s = s[0:20]
#print(s)
# Length should be 20
print("Length of s = %d" % len(s[0:20]))

# First occurrence of "a" should be at index 8
s = s[5:25]
print("The first occurrence of the letter a = %d" % s.index("a"))
