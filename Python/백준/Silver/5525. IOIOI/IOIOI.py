import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

cnt = 0
answer = 0

i = 1
while i < m - 1:
    if s[i-1:i+2] == "IOI":
        cnt += 1
        if cnt >= n:
            answer += 1
        i += 2   # 겹침 처리
    else:
        cnt = 0
        i += 1

print(answer)