# Write a Python program to check if the given number is a Disarium Number.
# 89
n = (input("Enter a number : "))
count = 1
sum = 0
for i in n :
    sum += int(i)**(count)
    count +=1
if(sum == int(n)):
    print("Disarium number")
else:
    print("Not a disarium number")