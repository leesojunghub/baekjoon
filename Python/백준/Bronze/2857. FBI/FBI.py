import sys
input = sys.stdin.readline

result = ''
for i in range(1, 6):
    s = input().strip()
    if 'FBI' in s:
        result += str(i) + ' '
if result == '':
    print('HE GOT AWAY!')
else:
    print(result)