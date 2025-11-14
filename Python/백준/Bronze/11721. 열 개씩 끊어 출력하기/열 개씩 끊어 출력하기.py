import sys
s = sys.stdin.readline().strip()
n = len(s)
for i in range(0, n, 10):
    if i + 10 > n:
        print(s[i:])
    else:
        print(s[i:i+10])