
# Write a Python Program to calculate your Body Mass Index.
def body_mass_index(weight,height):
    return round((weight)/(height**2),2)
w = float(input("Enter weight (in kg): "))
h = float(input("Enter height (in m): "))
bmi = body_mass_index(w,h)
print("Your Calculated bmi is : ",bmi)
if(bmi < 18.5):
    print("you are underweight")
elif(bmi > 18.5 and bmi < 24.9):
    print("Your weight is normal")
elif(bmi > 29.9):
    print("youre overweight")
else:
    print("you are obese")

# Write a Python Program to calculate the natural logarithm of any number.
import math
n = float(input("Enter a number: "))
log = round(math.log(n),3)
print(f"logrithm of {n} is {log}")

# Write a Python Program for cube sum of first n natural numbers?
n = int(input("Enter a number : "))
def cube(n):
    result = 0
    for i in range(1,n+1):
        result += i**3
    return result
print(f"Cube of first {n} natural number is {cube(n)}")

# Write a Python Program to find sum of array.
arr = [1,2,3,4,5]
# 1. method
print(sum(arr))
# 2. method
sum1 = 0
for i in arr:
    sum1+=i
print(sum1)

# Write a Python Program to find largest element in an array.

arr = [10, 20, 30, 99]

def largest(arr):
    if not arr:
        print("Array is empty")
    maximum = arr[0]
    for i in arr:
        if(i > maximum):
            maximum = i
    return maximum

print("Largest number from arr is ",largest(arr))