import sys
from collections import Counter
input = sys.stdin.readline

s = input().strip()
for ch in "CAMBRIDGE":
    s = s.replace(ch, "")
print(s)