import sys
n = int(sys.stdin.readline())
n = n-1
for i in range(int(n**0.5)+1, 0,-1):
    if i*(i+1) == n:
        print(i)