str = input ("Enter the main string: ")
sub_str = input (" Enter the substring: ")
if sub_str in str:
    print ("YES, the string is present.")
else:
    print("NO, the string is absent")

str = "The sky is blue and grass is green"
sub_str = "gren"
check = False
for i in str.split():
    if i == sub_str:
        check = True
        break
if check:
    print("YES")
else:
    print("No")