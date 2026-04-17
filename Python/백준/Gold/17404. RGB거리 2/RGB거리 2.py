import sys

input = sys.stdin.readline
INF = 10**15

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

answer = INF

for start in range(3):
    prev = [INF, INF, INF]
    prev[start] = cost[0][start]

    for i in range(1, n):
        curr = [0, 0, 0]
        curr[0] = cost[i][0] + min(prev[1], prev[2])
        curr[1] = cost[i][1] + min(prev[0], prev[2])
        curr[2] = cost[i][2] + min(prev[0], prev[1])
        prev = curr

    for last in range(3):
        if last != start:
            answer = min(answer, prev[last])

print(answer)
