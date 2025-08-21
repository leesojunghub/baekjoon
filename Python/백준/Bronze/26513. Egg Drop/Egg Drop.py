import sys
while True:
    n, k = map(int, sys.stdin.readline().strip().split())
    if n == 0 and k==0:
        break
    dic = {'SAFE':[1], 'BROKEN':[k]}
    for _ in range(n):
        floor, sb = map(str, sys.stdin.readline().strip().split())
        if sb == 'SAFE':
            dic['SAFE'].append(int(floor))
        elif sb == 'BROKEN':
            dic['BROKEN'].append(int(floor))
    print(max(dic['SAFE']) + 1, min(dic['BROKEN']) - 1)