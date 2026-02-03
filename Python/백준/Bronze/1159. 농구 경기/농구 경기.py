import sys
n = int(sys.stdin.readline())
dic = {}
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s[0] in dic:
        dic[s[0]] += 1
    else:
        dic[s[0]] = 1
ans = ''
for i in sorted(dic):
    if dic[i] >= 5:
        ans += i
if ans == '':
    print('PREDAJA')
else:
    print(ans)