import sys

a = set("MOBIS")
b = set(sys.stdin.readline())
if a & b == a:
    print('YES')
else:
    print('NO')