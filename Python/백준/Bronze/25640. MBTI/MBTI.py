import sys
from collections import Counter
input = sys.stdin.readline

mbti = input().strip()
n = int(input())
l = [input().strip() for _ in range(n)]
l = Counter(l)
print(l[mbti])