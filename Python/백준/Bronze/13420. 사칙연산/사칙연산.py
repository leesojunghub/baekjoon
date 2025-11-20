import sys
n = int(sys.stdin.readline())
for _ in range(n):
    l = list(sys.stdin.readline().strip().split())
    n = int(l[0])
    for i in range(1, len(l) -2, 2):
        if l[i] == '+':
            n += int(l[i+1])
        elif l[i] == '-':
            n -= int(l[i+1])
        elif l[i] == '*':
            n *= int(l[i+1])
        elif l[i] == '/':
            n /= int(l[i+1])
    if n == int(l[-1]):
        print('correct')
    else:
        print('wrong answer')