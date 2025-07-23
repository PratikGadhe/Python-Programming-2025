# Write a Python Program to Check Prime Number.
n=int(input("Enter a number : "))
prime = 1 #true
i=2
while(i<n):
    if(n%i != 0):
        prime = 1
    else:
        prime = 0
        break
    i+=1
if(prime == 1):
    print(f"{n} is a prime number !")
else:
    print(f"{n} is not a prime number !")