import sys
c = float(sys.stdin.readline())
l = int(sys.stdin.readline())
result = 0.0
for _ in range(l):
    wi, li = map(float, sys.stdin.readline().split())
    result += wi * li * c
print("%.7f"%result)