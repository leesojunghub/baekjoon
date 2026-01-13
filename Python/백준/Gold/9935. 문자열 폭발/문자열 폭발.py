import sys
s = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
stack = []
n = len(bomb)
for ch in s:
    stack.append(ch)
    if len(stack) >= n and ''.join(stack[-n:]) == bomb:
        del stack[-n:]
if stack:
    print(''.join(stack))
else:
    print('FRULA')
