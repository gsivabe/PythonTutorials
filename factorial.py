#Print the factorial of a given number
x = int(input("Enter any number to find its factorial: "))
fact = 1
for x in range(1, x+1):
    fact = fact * x
#    print(fact)
#    print(x)

print(fact)
