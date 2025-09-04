import sys
import heapq
from collections import Counter
t = int(sys.stdin.readline().strip())
for _ in range(t):
    k = int(sys.stdin.readline().strip())
    min_heap = []
    max_heap = []
    count = Counter()
    for i in range(k):
        s, n = map(str, sys.stdin.readline().strip().split())
        if s == 'I':
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, -int(n))
            count[int(n)] += 1
        elif s == 'D':
            if n == '1':
                while max_heap:
                    x = -heapq.heappop(max_heap)
                    if count[x] > 0:
                        count[x] -= 1
                        break

            elif n == '-1':
                while min_heap:
                    x = heapq.heappop(min_heap)
                    if count[x] > 0:
                        count[x] -= 1
                        break
    while max_heap and count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    if not min_heap or not max_heap:
        print('EMPTY')
    else:
        print(-max_heap[0], min_heap[0])