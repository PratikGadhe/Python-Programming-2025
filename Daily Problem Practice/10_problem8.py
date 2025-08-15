# Write a Python Program to Sort Words in Alphabetic Order.
name=input("Enter names : ")
words=[word.capitalize() for word in name.split()]
words.sort()
for word in words:
    print(word)
