import sys
from collections import Counter
input = sys.stdin.readline

s = input().strip()
c = Counter(s)
print(len(s) + c[':'] + c['_'] * 5)