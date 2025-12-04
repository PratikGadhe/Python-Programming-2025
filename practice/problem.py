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

arr=[1,2,3,4,5]
length=int((len(arr))/2)
first=arr[:length]
second=arr[length:]
result=second+first
print(result)

r=int(input("Enter number of rows : "))
c=int(input("Enter number of columns : "))
matrix=[[0 for _ in range(c)]for _ in range(r)] #2d array
for i in range(0,r):
    for j in range(0,c):
        matrix[i][j]=int(input(f"Enter [{i}][{j}] : "))
print("\nMatrix:")
for r in matrix:
    print(r)
  
r=int(input("Enter row : "))
c=int(input("Columns : "))
matrix1=[[0 for _ in range(c)]for _ in range(r)]
matrix2=[[0 for _ in range(c)]for _ in range(r)]
result=[[0 for _ in range(c)]for _ in range(r)]
print("-- Matrix 1 --")
for i in range(r):
    for j in range(c):
        matrix1[i][j]=int(input(f"[{i}][{j}] : "))
print("-- Matrix 2 --")
for i in range(r):
    for j in range(c):
        matrix2[i][j]=int(input(f"[{i}][{j}] : "))
print("-- Sum --")
for i in range(r):
    for j in range(c):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
for r in result:
    print(r)

r=int(input("Enter row : "))
c=int(input("Columns : "))
matrix1=[[0 for _ in range(c)]for _ in range(r)]
result=[[0 for _ in range(c)]for _ in range(r)]
print("-- Matrix 1 --")
for i in range(r):
    for j in range(c):
        matrix1[i][j]=int(input(f"[{i}][{j}] : "))

print("result")
for i in range(r):
    for j in range(c):
        result[i][j]=matrix1[j][i]
for r in result:
    print(r)

str=input("Enter string : ")
spilt = str.split()
list=[]
for i in spilt:
    list.append(i.capitalize())
list.sort()
for i in list:
    print(i)


punct=""
str=input("Enter a string : ")
for char in str:
    if char not in punctuations:
        punct+=char
print(punct)

n=input("Enter a number : ")
pow=1
num=0
for i in n:
    num+=int(i)**pow
    pow+=1
if(int(n)==num):
    print("Disarium number")
else:
    print("NOT")

n=int(input("Enter range : "))
for i in range(n):
    pow =1
    num=0
    for j in str(i):
        num+=int(j)**pow
        pow+=1
    if(num == i):
        print(i,end=" | ")
print("\n")

n=input("Enter a number : ")
sum=0
for i in n:
    sum+=int(i)
if(int(n)%sum == 0):
    print(int(n),"is harshad number")
else:
    print("NOT")
    
n=int(input("Enter range : "))
for i in range(n):
    sum=0
    for j in str(i):
        sum+=int(j)
    if(int(i)%sum == 0):
        print(i,end="|")


numbers = [10, 20, 30, 40, 50]
mul=1
for i in numbers:
    mul*=i
print(mul)
numbers = [30, 10, -45, 5, 20]
min=numbers[0]
for i in numbers:
    if(i<min):
        min=i
print(min)

n = [30, 10, -45, 5, 20]
n.sort()
print(n[0])

n = [30, 10, -45, 5, 20]
max=n[0]
for i in n:
    if(i>max):
        max=i
print(max)

n = [30, 10, -45, 5, 20]
n.sort(reverse = True)
print(n[0])

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=[]
for i in n:
    if(i%2 == 0):
        even.append(i)
print(even)

word= ["apple", "banana", "cherry", "date", "elderberry", "dragon","fruits"]
list=[]
for i in word:
    if(len(i)>5):
        list.append(i)
print(list)

str=input("Enter a string")
i=7
str1=str[:i]+str[i+1:]
print(str1)

list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
count = 0
for i in list:
    if(i == 2):
        count+=1
print(f"2 repeats {count} times")

input_str = "Python program to split and join a string"
spilt= input_str.split()
print(spilt)
separator=" "
join = separator.join(spilt)
print(join)
"""
