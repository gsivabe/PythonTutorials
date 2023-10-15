"""
#Simple Calculator using If Elif
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def quo(x,y):
    return x / y

def powe(x,y):
    return pow(x, y)

print ("Please select the operation.")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")
print ("e. Power")

choice = input("Please enter choice (a/ b/ c/ d) /e: ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':
    print(num_1, " - ", num_2, " = ", sub(num_1, num_2))

elif choice == 'c':
    print(num1, " * ", num2, " = ", mul(num1, num2))
elif choice == 'd':
    print(num_1, " / ", num_2, " = ", quo(num_1, num_2))
elif choice == 'e':
    print(num_1, "power", num_2, " = ", powe(num_1, num_2))

else:
    print("This is an invalid input")
"""

#Simple Calculator using Switch Case

print ("Please select the operation.")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")
print ("e. Power")

choice = input("Please enter choice (a/ b/ c/ d /e): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

match choice:
    case "a":
        print(num_1, " + ", num_2, " = ", (num_1 + num_2))
    case "b":
        print(num_1, " - ", num_2, " = ", (num_1 - num_2))
    case "c":
        print(num_1, " * ", num_2, " = ", (num_1 * num_2))
    case "d":
        print(num_1, " / ", num_2, " = ", (num_1 / num_2))
    case "e":
        print(num_1, " pow ", num_2, " = ", (num_1 ** num_2))

    case _:
        print("Invalid choice")
