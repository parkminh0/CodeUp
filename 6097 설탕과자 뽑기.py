# 판 생성
h, w = map(int, input().split())
tmp = []
for i in range(h):
    tmp.append([])
    for j in range(w):
        tmp[i].append(0)
        

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            tmp[x-1][y-1+j] = 1
        else:
            tmp[x-1+j][y-1] = 1
            
for i in tmp:
    for j in i:
        print(j, end=' ')
    print()