import sys
input = sys.stdin.readline

n = int(input())
l = set(map(int, input().split()))
l = list(l)
l.sort()
print(' '.join(map(str, l)))