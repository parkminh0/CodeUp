a = int(input())
b = input().split()
tmp = []
for i in b:
    i = int(i)
    tmp.append(i)
    
print(min(tmp))