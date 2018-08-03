'''
2
2
1 1
1 1
2
0 2
1 1
'''
test =int(input())

for t in range(test):
    co = 0
    m  = int(input())
    d = {}
    li = []
    for i in range(m):
        b = list(map(int,input().split()))
        li.append(b)
        for j in range(len(b)):
            try:
                d[j] = d.get(j, 0) + b[j]
            except:
                d[j] = b[j]
    for i in range(m):
        nz = 0
        for j in range(len(li)):
            if d[j] == sum(li[i]):
                nz = 1
                break
        if nz == 0:
            print(i, 'impossible')
            co = 1
            break
    if co == 0:
        print('possible')
