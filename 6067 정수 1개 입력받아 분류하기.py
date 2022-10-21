a = input().split()
for i in a:
    i = int(i)
    if i < 0:
        if i%2 == 0:
            print("A")
        else:
            print("B")
    else:
        if i%2 == 1:
            print("D")
        else:
            print("C")