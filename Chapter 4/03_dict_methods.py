#method of dictionary
#1. dict.keys(): returns all keys
dict={"Name":"Pratik vilas gadhe","language":"python","marks":96.5,"roll_number":57}
# print(dict.keys())

#2. dict.values() : returns all values
# print(dict.values())
# print(list(dict.keys()))
# print(tuple(dict.values()))

#3. myDict.items() : #returns all (key, val) pairs as tuples

print(dict.items())
pair=list(dict.items())
print(pair[0])