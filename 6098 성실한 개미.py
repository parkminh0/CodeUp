tmp = []

for i in range(10):
    a = input().split()
    tmp.append(a)

x = 1
y = 1
tmp[x][y] = '9'

while True:
    if tmp[x][y+1] == '0':
        tmp[x][y+1] = '9'
        y += 1
    elif tmp[x][y+1] == '1':
        if tmp[x+1][y] == '1':
            break
        elif tmp[x+1][y] == '2':
            x += 1
            tmp[x][y] = '9'  
            break  
        x += 1
        tmp[x][y] = '9'
    elif tmp[x][y+1] == '2':
        tmp[x][y+1] = '9'
        break        
    
for q in tmp:
    for w in q:
        print(w, end = ' ')
    print()