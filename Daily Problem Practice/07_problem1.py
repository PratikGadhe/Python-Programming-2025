# Program to the maximum in an array.
arr=[1,3,5,9,0,-1,2,5]
smaller=arr[0]
for i in range(1,len(arr)):
    if(arr[i] < smaller):
        smaller=arr[i]
print(f"Minimum value : {smaller}")