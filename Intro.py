#Keywords in Python
import keyword
print(keyword.kwlist)
tt=len(keyword.kwlist)
print ("Total number of keywords is %d " % (tt))
print("\n\n")

#Example for Input
print("BELLOW ARE EXAMPLE OF INPUT STATEMENT")
num2 = int(input('Please enter a number: '))
print('User has entered %d as input' % (num2))
print("\n\n")

#Example for Print
print("BELLOW ARE EXAMPLES OF PRINT STATEMENT")
print('5'*6)
print(5,6,7)
print('Python', 1, 2)

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string
print counter
print miles
print name
print ("Check for commit from First Branch")