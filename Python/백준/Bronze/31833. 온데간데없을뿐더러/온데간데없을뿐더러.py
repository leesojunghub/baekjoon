import sys
n = int(sys.stdin.readline())
a = list(sys.stdin.readline().strip().split())
b = list(sys.stdin.readline().strip().split())
x = int(''.join(a))
y = int(''.join(b))
print(min(x,y))