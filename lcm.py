#Calculate LCM of 2 numbers

num1 = int(input("Enter the first number of integer to get LCM: "))
num2 = int(input("Enter the second number of integer to get LCM: "))

if num1 > num2:
    greater = num1
else:
    greater = num2

while(True):
    if((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1

print(lcm)
