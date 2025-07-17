
#strings
#operations perform on string
#1.CONCATENATION
str1="Pratik "
str2="Gadhe"
final=str1+str2
print("Your Name is",final)

#2.LENGTH OF STRING len()
print(len(final))

#3.Indexing

name="Pratik"
ch=name[1]
print("Chracter :",ch)

#slicing

name1="Pratik Vilas Gadhe"
print(name1[0:6])
print(name[:6])
print(name1[0:])
print(name1[0:len(name1)])
print(name1[13:])
print(name1[0:20])#ending index is out of range but still working

#negative indexing 

a="apple"
print(a[-3:-1])
print(a[-6:1])