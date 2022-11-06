
numStr = input("Enter a number:")
# finding the length
total = 0
numLen = len(numStr)
# finding sum
for i in (numStr):
    total += pow(int(i), numLen)
if total == int(numStr):
    print("it is a Armstrong number ")
else:
    print("It is Not a Armstrong number ")
