# creating empty data frame 
import pandas as pd
import numpy as np 
df = pd.DataFrame()
print(df)

y1 = {'q1':5000,'q2':8000,'q3':12000,'q4':18000} #series 1
y2 = {'a':13000,'b':14000,'c':12000} #series 2
total = {1:y1,2:y2} #final series
df = pd.DataFrame(total)
print(df)

# creating a dataframe using list 

l1 = [1,2,3,4,5]
col = ["pratik"]
index = ['a','b','c','d','e']
df = pd.DataFrame(l1 , index = index , columns = col)
print(df)

# creating dataframe using nested list 
l1 = [80,90,70]
l2 = [75,95,67]
l3 = [79,89,80]
student = [l1,l2,l3]
print(student)
df = pd.DataFrame(student,columns = ["s1",'s2','s3'],index=['phy','chem','math'])
print(df)

# creating a dataframe using single series
s1 = pd.Series([10,20,30,40,50])
df = pd.DataFrame(s1)
print(df)

# creating a dataframe usinng series and passing it in df as list
s2 = pd.Series([1,2,3,4,5])
df = pd.DataFrame([s1,s2])
print(df)

# creating dataframe using series and dictionary 
s1 = pd.Series([10,20,30,40,50])
s2 = pd.Series([1,2,3,4,5])
df = pd.DataFrame({'ST1':s1,'ST2':s2},index = [0,1,2,3,4])
print(df)

# creating dataframe usinf dictionary of list

dict_of_list = {"Name" : ["Pratik",'Vilas','Sanket','Archana'],"Salary" :[6000,15000,11000,75000],"age":[20,48,23,43]}
df = pd.DataFrame(dict_of_list,index=[1,2,3,4])
print(df)

# creating dataframe using dictionary of series 
name = pd.Series(["Pratik","Sanket",'Vilas','Archana'])
salary = pd.Series([6000,75000,15000,11000])
age = pd.Series([20,23,48,43])
df = pd.DataFrame({"Name" : name ,"Salary" : salary ,"age":age})
print(df)

# creating dataframe using list of dictionary

new = [{'Name':"Pratik",'Salary':6000,'Age':20},
       {'Name':"Sanket",'Salary':75000,'Age':23}]
df = pd.DataFrame(new)
print(df)

# creating Dataframe using numpy ndarray
array = np.array([["Pratik",6000,20],["Sanket",75000,23]])
cols = ["Name",'Salary','Age']
index = [1,2]
df = pd.DataFrame(data =array , columns = cols , index = index)
print(df)

df = pd.DataFrame({"name":["Pratik","Sanket",],"age":[20,23]},index=['a','b'])
print(df)

# Attributes in dataframe 1. index
print(df.index)
# 2. columns
print(df.columns)
# 3.axes
print(df.axes)
# 4.dtypes
print(df.dtypes)
# 5.size (rows * columns)
print(df.size)
# 6.shape
print(df.shape)
# 7.ndim
print(df.ndim)
# 8.empty
print(df.empty)
# 9.T (transpose)
print(df.T)
