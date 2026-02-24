import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

open_ = [True] * n
S = sum(arr)

out = [str(S)]
for _ in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        j = op[1] - 1
        x = op[2]
        if open_[j]:
            S += (x - arr[j])
        arr[j] = x
    else:
        j = op[1] - 1
        if open_[j]:
            S -= arr[j]
            open_[j] = False
        else:
            S += arr[j]
            open_[j] = True

    out.append(str(S))

print("\n".join(out))