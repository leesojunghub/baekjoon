import sys, heapq
n, k = map(int, sys.stdin.readline().split())
heap = []
for _ in range(n):
    school, team, problem, penalty = sys.stdin.readline().strip().split()
    heapq.heappush(heap, ((-1 * int(problem), int(penalty)), school, team))
sch = set()
i = 0
while heap and i < k:
    _, school, team = heapq.heappop(heap)
    if school in sch:
        pass
    else:
        print(team)
        sch.add(school)
        i += 1