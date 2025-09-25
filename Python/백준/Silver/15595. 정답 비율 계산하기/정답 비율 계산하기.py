import sys
n= int(sys.stdin.readline())
dic = {}
l = set()
for _ in range(n):
    num, id, result, mem, ti, lang, leng = sys.stdin.readline().strip().split()
    if id != 'megalusion':
        if id not in l:
            if id in dic:
                dic[id] += 1
            else:
                dic[id] = 1
            if result == '4':
                l.add(id)
if len(l) == 0:
    print(0.0)
else:
    s = 0
    for i in l:
        s += dic[i]
    print(len(l)/s*100)