import sys
n = int(sys.stdin.readline())
l = list(sys.stdin.readline().strip().split())
dic = {}
for i in range(n):
    if l[i] in dic:
        dic[l[i]] += 1
    else:
        dic[l[i]] = 1
    if dic[l[i]] > 4:
        print(i+1)
        exit()
print(0)