a = int(input())
sum = 0
i = 0
while True:
    sum += i
    if sum >= a:
        print(i)
        break;
    i += 1