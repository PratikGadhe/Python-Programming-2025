#break statement
i=1
while(i<=5):
    print(i)
    if(i==3):
        break
    i+=1

#continue statement 

i=1
while(i<=5):
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1