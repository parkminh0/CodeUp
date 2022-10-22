a = int(input())
b = input().split()
tmp = []

for i in range(23):
    tmp.append(int(0))

for i in range(len(b)):    
    tmp[int(b[i])-1] += 1

for i in tmp:
    print(i, end=' ')