# 바둑판 생성
tmp = []
for i in range(19):
    a = input().split()
    tmp.append(a)
        
n = int(input()) # 뒤집는 횟수
for j in range(n):
    x, y = map(int, input().split()) # 기준 좌표
    ref = 0
    for k in tmp[x-1]:
        if k == '0':
            tmp[x-1][ref] = '1'
        else:
            tmp[x-1][ref] = '0'
        ref += 1
    ref = 0
    for k in tmp:
        if k[y-1] == '0':
            tmp[ref][y-1] = '1'
        else:
            tmp[ref][y-1] = '0'
        ref += 1
        
            
for i in tmp:
    for j in i:
        print(j, end=' ')
    print()