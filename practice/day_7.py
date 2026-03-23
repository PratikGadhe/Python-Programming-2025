# Write a Python Program to Sort Words in Alphabetic Order.

string = "suresh ramesh vibhuti gulgule raji ram shyam ajay"
words = []
for i in string.split():
    words.append(i.capitalize())
words.sort()
for i in words:
    print(i)

# comprehension method 
string = "suresh ramesh vibhuti gulgule raji ram shyam ajay"
words = [ i.capitalize() for i in string.split() ]
words.sort()
for i in words:
    print(i)

# Write a Python Program to Remove Punctuation From a String.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string = input("Enter a string ")
no_punc = ""
for i in string:
    if i not in punctuations:
        no_punc = no_punc + i
print(no_punc)