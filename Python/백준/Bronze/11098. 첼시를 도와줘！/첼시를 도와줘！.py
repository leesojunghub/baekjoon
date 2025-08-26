import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    dic = {}
    for i in range(n):
        a, b = map(str, sys.stdin.readline().strip().split())
        dic[int(a)] = b
    print(dic[max(dic)])