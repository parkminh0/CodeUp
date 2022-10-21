a = input().split()
for i in a:
    i = int(i)
    if i // 3 == 1:
        print("spring")
    elif i // 3 == 2:
        print("summer")
    elif i // 3 == 3:
        print("fall")
    else:
        print("winter")