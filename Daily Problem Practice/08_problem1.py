# neon number 
'''
n=int(input("Enter number : "))
for i in range(1,n+1):
    square=i**2
    sum_of_digit=0
    for j in str(square):
        sum_of_digit += int(j)
    if(sum_of_digit == i):
        print(i)
'''
n=int(input("Enter a number : "))
square=n**2
sum_of_digit=0
while(square>0):
    num=square%10
    sum_of_digit+=num
    square//=10
if(sum_of_digit == n):
        print(n)
