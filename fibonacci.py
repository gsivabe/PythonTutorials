#Print all fibonacci series
count = 0
n1 = 0
n2 = 1
while count < 10:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
