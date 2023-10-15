"""
#To check given number is armstong or not
x = int(input("Enter any number to find it is armstrong or not: "))
l = len(str(x))
tot = 0
for i in iter(str(x)):
    #print(i)
    po = pow(int(i),l)
    #print(po)
    tot = tot+po

if x == tot:
    print(f"The number {x} is armstrong")
else:
    print(f"The number {x} is NOT armstrong")
"""

#To print armstong in an interval
num1 = int(input("Enter the initial value: "))
num2 = int(input("Enter the final value: "))

for x in range(num1,num2+1):
    l = len(str(x))
    tot = 0
    for i in iter(str(x)):
        # print(i)
        po = pow(int(i), l)
        # print(po)
        tot = tot + po

    if x == tot:
        print(f"The number {x} is armstrong")
    #else:
        #print(f"The number {x} is NOT armstrong")
