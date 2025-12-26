import sys
n = int(sys.stdin.readline())
for _ in range(n):
    s_num = int(sys.stdin.readline())
    v_num = int(sys.stdin.readline())
    o_num = int(sys.stdin.readline())
    s_list = [sys.stdin.readline().strip() for i in range(s_num)]
    v_list = [sys.stdin.readline().strip() for i in range(v_num)]
    o_list = [sys.stdin.readline().strip() for i in range(o_num)]
    for s in s_list:
        for v in v_list:
            for o in o_list:
                print(s,v,o+'.')
    print()