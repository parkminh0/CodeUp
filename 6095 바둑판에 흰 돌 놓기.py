n = int(input())

a = []
for i in range(19):
    a.append([])
    for j in range(19):
        a[i].append(0)

for j in range(n):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1
    
for k in a:
    for l in k:
        print(l, end = ' ')
    print()