import sys
n = int(sys.stdin.readline())
dic = {}
for _ in range(n):
    name, gram = sys.stdin.readline().strip().split()
    if name in dic:
        dic[name] += int(gram)
    else:
        dic[name] = int(gram)
value = dic.values()
for i in value:
    s = list(value)
    s.remove(i)
    if i * 1618 // 1000 in s:
        print('Delicious!')
        exit()
print('Not Delicious...')
