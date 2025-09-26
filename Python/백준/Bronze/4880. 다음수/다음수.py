import sys
while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0 and c == 0:
        break
    if (a + c) / 2 == b:
        print('AP', 2 * c - b)
    else:
        print('GP', int(c**2 / b))