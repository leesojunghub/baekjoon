import sys
dic = {
    'W': 64,
    'H': 32,
    'Q': 16,
    'E': 8,
    'S': 4,
    'T': 2,
    'X': 1,
}
while True:
    s = list(sys.stdin.readline().strip().split('/'))
    if s[0] == '*':
        break
    s = s[1:-1]
    cnt = 0
    for i in s:
        n = 0
        for j in i:
            n += dic[j]
        if n == 64:
            cnt += 1
    print(cnt)