# Write a Python Program to Check Armstrong Number?
#153 is armstrong : 1^3+5^3+3^3=153

n=int(input("Enter a number : "))
num_str=str(n)
str_num=len(num_str)
sum=0
temp=n
while(temp>0):
    num = temp%10 #store the last digit
    sum+=num**str_num
    temp//=10 #remove the last digit

if(n == sum):
    print(f"{n} is a Armstrong Number ")
else:
    print(f"{n} is not a Armstrong Number ")