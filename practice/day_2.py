"""# Write a Python Program to Find LCM.
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
# n1= 5 , n2 = 3
if(n1 > n2 ):
    greater = n1
else :
    greater = n2
while(True):
    if((greater % n1 == 0) and (greater % n2 == 0)):
        lcm = greater
        break
    greater += 1
print(lcm)

# Write a Python Program to Find HCF.
n1 = int(input("Enter a number 1 : "))
n2 = int(input("Enter a number 2 : "))

if(n1 < n2 ):
    smaller = n1
else :
    smaller = n2

for i in range(1,smaller+1):
    if((n1 % i == 0) and (n2 % i == 0 )):
        hcf = i
print(hcf)
"""

# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

"""
Divide 27 by 2. Quotient is 13, remainder is 1. Note the remainder.
Divide 13 by 2. Quotient is 6, remainder is 1. Note the remainder.
Divide 6 by 2. Quotient is 3, remainder is 0. Note the remainder.
Divide 3 by 2. Quotient is 1, remainder is 1. Note the remainder.
Divide 1 by 2. Quotient is 0, remainder is 1. Note the remainder.

n = int(input("Enter a decimal number: "))

binary = 0
place = 1

while n > 0:
    remainder = n % 2
    binary = binary + remainder * place
    place = place * 10
    n = n // 2   # integer division (gives quotient)

print("Binary number:", binary)

# decimal to octal 
n = int(input("Enter a decimal number: "))
octal = 0 
while n > 0 :
    rem = n%8
    octal = octal*10 + rem
    n = n//8
octal = str(octal)
octal = octal[::-1]
print("Octal number : ", octal)
"""


# Write a Python Program to Display Fibonacci Sequence Using Recursion.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1)) + (fibonacci(n - 2))


nterms = int(input("Enter the number of terms (greater than 0): "))
print("fibonacci series : ")
for i in range(nterms):
    print(fibonacci(i))
