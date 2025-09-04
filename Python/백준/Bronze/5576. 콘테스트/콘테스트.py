import sys

w = [int(sys.stdin.readline().strip()) for _ in range(10)]
k = [int(sys.stdin.readline().strip()) for _ in range(10)]
w.sort(reverse=True)
k.sort(reverse=True)
print(sum(w[:3]), sum(k[:3]))