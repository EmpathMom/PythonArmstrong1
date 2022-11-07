

total = 0


def Armstrong(n):
    m = list(n)
    global total
    for i in m:
        total += pow(int(i), len(n))
    if total == int(n):
        print("it is Armstrong number")
    else:
        print("it is not Armstrong number")


Armstrong(input("enter your number"))
print(total)
