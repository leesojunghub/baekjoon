import sys
n = int(sys.stdin.readline())
l = list(sys.stdin.readline().strip().split())
total = 0
score = 1
for i in l:
    if i == '1':
        total += score
        score += 1
    else:
        score = 1
print(total)