import sys
a, b = map(int, sys.stdin.readline().split())
if a % 2 == 0:
    a += 1
else:
    a += 2
if b % 2 == 0:
    b -= 2 
else:
    b -= 1
print(2 + (b - a + 1) // 2)