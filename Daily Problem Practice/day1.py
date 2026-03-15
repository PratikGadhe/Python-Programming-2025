"""
Write a Python program to find the area of a triangle. and many more areas
def triangle(length , height):
    area = 0.5 * length * height
    return area
def circle(radius):
    area = 3.14 * radius * radius
    return area
def square(side):
    area = side * side
    return area
def rectangle(length , breadth):
    area = length * breadth 
    return area

area_circle = circle(2)
area_triangle = triangle(2,2)
area_square = square(2)
area_rectangle = rectangle(2,2)
print(f"triangle : {area_triangle}")
print(f"square : {area_square}")
print(f"circle : {area_circle}")
print(f"rectangle : {area_rectangle}")


# Write a Python program to swap two variables.
n1 = 10
n2 = 20
temp = n1
n1 = n2
n2 = temp
print(f"n1 : {n1} , n2 : {n2}")

# 2nd method 
n1 , n2 = n2 , n1
print(f"n1 : {n1} , n2 : {n2}")

# Write a Python program to generate a random number.
import random 
rand = random.randint(0,100)
print(f"random number : {rand}")

# Write a Python program to convert kilometers to miles.
kilo = int(input("Enter kilometer : "))
miles = kilo*0.62371
print(f"{kilo} Kilometer == {miles} miles")


# Write a Python program to convert Celsius to Fahrenheit.
celcius = float(input("Enter Celcius : "))
fehrenheit = (celcius * (9/5) + 32)
print(f"{celcius} Celcius == {fehrenheit} Fehrenheit")

# Write a Python Program to Check Leap Year.
year = int(input("Enter a year : "))
if(year % 400 == 0 and year % 100 == 0 ):
    print(f"{year} is leap and centurian year!")
elif(year % 4 == 0 and year % 100 != 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")

# Write a Python Program to Check Prime Number.
num = int(input("Enter a number : "))
for i in range(2,num):
    if(num % i != 0):
        prime = 1
    else:
        prime = 0 
        break
if(prime == 1):
    print(f"{num} is a prime number!")
else:
    print(f"{num} is not a prime number!")

# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
r = int(input("Enter a range : "))
print(f"Prime Number between 0-{r} are : ")
prime = 0
for i in range(2,r):
    for j in range(2,i):
        if(i%j == 0 ):
            prime = 0
            break
        else:
            prime = 1
    if(prime == 1):
        print(f"{i}",sep=",")

#  Write a Python Program to Find the Factorial of a Number.
n = int(input("Enter a number : "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"Factorial of {n} is {fact}")

# Write a Python Program to Display the multiplication Table.
n = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

remaining from program 18

# Write a Python Program to Print the Fibonacci sequence.
n = int(input("Enter a number : "))
fib0 = 0
fib1 = 1
print(fib0,fib1)
for i in range(2,n+1):
    fib = fib0 + fib1
    print(f"{fib} ")
    fib0,fib1 = fib1,fib

# Write a Python Program to Check Armstrong Number?
n = input("Enter a number : ")
length = len(n)
final = 0 
for i in n : 
    final += int(i) ** length
if(int(n) == final):
    print(f"{n} is a armstrong number!")
else:
    print(f"{n} is not a armstrong number!")

# Write a Python Program to Find Armstrong Number in an Interval.
n = int(input("Enter a number range : "))
for i in range(n):
    final = 0 
    length = len(str(i))
    for j in str(i):
        final += int(j)**int(length)
    if(final == i):
        print(i)

# Write a Python Program to Find the Sum of Natural Numbers.
n=int(input("Enter a number : "))
sum = 0
for i in range(0,n+1):
    sum+=i
print(sum)
"""