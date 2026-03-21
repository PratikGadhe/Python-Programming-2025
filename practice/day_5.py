arr = [1, 2, 3, 4, 5]
d = int(input("Enter a rotation number : "))
def rotation(arr,d):
    n = len(arr)
    if(d < 0 and d>=n):
        return "Invalid rotation!!"
    r_array = [0]*n
    for i in range(n):
        r_array[i] = arr[(i+d)%n]
    return r_array
print("Original array ",arr)
print("rotated array : ",rotation(arr,d))

# Write a Python Program to Split the array and add the first part to the end?
arr = [1, 2, 3, 4, 5]
d = int(len(arr)/2)
first_part = arr[0:d]
second_part = arr[d:len(arr)+1]
final_part = second_part + first_part
print(final_part)

# Write a Python Program to check if given array is Monotonic.
arr1 = [1, 2, 2, 3] # Monotonic (non-decreasing)
arr2 = [3, 2, 1] # Monotonic (non-increasing)
arr3 = [1, 3, 2, 4]
def check_monotonic(arr):
    increasing = decreasing = True
    for i in range(1,len(arr)):
        if(arr[i] > arr[i-1]):
            decreasing = False
        elif(arr[i] < arr[i-1]) : 
            increasing = False
    return increasing or decreasing 
print("arr1 is monotonic ?", check_monotonic(arr1))
print("arr2 is monotonic ?", check_monotonic(arr2))
print("arr3 is monotonic ?", check_monotonic(arr3))

# Write a Python Program to create Matrices.
r = int(input("Enter number of rows : "))
c = int(input("Enter number of columns : "))
array = []
for i in range(0,r):
    row = []
    for j in range(0,c):
        user = int(input(f"enter arr1[{i}][{j}] : "))
        row.append(user)
    array.append(row)
print("Matrix in python")
for row in array:
    print(row)

# Write a Python Program to Add Two Matrices.
arr1 = []
arr2 = []
r1 = int(input("Enter number of rows for matrix 1 : "))
c1 = int(input("Enter number of columns for matrix 1: "))
for i in range(0,r1):
    row1 = []
    for j in range(0,c1):
        user = int(input(f"Matrix 1 [{i}][{j}] : "))
        row1.append(user)
    arr1.append(row1)
for row1 in arr1:
    print(row1)
r2 = int(input("Enter number of rows for matrix 1 : "))
c2 = int(input("Enter number of columns for matrix 1: "))
for i in range(0,r2):
    row2 = []
    for j in range(0,c2):
        user = int(input(f"Matrix 2 [{i}][{j}] : "))
        row2.append(user)
    arr2.append(row1)
for row2 in arr2:
    print(row2)
