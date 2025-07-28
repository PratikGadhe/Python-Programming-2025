# Write a Python Program to Find Armstrong Number in an Interval.
n=int(input("Enter range : "))
i=1
print(f"Armstrong Numbers between (1-{n}) are : ",end=" ")
while (i<=n):
    temp=i
    num_str=len(str(temp))
    total=0
    while(temp>0):
        num=temp%10
        total+=num**num_str
        temp//=10
    if(i == total):
        print(i,end=" ")
    i+=1
print("\n")