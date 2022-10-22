a, b, c = map(int, input().split())

z = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            z += 1
            print(i, j, k)
            
print(z)            