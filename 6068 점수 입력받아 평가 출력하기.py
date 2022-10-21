a = input().split()
for i in a:
    i = int(i)
    if i < 40:
        print("D")
    elif i < 70:
        print("C")
    elif i < 90:
        print("B")
    else:
        print("A")