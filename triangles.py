#Program for Triangles
num = int(input("Enter number of lines for triangle: "))

print("Ascending to Descending")
for i in range(0,num):
    for j in range(0, i+1):
        print("* ", end="")
    print("")
print("")

print("Descending to Ascending")
for i in range(num, 0, -1):
    for j in range(1, i+1):
        print("* ", end="")
    print("")
print("")

print("Ascending to Descending to Ascending")
for i in range(0,num):
    for j in range(0, i+1):
        print("* ", end="")
    print("")
for i in range(num-1, 0, -1):
    for j in range(1, i+1):
        print("* ", end="")
    print("")

print("Descending to Ascending with numbers")
for i in range(num):
    for j in range(num-i):
        print(i+j+1, end=" ")
    print("")
print("")
