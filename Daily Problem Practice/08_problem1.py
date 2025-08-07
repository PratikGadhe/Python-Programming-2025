# neon number 
n=int(input("Enter number : "))
for i in range(1,n+1):
    square=i**2
    sum_of_digit=0
    for j in str(square):
        sum_of_digit += int(j)
    if(sum_of_digit == i):
        print(i)
    