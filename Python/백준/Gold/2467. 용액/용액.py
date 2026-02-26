import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
left = 0
right = n-1
best = (l[left], l[right])
best_abs = abs(l[left] + l[right])
while left < right:
    s = l[left] + l[right]
    if abs(s) <= best_abs:
        best_abs = abs(s)
        best = (l[left], l[right])
        if best_abs == 0:
            break
    if s < 0:
        left += 1
    else:
        right -= 1
print(best[0], best[1])