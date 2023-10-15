"""
#Check for Prime Number#1
num = int(input("Enter any number to check for Prime: "))

if num == 1:
    print(num, "is not a prime number")

elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            #print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than or equal to 1, it is not prime
else:
    print(num, "is not a prime number")

#Check for Prime Number#2
num = int(input("Enter any number to check for Prime: "))

for i in range(2,num):
    if num % 2 == 0:
        print(num, " is not a Prime Number")
        break
else:
    print(num, " is a Prime Number")
"""
#Print Prime Numbers in an interval
num1 = int(input("Enter the initial value: "))
num2 = int(input("Enter the final value: "))

for number in range(num1,num2+1):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                break
        else:
            print(number)
