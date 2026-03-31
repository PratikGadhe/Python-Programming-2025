import pandas as pd
import numpy as np
# creating an empty series
# s1 = pd.Series()
# print(s1)

#creating series using list 
# s1 = pd.Series([1,2,3,4,5],['a','b','c','d','e'])
# print(s1)

# creating using two list
months=['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
no_days=[31,28,31,30,31,30,31,30,30,31,30,31]

# s1 = pd.Series(no_days,index=months)
# print(s1)

s1=pd.Series(range(10))
print(s1)

s2=pd.Series(range(1,15,3),index = [x for x in 'abcde'])
print(s2) 


s3 = pd.Series([1,2,3,0.5])
print(s3)
s3.index =['a','b','c','d']
print(s3)

# creating series using scalar and constant value
s4 = pd.Series(63,index=[1,23,91,11])
print(s4)
s5=pd.Series(63,index = range(1,15,3))
print(s5)

# creating series using string as data
s6 = pd.Series("welcome to pandas",index=["Pratik","Sanket","Gadhe"])
print(s6) 

# creating a series using dictionary
s6 = pd.Series({'P':"Pratik",'V':"Vilas",'G':"Gadhe"})
print(s6)

d1 = {'P':"Pratik",'V':"Vilas",'G':"Gadhe"}
s1=pd.Series(d1)
print(s1)


d2 = {'A':['p','v','g'],'B':{'p':'pratik'}}
s1 = pd.Series(d2)
print(s1)

s1 = np.arange(10,15)
s_obj = pd.Series(index = s1*4 , data = s1)
print(s_obj)

s2 = pd.Series([1,0.5,np.nan,0])
print(s2)

s1=pd.Series(data = [x for x in range(2,21,2)] , index = [x for x in range(0,10)])
print(s1)

array = np.array([1,2,3,4,5])
s1 = pd.Series(array)
print(s1)