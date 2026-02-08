import sys
l = [int(sys.stdin.readline()) for _ in range(5)]
l.sort()
print(int(sum(l) / 5))
print(l[2])