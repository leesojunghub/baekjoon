import sys
l = list(map(int, sys.stdin.readline().split()))
l.sort()
if l[1] - l[0] > l[2] - l[1]:
    a = l[2] - l[1]
else:
    a = l[1] - l[0]
for i in range(0,2):
    if l[i] + a != l[i+1]:
        print(l[i] + a)
        exit()
print(l[2] + a)