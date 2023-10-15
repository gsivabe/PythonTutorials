ran = int(input("Enter the range of array: "))
arr_src = []
for i in range(0, ran):
    temp = int(input(f"Enter the value of array[{i}]: "))
    arr_src.append(temp)
print("You created an array as: ", arr_src)

"""
#Program to find the frequency of each value in the array
arr_cou = [None] * len(arr_src)

for i in range(0,len(arr_src)):
    count = 0
    for j in range(0, len(arr_src)):
        if(arr_src[i] == arr_src[j]):
            count = count + 1
    print(f"The count of {arr_src[i]} is: ",count)

#Program to find the maximum & minimum value in the array
max_num = arr_src[0]
for i in range(0, len(arr_src)):
    if (arr_src[i] > max_num):
        max_num = arr_src[i]
print("Maximum number in array is: ",max_num)

min_num = arr_src[0]
for i in range(0, len(arr_src)):
    if (arr_src[i] < min_num):
        min_num = arr_src[i]
print("Minimum number in array is: ",min_num)

#To search a number created in above array
val = int(input("Enter the value to search in array: "))
k = 0
for e in arr_src:
    if e==val:
        print(f"The number {val} present in the position of {k}")
        break
    k+=1
else:
    print(f"The number {val} is not present in the array")

#Program to find the sum of array
sum = 0
for i in arr_src:
    sum = sum + i
print("The sum of array is: ", sum)

#Program to print array in ascending and descending
arr_asc = arr_src
arr_dsc = arr_src

for i in range(0,len(arr_asc)):
    for j in range(0, len(arr_asc)):
        if(arr_asc[i] <= arr_asc[j]):
            arr_asc[i], arr_asc[j] = arr_asc[j], arr_asc[i]
print("Ascending order of Array:", arr_asc)

for i in range(0,len(arr_dsc)):
    for j in range(0, len(arr_dsc)):
        if(arr_dsc[i] >= arr_dsc[j]):
            arr_dsc[i], arr_dsc[j] = arr_dsc[j], arr_dsc[i]
print("Descending order of Array:", arr_dsc)

#Program to print add and even position of numbers in array
arr_odd = []
arr_eve = []
for i in range(0, len(arr_src)):
    if(i%2 == 0):
        arr_eve.append(arr_src[i])
    else:
        arr_odd.append(arr_src[i])

print("Values in odd position", arr_odd)
print("Values in even position",arr_eve)
"""

#Program to reverse the array
arr_rev = []
#for i in reversed(range(len(arr_src))):
#    arr_rev.append(arr_src[i])
#print("Reverse Array :", arr_rev)

for i in range(len(arr_src)-1, -1, -1):
    arr_rev.append(arr_src[i])
print("Reverse Array :", arr_rev)
