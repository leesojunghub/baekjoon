import sys
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    n_list = {int(sys.stdin.readline()) for _ in range(n)}
    m_list = {int(sys.stdin.readline()) for _ in range(m)}
    cnt = 0
    if n < m:
        for i in n_list:
            if i in m_list:
                cnt += 1
    else:
        for i in m_list:
            if i in n_list:
                cnt += 1
    print(cnt)