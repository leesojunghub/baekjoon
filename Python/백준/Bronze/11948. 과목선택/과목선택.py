import sys
a = [int(sys.stdin.readline()) for _ in range(4)]
b = [int(sys.stdin.readline()) for _ in range(2)]
a.sort(reverse=True)
b.sort(reverse=True)
print(sum(a[:3]) + sum(b[0:1]))