#prime number 
"""
n=int(input("Enter a number : "))
for i in range(2,n):
    if(n%i == 0):
        prime = 0
        break
    else :
        prime = 1
if (prime == 1) :
    print("The number is prime")
else :
    print("Number is not prime")
    
# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
n= int(input("Enter range : "))
prime = 1
for i in range(2,n):
    for j in range(2,i):
        if (i%j != 0):
            prime = 1
        else :
            prime = 0
            break
    if(prime == 1):
        print(i)
# Write a Python Program to Find the Factorial of a Number.
n=int(input("Enter a number : "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)

# Write a Python Program to Print the Fibonacci sequence.
n=int(input("Enter a number : "))
fib0,fib1=0,1
print(fib0)
print(fib1)
for i in range(2,n):
    fib = fib0+fib1
    print (fib)
    fib0=fib1
    fib1=fib

# Write a Python Program to Check Armstrong Number?
#153 is armstrong : 1^3+5^3+3^3=153

n=int(input("Enter a number : "))
length = len(str(n))
check=0
for i in str(n):
    check+=int(i)**length
if(check == n):
    print(f"{n} is Armstrong Number")
else:
    print(f"{n} is not armstrong number")

# Write a Python Program to Find the Sum of Natural Numbers.
n=int(input("Enter a number : "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

# Write a Python Program to Find Armstrong Number in an Interval.
n=int(input("Enter range : "))
for i in range (10,n):
    length = len(str(i))
    final=0
    for j in str(i):
        final+=int(j)**length
    if(final == i):
        print(i)

# Program to reverse a number
n=int(input("Enter a number : "))
for i in str(n):
    final=int(i)%10
    
n=int(input("Enter a number : "))
prime = 1
for i in range(2,n):
    if(n%i == 0):
        prime = 1
    else:
        prime = 0
if(prime == 1):
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")
    
n = int(input("Enter range : "))
print(f"Prime number btw 1-{n} : ")
prime = 1
for i in range(2,n):
    for j in range(2,i):
        if(i%j != 0):
            prime = 1
        else:
            prime = 0
            break
    if(prime == 1):
        print(i,sep=",")

n=int(input("Enter a number : "))
fact=1
for i in range(1,n+1):
    fact = fact*i
print(fact)

n=int(input("Enter number"))
f1,f2=0,1
print(f1," ",f2," ")
for i in range(2,n):
    fib=f1+f2
    print(fib)
    f1,f2=f2,fib

n=int(input("Enter a number : "))
length=len(str(n))
num=0
temp=n
while(n>0):
    digit=(n%10)
    num+=digit**length
    n//=10
if(num == temp):
    print("Armstrong number")
else:
    print("not")
n =input("Enter number : ")
length=len(n)
num=0
for i in n:
    num+=int(i)**length
if(num == int(n)):
    print("armstrong")
else:
    print("not")

n=int(input("Enter range : "))
for i in range(1,n+1):
    length=len(str(i))
    num=0
    for j in str(i):
        num+=int(j)**length
    if(num == int(i)):
        print(i)
      
sum = lambda x,y : x+y
sub = lambda x,y : x-y
mul = lambda x,y : x*y
div = lambda x,y : x/y
n1,n2=int(input("Enter number 1 :")),int(input("Enter number 2 : "))
print("Select operation")
print("\n1.add\n2.sub\n3.mul\n4.div")
choice=input("Enter your choice : ")
if choice in ('1','2','3','4'):
    if(choice == '1'):
        print(sum(n1,n2))
    elif(choice == '2'):
        print(sub(n1,n2))
    elif(choice == '3'):
        print(mul(n1,n2))
    elif(choice == '4'):
        print(div(n1,n2))
else:
    print("invalid choice")
 
array = [1,2,3,4,5]
sum=0
for i in array:
    sum+=i
print(sum)

array=[90,10,11,212,23,11,1]
array.sort(reverse=True)
print("largest=",array[0])
"""