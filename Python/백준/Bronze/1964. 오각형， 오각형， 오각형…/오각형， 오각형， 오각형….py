import sys
n = int(sys.stdin.readline())
print((sum(range(1, n+1))*5-(n**2-1))%45678)