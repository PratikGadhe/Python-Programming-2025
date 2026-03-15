
#Write a Python Program to Check Prime Number.
n = int(input("Enter a number : "))
for i in range(2,n):
    if(n%i != 0):
        prime = 1
    else :
        prime = 0
        break
if(prime == 1):
    print(f"{n} is prime number")
else :
    print(f"{n} is not prime number")
    

#Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
n = int(input("Enter a range : "))
for i in range(1,n+1):
    for j in range(2,i):
        if(i%j != 0):
            prime = 1
        else :
            prime = 0
            break
    if(prime == 1):
        print(i)

# Write a Python Program to Find the Factorial of a Number.
n = int(input("Enter a number : "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)

# Write a Python Program to Print the Fibonacci sequence.

n = int(input("Enter a number : "))
fib0 = 0
fib1 = 1
print(f"{fib0},{fib1},")
for i in range(2,n+1):
    fib = fib0 + fib1
    print(f"{fib},")
    fib0 , fib1 = fib1 , fib

# Write a Python Program to Check Armstrong Number?
n = input("Enter a number : ")
length = len(n)
check = 0
for i in n:
    check += int(i)**length
if(int(n) == check):
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not a armstrong number")

# Write a Python Program to Find Armstrong Number in an Interval.
n = int(input("Enter a range : "))
for i in range(10,n+1):
    str_num = str(i)
    length = len(str_num)
    check = 0
    temp = i
    while(temp > 0):
        digit = temp % 10
        check += digit ** length
        temp //= 10
    if(i == check):
        print(i)

